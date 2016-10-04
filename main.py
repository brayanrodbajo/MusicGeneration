from chords_generation.learn_trees_music_generate import remove_symbols, generate_sample
from melodies_generation.piano_generation import annotate_rythm_variations, convert_ly_notation, write_piano_ly, generate_midi
from melodies_generation.play_midi import main_play
from nltk import PCFG, Nonterminal
if __name__ =='__main__':
    grammar_file = open("grammar/pcfg.txt", "r")
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
    tonality='D'
    title = 'Automatic Generated Song'
    composer ='Grupo Niche'
    copyright = 'Brayan Rodríguez'
    time= '2/2'
    tempo = '100'
    chords_without_points = [x for x in chords if x != '.'] #remove points from chords
    chords_variations = annotate_rythm_variations(chords_without_points)
    (upper_staff, lower_staff) = convert_ly_notation(chords_variations, tonality)
    file_name = "melodies_generation/piano_salsa"
    write_piano_ly(upper_staff, lower_staff, title, composer, copyright, time, tempo, file_name)
    generate_midi(file_name)
    main_play(file_name+".midi")
