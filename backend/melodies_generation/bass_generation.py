# from __future__ import print_function #To write file by printing
import os, sys
# from piano_generation import generate_midi

# Pair of an iterable
def pairwise(iterable):
    "s -> (s0, s1), (s2, s3), (s4, s5), ..."
    a = iter(iterable)
    return zip(a, a)

def put_p(chords):
    return [chords[0]+'p']+ chords[1:]

# Returns the dictionary with the diferent grades of the tonality
def getGrades(ton):
    if ton=='Ces':
        return {
          'i':'ces',
          'ii':'des',
          'iii':'eeses',
          'iv':'fes',
          'v':'ges',
          'vi':'aeses',
          'vis':'aes',
          'vii':'beses',
          'viis':'bes',
        }
    if ton=='C':
        return {
          'i':'c',
          'ii':'d',
          'iii':'ees',
          'iv':'f',
          'v':'g',
          'vi':'aes',
          'vis':'a',
          'vii':'bes',
          'viis':'b',
        }
    if ton=='Cis':
        return {
          'i':'cis',
          'ii':'dis',
          'iii':'e',
          'iv':'fis',
          'v':'gis',
          'vi':'a',
          'vis':'ais',
          'vii':'b',
          'viis':'bis',
        }
    elif ton=='Des':
        return {
        'i':'des',
        'ii':'ees',
        'iii':'fes',
        'iv':'ges',
        'v':'aes',
        'vi':'beses',
        'vis':'bes',
        'vii':'ces',
        'viis':'c',
        }
    elif ton=='D':
        return {
          'i':'d',
          'ii':'e',
          'iii':'f',
          'iv':'g',
          'v':'a',
          'vi':'bes',
          'vis':'b',
          'vii':'c',
          'viis':'cis',
        }
    if ton=='Dis':
        return {
          'i':'dis',
          'ii':'eis',
          'iii':'fis',
          'iv':'gis',
          'v':'ais',
          'vi':'b',
          'vis':'bis',
          'vii':'cis',
          'viis':'cisis',
        }
    elif ton=='Ees':
        return {
          'i':'ees',
          'ii':'f',
          'iii':'ges',
          'iv':'aes',
          'v':'bes',
          'vi':'ces',
          'vis':'c',
          'vii':'des',
          'viis':'d',
        }
    elif ton=='E':
        return {
          'i':'e',
          'ii':'fis',
          'iii':'g',
          'iv':'a',
          'v':'b',
          'vi':'c',
          'vis':'cis',
          'vii':'d',
          'viis':'dis',
        }
    elif ton=='Eis':
        return {
          'i':'eis',
          'ii':'fisis',
          'iii':'gis',
          'iv':'ais',
          'v':'bis',
          'vi':'cis',
          'vis':'cisis',
          'vii':'dis',
          'viis':'disis',
        }
    if ton=='Fes':
        return {
          'i':'fes',
          'ii':'ges',
          'iii':'aeses',
          'iv':'beses',
          'v':'ces',
          'vi':'deses',
          'vis':'des',
          'vii':'eeses',
          'viis':'ees',
        }
    if ton=='F':
        return {
          'i':'f',
          'ii':'g',
          'iii':'aes',
          'iv':'bes',
          'v':'c',
          'vi':'des',
          'vis':'d',
          'vii':'ees',
          'viis':'e',
        }
    if ton=='Fis':
        return {
          'i':'fis',
          'ii':'gis',
          'iii':'a',
          'iv':'b',
          'v':'cis',
          'vi':'d',
          'vis':'dis',
          'vii':'e',
          'viis':'eis',
        }
    elif ton=='Ges':
        return {
          'i':'ges',
          'ii':'aes',
          'iii':'beses',
          'iv':'ces',
          'v':'des',
          'vi':'eeses',
          'vis':'ees',
          'vii':'fes',
          'viis':'f',
        }
    elif ton=='G':
        return {
          'i':'g',
          'ii':'a',
          'iii':'bes',
          'iv':'c',
          'v':'d',
          'vi':'ees',
          'vis':'e',
          'vii':'f',
          'viis':'fis',
        }
    elif ton=='Gis':
        return {
          'i':'gis',
          'ii':'ais',
          'iii':'b',
          'iv':'cis',
          'v':'dis',
          'vi':'e',
          'vis':'eis',
          'vii':'fis',
          'viis':'fisis',
        }
    if ton=='Aes':
        return {
          'i':'aes',
          'ii':'bes',
          'iii':'ces',
          'iv':'des',
          'v':'ees',
          'vi':'fes',
          'vis':'f',
          'vii':'ges',
          'viis':'g',
        }
    if ton=='A':
        return {
          'i':'a',
          'ii':'b',
          'iii':'c',
          'iv':'d',
          'v':'e',
          'vi':'f',
          'vis':'fis',
          'vii':'g',
          'viis':'gis',
        }
    if ton=='Ais':
        return {
          'i':'ais',
          'ii':'bis',
          'iii':'cis',
          'iv':'dis',
          'v':'eis',
          'vi':'fis',
          'vis':'fisis',
          'vii':'gis',
          'viis':'gisis',
        }
    elif ton=='Bes':
        return {
          'i':'bes',
          'ii':'c',
          'iii':'des',
          'iv':'ees',
          'v':'f',
          'vi':'ges',
          'vis':'g',
          'vii':'aes',
          'viis':'a',
        }
    elif ton=='B':
        return {
          'i':'b',
          'ii':'cis',
          'iii':'d',
          'iv':'e',
          'v':'fis',
          'vi':'g',
          'vis':'gis',
          'vii':'a',
          'viis':'ais',
        }
    elif ton=='Bis':
        return {
          'i':'bis',
          'ii':'cisis',
          'iii':'dis',
          'iv':'eis',
          'v':'fisis',
          'vi':'gis',
          'vis':'gisis',
          'vii':'ais',
          'viis':'aisis',
        }

# Convert note in ly notation depending on the repeat of the same note.
def char2notes (grades, char, time, r_time):
    note = ''
    if(r_time==1):
        rythm=['8~','4']
    else:
        rythm=['4~','4.']
    #1st grade
    if(char=='ip'):
        note= grades['i']+',4.'
    elif(char=='i'):
        if(time==1):
            note= grades['i']+','+rythm[0]+' '+grades['i']+','+rythm[1]+' '
        else:
            note=  grades['v']+','+rythm[0]+' '+grades['v']+','+rythm[1]+' '
    #2nd grade
    if(char=='iip'):
        note= grades['ii']+',4.'
    elif(char=='ii'):
        if(time==1):
            note= grades['ii']+','+rythm[0]+' '+grades['ii']+','+rythm[1]+' '
        else:
            note=  grades['vi']+','+rythm[0]+' '+grades['vi']+','+rythm[1]+' '
    #3rd grade
    if(char=='IIIp'):
        note= grades['iii']+',4.'
    elif(char=='III'):
        if(time==1):
            note= grades['iii']+','+rythm[0]+' '+grades['iii']+','+rythm[1]+' '
        else:
            note=  grades['vii']+','+rythm[0]+' '+grades['vii']+','+rythm[1]+' '
    #4th grade
    if(char=='ivp'):
        note= grades['iv']+',4.'
    elif(char=='iv'):
        if(time==1):
            note= grades['iv']+','+rythm[0]+' '+grades['iv']+','+rythm[1]+' '
        else:
            note=  grades['i']+','+rythm[0]+' '+grades['i']+','+rythm[1]+' '
    #4th grade
    if(char=='IV7p'):
        note= grades['iv']+',4.'
    elif(char=='IV7'):
        if(time==1):
            note= grades['iv']+','+rythm[0]+' '+grades['iv']+','+rythm[1]+' '
        else:
            note=  grades['vis']+','+rythm[0]+' '+grades['vis']+','+rythm[1]+' '
    #5th grade,
    if(char=='V7p'):
        note= grades['v']+',4.'
    elif(char=='V7'):
        if(time==1):
            note= grades['v']+','+rythm[0]+' '+grades['v']+','+rythm[1]+' '
        else:
            note=  grades['viis']+','+rythm[0]+' '+grades['viis']+','+rythm[1]+' '
    #6th grade
    if(char=='VIp'):
        note= grades['vi']+',4.'
    elif(char=='VI'):
        if(time==1):
            note= grades['vi']+','+rythm[0]+' '+grades['vi']+','+rythm[1]+' '
        else:
            note=  grades['iii']+','+rythm[0]+' '+grades['iii']+','+rythm[1]+' '
    #7th grade
    if(char=='VIIp'):
        note= grades['vii']+',4.'
    elif(char=='VII'):
        if(time==1):
            note= grades['vii']+','+rythm[0]+' '+grades['vii']+','+rythm[1]+' '
        else:
            note=  grades['iv']+','+rythm[0]+' '+grades['iv']+','+rythm[1]+' '
    return note

#Chords are converted into the lilypond notation according to the set rythm in every chord
def convert_ly_notation_bass(chords, ton):
    grades = getGrades(ton)
    bass_staff = ""
    #Every chord will be annotated in the ly file
    for (current, next) in pairwise(chords):
        note_one = char2notes(grades,current, 1, 2)
        if(current==next):
            note_two = char2notes(grades, next, 2, 1)
        else:
            note_two = char2notes(grades, next, 1, 1)
        bass_staff+=' '+note_one+' '+note_two
    return bass_staff

#To write in the ly file the staffs of the piano melody
#All the arguments must be strings
def write_bass_ly(bass_staff, title, composer, copyright, tonality, time, tempo, file_name ):
    staff = '\n electricBass = {'
    staff +='\n\\global'
    staff +='\n'+bass_staff
    staff +='\n}\n'

    header = '\\version "2.18.2"'
    header += '\n\header {'
    header += '\n title = "' +title+'"'
    header += '\n composer = "'+composer+'"'
    header += '\n copyright = "'+copyright+'"'
    header += '\n}\n'

    # Score global settings
    globa = '\nglobal = {'
    globa += '\\key '+tonality.lower()+' \\minor'
    globa += '\\time '+time
    globa +='\n}\n'

    score = '\n\\score{'
    score += '\n \\new StaffGroup \\with {'
    score += '\n\\consists "Instrument_name_engraver"'
    score += '\ninstrumentName = "Bajo eléctrico"'
    score += '\nshortInstrumentName = "BE"'
    score += '\n} <<'
    score += '\n\\new Staff \\with {'
    score += '\nmidiInstrument = "electric bass (finger)"'
    score += '\n} { \\clef "bass_8" \\electricBass }'
    score += '\n\\new TabStaff \\with {'
    score += '\nstringTunings = #bass-tuning'
    score += '\n} \\electricBass'
    score += '\n>>'
    score += '\n\\layout { }'
    score += '\n\\midi {'
    score += '\n\\tempo 2='+tempo
    score += '\n}'
    score +='\n}'

    whole_ly = header + globa +  staff + score
    #write to a file
    f = open(file_name+".ly",'w')
    print(whole_ly, file=f)
    f.close()


def generate_midi(file_name):
	os.popen('lilypond '+file_name+'.ly')

if __name__ == '__main__':
    chords = ['i', 'III', 'i', 'III', 'i', 'III', 'i', 'i', 'i', 'III', 'VII', 'VII', 'V7', 'VII', 'i', 'i', 'VI', 'VI', 'V7', 'VII', 'VII', 'V7', '.', 'III', 'III', 'ii', 'VII', 'V7', 'VII', 'V7', 'VI', 'VII', 'VII', 'V7', 'V7', 'IV7', 'V7', 'V7', 'i', 'III', 'VI', 'iv', 'VI', 'IV7', 'VII', 'V7', 'i', 'i', 'VI', 'IV7', 'VII', 'i', 'i', 'V7', 'iv', 'III', '.', 'III', 'i', 'i', 'i', 'iv', 'iv', 'IV7', 'V7', 'V7', 'i', 'IV7', 'VII', 'V7', 'V7', 'VII', 'VII', 'V7', 'i', 'i', 'i', 'i', 'V7', 'VII', 'VII', 'V7', 'i', 'III', 'VII', 'VII', 'VI', 'VI', 'iv', 'iv', 'V7', 'V7', 'ii', 'VII', 'V7', 'VII', 'V7', '.', 'VII', 'VII', 'III', 'IV7', 'VI', 'VI', 'iv', 'VII', 'i', 'III', 'IV7', 'VI', 'iv', 'IV7', 'VII', 'V7', 'VII', 'VII', 'III', 'ii', 'VI', 'VII', 'VII', 'i', 'i', 'IV7', 'iv', 'V7', 'V7', 'VII', 'V7', 'V7', 'V7', 'i', 'i', 'iv', 'iv', 'VI', 'ii', 'V7', 'VII', 'III', 'i', 'V7', 'V7', 'i', 'III', 'i', 'III', 'V7', 'III', 'III', 'III', 'III', 'iv', 'V7', 'VII', 'i', 'i', 'i', 'III', '.', 'i', 'i', 'ii', 'VII', 'VII', 'V7', 'V7', 'V7', 'VII', 'ii', 'i', 'III', 'III', 'i', 'iv', 'VII', 'V7', 'VII', 'VII', 'VI', 'III', 'i', 'III', 'i', 'VI', 'VI', 'IV7', 'iv', 'VII', 'V7', 'VI', 'III', 'i', 'i', 'III', 'iv', 'V7', 'V7', 'VI', 'VI', 'III', 'i', 'III', 'i', 'VI', 'ii', 'V7', 'V7', 'VI', 'VI', 'III', 'i', 'i', 'i', 'III', 'III', 'III', 'III', 'VI', 'iv', 'V7', 'IV7', 'i', 'i', 'ii', 'VI', 'VII', 'VII', 'IV7', 'IV7', 'i', 'i', 'III', 'III', 'ii', 'V7', 'IV7', 'ii', 'i', '.', 'i', 'III', 'V7', 'VII', 'VII', 'V7', 'i', 'i', 'i', 'VI', 'V7', 'VII', 'VII', 'VII', 'i', 'V7', 'III', 'III', '.', 'iv', 'VII', 'VII', 'V7', 'V7', 'i', 'VII', 'V7', 'III', 'III', 'i', 'i', 'i', 'i', 'i', 'i', 'i', 'III', 'i', 'III', 'VII', 'V7', 'i', 'i', 'i', 'i', 'VII', 'VII', 'i', 'III', 'i', 'i', 'i', 'V7', 'V7', 'i', 'i', 'i', 'III', 'VII', 'III', 'ii', 'iv', 'IV7', 'ii', 'V7', 'VII', 'V7', 'V7', 'III', 'III', 'ii', 'VII', 'III', 'III', 'VII', 'VII', 'i', 'III', 'VII', 'VII', 'i', 'i', 'VI', 'iv', 'V7', 'V7', 'V7', 'V7', 'i', 'i', 'i', 'i', 'ii', 'VII', 'i', 'VII', 'III', 'V7', 'i', 'i', 'iv', 'ii', 'V7', 'III', 'i', 'V7', 'VII', 'i', 'i', 'iv', 'V7', 'VII', 'VII', 'V7', 'V7', 'V7', 'V7', 'V7', 'III', 'III', 'VI', 'VI', 'iv', 'ii', 'V7', 'III', 'IV7', 'VI', 'iv', 'iv', 'VII', 'i', 'III', 'III', 'i', 'i', 'i', 'III', 'III', 'i', 'i', 'i', 'III', 'i', 'i', 'III', 'i', 'III', 'i', 'iv', 'iv', 'V7', 'V7', 'V7', 'VII', 'III', '.', 'iv', 'IV7', 'V7', 'i', 'i', '.', 'i', 'i', '.']
    chords = put_p(chords)
    tonality='D'
    title = 'Automatic Generated Song'
    composer ='Grupo Niche'
    copyright = 'Brayan Rodríguez'
    time= '2/2'
    tempo = '100'
    chords_without_points = [x for x in chords if x != '.'] #remove points from chords
    bass_staff = convert_ly_notation_bass(chords_without_points, tonality)
    file_name = "bass_salsa_output3"
    write_bass_ly(bass_staff, title, composer, copyright, tonality, time, tempo, file_name)
    generate_midi(file_name)
