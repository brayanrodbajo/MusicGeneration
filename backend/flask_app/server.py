"""Entry point for the server application."""

from flask import request, Flask, Response, send_file, make_response
from nltk import PCFG, Nonterminal
import json
import os, subprocess
from .chords_generation.learn_trees_music_generate import remove_symbols, generate_sample
from .melodies_generation.bass_generation import write_bass_ly, convert_ly_notation_bass, put_p
from .melodies_generation.piano_generation import convert_ly_notation_piano, annotate_rythm_variations, write_piano_ly, generate_midi
from .melodies_generation.percusion_generation import ly_notation_percusion, get_rythm_tim,get_rythm_congas,get_rythm_cam,get_rythm_gui,get_rythm_mar, write_percusion_ly
from .melodies_generation.wav import combine

app = Flask(__name__)

@app.route('/api/generate', methods=['GET'])
def generate():
    print ('generate')
    tonality = str(request.args.get('tonality'))
    tempo = str(request.args.get('tempo'))
    dest_path = '../front/src/static/'
    print (tonality)
    print (tempo)
    grammar_file = open('flask_app/grammar/pcfg.txt', 'r')
    grammar_str = grammar_file.read()
    grammar_file.close()
    # print ("GRAMÁTICA CON + \n"+grammar_str)
    grammar_str= remove_symbols(grammar_str)
    # print ("GRAMÁTICA SIN + \n"+grammar_str)
    grammar = PCFG.fromstring(grammar_str)
    #grammar = learn_trees(three_trees)
    #f = open("pcfg.txt", "w")
    #f.write(str(grammar))
    #f.close()
    s= Nonterminal('S')
    s = [s]
    chords = generate_sample(grammar, s, [])
    print (chords)
    title = 'Automatic Generated Song'
    composer ='Grupo Niche'
    copyright = 'Brayan Rodríguez'
    time= '2/2'
    chords_without_points = [x for x in chords if x != '.'] #remove points from chords
    #piano
    chords_variations = annotate_rythm_variations(chords_without_points, 4)
    (upper_staff, lower_staff) = convert_ly_notation_piano(chords_variations, tonality)
    file_name_piano = 'piano_salsa'
    write_piano_ly(upper_staff, lower_staff, title, composer, copyright, tonality, time, tempo, file_name_piano)
    generate_midi(file_name_piano)
    #to convert midi into wav
    with open(os.devnull, 'wb') as devnull:
        subprocess.check_call(['timidity', file_name_piano+'.midi','-Ow'], stdout=devnull, stderr=subprocess.STDOUT)
    #bass
    file_name_bass = 'bass_salsa'
    chords_variations = put_p(chords_without_points)
    bass_staff = convert_ly_notation_bass(chords_variations, tonality)
    write_bass_ly(bass_staff, title, composer, copyright, tonality, time, tempo, file_name_bass)
    generate_midi(file_name_bass)
    #to convert midi into wav
    with open(os.devnull, 'wb') as devnull:
        subprocess.check_call(['timidity', file_name_bass+'.midi', '-Ow'], stdout=devnull, stderr=subprocess.STDOUT)
    combine(file_name_piano+'.wav', file_name_bass+'.wav', 'piano_bass.wav')
    #percusion
    measures = len(chords_without_points)/2
    congas = get_rythm_congas()
    staff_c = ly_notation_percusion(congas, measures)
    cam = get_rythm_cam()
    staff_cam = ly_notation_percusion(cam, measures)
    tim = get_rythm_tim()
    staff_t = ly_notation_percusion(tim, measures)
    gui = get_rythm_gui()
    staff_g = ly_notation_percusion(gui, measures)
    mar = get_rythm_mar()
    staff_m = ly_notation_percusion(mar, measures)
    file_name_percusion = 'percusion_salsa'
    write_percusion_ly(staff_c,staff_cam,staff_t,staff_g,staff_m, title, composer, copyright, tonality, time, tempo, file_name_percusion)
    generate_midi(file_name_percusion)
    #to convert midi into wav
    with open(os.devnull, 'wb') as devnull:
        subprocess.check_call(['timidity', file_name_percusion+'.midi', '-Ow'], stdout=devnull, stderr=subprocess.STDOUT)
    file_name_combined = 'combined.wav'
    combine('piano_bass.wav', file_name_percusion+'.wav', file_name_combined)
    #to move to front end
    with open(os.devnull, 'wb') as devnull:
        subprocess.check_call(['mv', file_name_combined, dest_path], stdout=devnull, stderr=subprocess.STDOUT)
        subprocess.check_call(['mv', file_name_bass + '.pdf', dest_path], stdout=devnull, stderr=subprocess.STDOUT)
        subprocess.check_call(['mv', file_name_piano + '.pdf', dest_path], stdout=devnull, stderr=subprocess.STDOUT)
    # combined_file = open('combined.wav', 'rb')
    # combined_content = combined_file.read()
    # resp = make_response(combined_content)
    # combined_file.close()
    # resp = make_response(send_file('../combined.wav'))
    grammar_file = open('flask_app/chords_generation/chosen_prod.txt', 'r')
    chosen_prod = grammar_file.read()
    grammar_file.close()
    resp_json = json.dumps({'error': False, 'components': chosen_prod})
    resp = Response(resp_json)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    # resp.headers['Content-Type'] = 'audio/wav'
    # resp.headers['Content-Disposition'] = 'attachment;filename=combined.wav'
    return resp
    # return resp


def main():
    """Main entry point of the app."""
    try:
        app.run(host='0.0.0.0', debug=True, port=8000, use_reloader=True)
    except Exception as exc:
        print(exc.message)
    finally:
        # get last entry and insert build appended if not completed
        # Do something here
        pass
