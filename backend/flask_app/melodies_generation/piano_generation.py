# from __future__ import print_function #To write file by printing
import subprocess, sys, os

#The rythmic circle is the third and the fourth chord of every four chords set has one specific variation of the default rythm respectively
def annotate_rythm_variations(chords, n_var):
  chords_variations=[chords[0]+'p']
  for i in range(1,len(chords)):
    if i%n_var==1:
      chords_variations.append(chords[i])
    elif i%n_var==2:
      chords_variations.append(chords[i]+'1')
    elif i%n_var==3:
      chords_variations.append(chords[i]+'2')
    else: #%4 case
      chords_variations.append(chords[i]+'3')

  return chords_variations

# Returns the dictionary with the diferent grades of the tonality
def getGrades(ton):
    print("ton "+ton)
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

#The chords are converted into the lilypond notation according to the set rythm in every chord
def convert_ly_notation_piano(chords, ton):
  grades = getGrades(ton)
  rythm=[]
  rythm.append(['8~','4'])
  rythm.append(['4~','4.'])

  #p means the first measure of the melody
  #1 for the chord which begins with two quarters simultaneous in octave
  #2 for the chord which begins with two quarters simultaneous in octave, then the third and fifth grade simultaneous in quarter and again an octave in quarter
  char2notes = {
    #1st grade
    'ip':("<"+grades['v']+"' "+grades['v']+"''>4 <"+grades['i']+"'' "+grades['iii']+"''>4 ",grades['i']+"4. "),
    'i':("r8 <"+grades['v']+"' "+grades['v']+"''>4 ",grades['i']+rythm[0][0]+" "+grades['i']+rythm[0][1]),
    'i1':("<"+grades['v']+"' "+grades['v']+"''>8 <"+grades['v']+"' "+grades['v']+"''>4 <"+grades['i']+"'' "+grades['iii']+"''>4 ",grades['i']+rythm[1][0]+" "+grades['i']+rythm[1][1]),
    'i2':("r4 <"+grades['v']+"' "+grades['v']+"''>4 ",grades['i']+rythm[0][0]+" "+grades['i']+rythm[0][1]),
    'i3':("<"+grades['v']+"' "+grades['v']+"''>4 <"+grades['i']+"'' "+grades['iii']+"''>4 ",grades['i']+rythm[1][0]+" "+grades['i']+ rythm[1][1]),
    #2nd grade
    'iip':("<"+grades['vi']+"' "+grades['vi']+"''>4 <"+grades['ii']+"'' "+grades['iv']+"''>4 ",grades['ii']+"4. "),
    'ii':("r8 <"+grades['vi']+"' "+grades['vi']+"''>4 ", grades['ii']+rythm[0][0]+" "+grades['ii']+ rythm[0][1]),
    'ii1':("<"+grades['vi']+"' "+grades['vi']+"''>8 <"+grades['vi']+"' "+grades['vi']+"''>4 <"+grades['ii']+"'' "+grades['iv']+"''>4 ", grades['ii']+rythm[1][0]+" "+grades['ii']+ rythm[1][1]),
    'ii2':("r4 <"+grades['vi']+"' "+grades['vi']+"''>4 ", grades['ii']+rythm[0][0]+" "+grades['ii']+ rythm[0][1]),
    'ii3':("<"+grades['vi']+"' "+grades['vi']+"''>4 <"+grades['ii']+"'' "+grades['iv']+"''>4 ",grades['ii']+rythm[1][0]+" "+grades['ii']+ rythm[1][1]),
    #3rd grade
    'IIIp':("<"+grades['v']+"' "+grades['v']+"''>4 <"+grades['vii']+"' "+grades['iii']+"''>4 ",grades['iii']+"4. "),
    'III':("r8 <"+grades['v']+"' "+grades['v']+"''>4 ",grades['iii']+rythm[0][0]+" "+grades['iii']+ rythm[0][1]),
    'III1':("<"+grades['v']+"' "+grades['v']+"''>8 <"+grades['v']+"' "+grades['v']+"''>4 <"+grades['vii']+"' "+grades['iii']+"''>4 ",grades['iii']+rythm[1][0]+" "+grades['iii']+ rythm[1][1]),
    'III2':("r4 <"+grades['v']+"' "+grades['v']+"''>4 ",grades['iii']+rythm[0][0]+" "+grades['iii']+ rythm[0][1]),
    'III3':("<"+grades['v']+"' "+grades['v']+"''>4 <"+grades['vii']+"' "+grades['iii']+"''>4 ",grades['iii']+rythm[1][0]+" "+grades['iii']+ rythm[1][1]),
    #4th grade
    'ivp':("<"+grades['vi']+"' "+grades['vi']+"''>4 <"+grades['i']+"'' "+grades['iv']+"''>4 ",grades['iv']+"4. "),
    'iv':("r8 <"+grades['vi']+"' "+grades['vi']+"''>4 ",grades['iv']+rythm[0][0]+" "+grades['iv']+ rythm[0][1]),
    'iv1':("<"+grades['vi']+"' "+grades['vi']+"''>8 <"+grades['vi']+"' "+grades['vi']+"''>4 <"+grades['i']+"'' "+grades['iv']+"''>4 ",grades['iv']+rythm[1][0]+" "+grades['iv']+ rythm[1][1]),
    'iv2':("r4 <"+grades['vi']+"' "+grades['vi']+"''>4 ",grades['iv']+rythm[0][0]+" "+grades['iv']+ rythm[0][1]),
    'iv3':("<"+grades['vi']+"' "+grades['vi']+"''>4 <"+grades['i']+"'' "+grades['iv']+"''>4 ",grades['iv']+rythm[1][0]+" "+grades['iv']+ rythm[1][1]),
    #4th grade
    'IV7p':("<"+grades['vis']+"' "+grades['vis']+"''>4 <"+grades['i']+"'' "+grades['iv']+"''>4 ",grades['iv']+"4. "),
    'IV7':("r8 <"+grades['vis']+"' "+grades['vis']+"''>4 ",grades['iv']+rythm[0][0]+" "+grades['iv']+ rythm[0][1]),
    'IV71':("<"+grades['vis']+"' "+grades['vis']+"''>8 <"+grades['vis']+"' "+grades['vis']+"''>4 <"+grades['i']+"'' "+grades['iv']+"''>4 ",grades['iv']+rythm[1][0]+" "+grades['iv']+ rythm[1][1]),
    'IV72':("r4 <"+grades['vis']+"' "+grades['vis']+"''>4 ",grades['iv']+rythm[0][0]+" "+grades['iv']+ rythm[0][1]),
    'IV73':("<"+grades['vis']+"' "+grades['vis']+"''>4 <"+grades['i']+"'' "+grades['iv']+"''>4 ",grades['iv']+rythm[1][0]+" "+grades['iv']+ rythm[1][1]),
    #5th grade
    'V7p':("<"+grades['v']+"' "+grades['v']+"''>4 <"+grades['viis']+"' "+grades['ii']+"''>4 ",grades['v']+"4. "),
    'V7':("r8 <"+grades['v']+"' "+grades['v']+"''>4 ",grades['v']+rythm[0][0]+" "+grades['v']+ rythm[0][1]),
    'V71': ("<"+grades['v']+"' "+grades['v']+"''>8 <"+grades['v']+"' "+grades['v']+"''>4 <"+grades['viis']+"' "+grades['ii']+"''>4 ",grades['v']+rythm[1][0]+" "+grades['v']+ rythm[1][1]),
    'V72': ("r4 <"+grades['v']+"' "+grades['v']+"''>4 ",grades['v']+rythm[0][0]+" "+grades['v']+ rythm[0][1]),
    'V73':("<"+grades['v']+"' "+grades['v']+"''>4 <"+grades['viis']+"' "+grades['ii']+"''>4 ",grades['v']+rythm[1][0]+" "+grades['v']+ rythm[1][1]),
    #6th grade
    'VIp':("<"+grades['vi']+"' "+grades['vi']+"''>4 <"+grades['i']+"'' "+grades['iii']+"''>4 ",grades['vi']+"4. "),
    'VI':("r8 <"+grades['vi']+"' "+grades['vi']+"''>4 ",grades['vi']+rythm[0][0]+" "+grades['vi']+ rythm[0][1]),
    'VI1':("<"+grades['vi']+"' "+grades['vi']+"''>8 <"+grades['vi']+"' "+grades['vi']+"''>4 <"+grades['i']+"'' "+grades['iii']+"''>4 ",grades['vi']+rythm[1][0]+" "+grades['vi']+ rythm[1][1]),
    'VI2':("r4 <"+grades['vi']+"' "+grades['vi']+"''>4 ",grades['vi']+rythm[0][0]+" "+grades['vi']+ rythm[0][1]),
    'VI3':("<"+grades['vi']+"' "+grades['vi']+"''>4 <"+grades['i']+"'' "+grades['iii']+"''>4 ",grades['vi']+rythm[1][0]+" "+grades['vi']+ rythm[1][1]),
    #7th grade
    'VIIp':("<"+grades['vii']+"' "+grades['vii']+"''>4 <"+grades['ii']+"'' "+grades['iv']+"''>4 ",grades['vii']+"4. "),
    'VII':("r8 <"+grades['vii']+"' "+grades['vii']+"''>4 ",grades['vii']+rythm[0][0]+" "+grades['vii']+ rythm[0][1]),
    'VII1':("<"+grades['vii']+"' "+grades['vii']+"''>8 <"+grades['vii']+"' "+grades['vii']+"''>4 <"+grades['ii']+"'' "+grades['iv']+"''>4 ",grades['vii']+rythm[1][0]+" "+grades['vii']+ rythm[1][1]),
    'VII2':("r4 <"+grades['vii']+"' "+grades['vii']+"''>4 ",grades['vii']+rythm[0][0]+" "+grades['vii']+ rythm[0][1]),
    'VII3':("<"+grades['vii']+"' "+grades['vii']+"''>4 <"+grades['ii']+"'' "+grades['iv']+"''>4 ",grades['vii']+rythm[1][0]+" "+grades['vii']+ rythm[1][1]),
  }

  upper_staff = ""
  lower_staff = ""
  #Every chord will be annotated in the ly file
  for chord in chords:
      (u,l) = char2notes[chord]
      upper_staff += u
      lower_staff += l
  return (upper_staff, lower_staff)

#To write in the ly file the staffs of the piano melody
#All the arguments must be strings
def write_piano_ly(upper_staff, lower_staff, title, composer, copyright, tonality, time, tempo, file_name ):
  staff = '\n right = {'
  staff +='\n\\global'
  staff +='\n'+upper_staff
  staff +='\n}\n'

  staff += '\n left = {'
  staff +='\n\\global'
  staff +='\n'+lower_staff
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
  score += '\n \\new PianoStaff \\with {'
  score += '\ninstrumentName = "Piano"'
  score += '\nshortInstrumentName = "P"'
  score += '\n} <<'
  score += '\n\\new Staff  = "right" \\with {'
  score += '\nmidiInstrument = "acoustic grand"'
  score += '\n} \\right '
  score += '\n\\new Staff  = "left" \\with {'
  score += '\nmidiInstrument = "acoustic grand"'
  score += '\n} {\\clef bass \\left }'
  score += '\n>>'
  score += '\n\\layout { }'
  score += '\n\\midi {'
  score += '\n\\tempo 2='+tempo
  score += '\n}'
  score +='\n}'

  whole_ly = header + globa +staff + score
  #write to a file
  f = open(file_name+".ly",'w')
  print(whole_ly, file=f)
  f.close()

def generate_midi(file_name):
    with open(os.devnull, 'wb') as devnull:
        subprocess.check_call(['lilypond', file_name+'.ly'], stdout=devnull, stderr=subprocess.STDOUT)

if __name__ == '__main__':
    chords = ['i', 'III', 'i', 'III', 'i', 'III', 'i', 'i', 'i', 'III', 'VII', 'VII', 'V7', 'VII', 'i', 'i', 'VI', 'VI', 'V7', 'VII', 'VII', 'V7', '.', 'III', 'III', 'ii', 'VII', 'V7', 'VII', 'V7', 'VI', 'VII', 'VII', 'V7', 'V7', 'IV7', 'V7', 'V7', 'i', 'III', 'VI', 'iv', 'VI', 'IV7', 'VII', 'V7', 'i', 'i', 'VI', 'IV7', 'VII', 'i', 'i', 'V7', 'iv', 'III', '.', 'III', 'i', 'i', 'i', 'iv', 'iv', 'IV7', 'V7', 'V7', 'i', 'IV7', 'VII', 'V7', 'V7', 'VII', 'VII', 'V7', 'i', 'i', 'i', 'i', 'V7', 'VII', 'VII', 'V7', 'i', 'III', 'VII', 'VII', 'VI', 'VI', 'iv', 'iv', 'V7', 'V7', 'ii', 'VII', 'V7', 'VII', 'V7', '.', 'VII', 'VII', 'III', 'IV7', 'VI', 'VI', 'iv', 'VII', 'i', 'III', 'IV7', 'VI', 'iv', 'IV7', 'VII', 'V7', 'VII', 'VII', 'III', 'ii', 'VI', 'VII', 'VII', 'i', 'i', 'IV7', 'iv', 'V7', 'V7', 'VII', 'V7', 'V7', 'V7', 'i', 'i', 'iv', 'iv', 'VI', 'ii', 'V7', 'VII', 'III', 'i', 'V7', 'V7', 'i', 'III', 'i', 'III', 'V7', 'III', 'III', 'III', 'III', 'iv', 'V7', 'VII', 'i', 'i', 'i', 'III', '.', 'i', 'i', 'ii', 'VII', 'VII', 'V7', 'V7', 'V7', 'VII', 'ii', 'i', 'III', 'III', 'i', 'iv', 'VII', 'V7', 'VII', 'VII', 'VI', 'III', 'i', 'III', 'i', 'VI', 'VI', 'IV7', 'iv', 'VII', 'V7', 'VI', 'III', 'i', 'i', 'III', 'iv', 'V7', 'V7', 'VI', 'VI', 'III', 'i', 'III', 'i', 'VI', 'ii', 'V7', 'V7', 'VI', 'VI', 'III', 'i', 'i', 'i', 'III', 'III', 'III', 'III', 'VI', 'iv', 'V7', 'IV7', 'i', 'i', 'ii', 'VI', 'VII', 'VII', 'IV7', 'IV7', 'i', 'i', 'III', 'III', 'ii', 'V7', 'IV7', 'ii', 'i', '.', 'i', 'III', 'V7', 'VII', 'VII', 'V7', 'i', 'i', 'i', 'VI', 'V7', 'VII', 'VII', 'VII', 'i', 'V7', 'III', 'III', '.', 'iv', 'VII', 'VII', 'V7', 'V7', 'i', 'VII', 'V7', 'III', 'III', 'i', 'i', 'i', 'i', 'i', 'i', 'i', 'III', 'i', 'III', 'VII', 'V7', 'i', 'i', 'i', 'i', 'VII', 'VII', 'i', 'III', 'i', 'i', 'i', 'V7', 'V7', 'i', 'i', 'i', 'III', 'VII', 'III', 'ii', 'iv', 'IV7', 'ii', 'V7', 'VII', 'V7', 'V7', 'III', 'III', 'ii', 'VII', 'III', 'III', 'VII', 'VII', 'i', 'III', 'VII', 'VII', 'i', 'i', 'VI', 'iv', 'V7', 'V7', 'V7', 'V7', 'i', 'i', 'i', 'i', 'ii', 'VII', 'i', 'VII', 'III', 'V7', 'i', 'i', 'iv', 'ii', 'V7', 'III', 'i', 'V7', 'VII', 'i', 'i', 'iv', 'V7', 'VII', 'VII', 'V7', 'V7', 'V7', 'V7', 'V7', 'III', 'III', 'VI', 'VI', 'iv', 'ii', 'V7', 'III', 'IV7', 'VI', 'iv', 'iv', 'VII', 'i', 'III', 'III', 'i', 'i', 'i', 'III', 'III', 'i', 'i', 'i', 'III', 'i', 'i', 'III', 'i', 'III', 'i', 'iv', 'iv', 'V7', 'V7', 'V7', 'VII', 'III', '.', 'iv', 'IV7', 'V7', 'i', 'i', '.', 'i', 'i', '.']
    tonality='D'
    title = 'Automatic Generated Song'
    composer ='Grupo Niche'
    copyright = 'Brayan Rodríguez'
    time= '2/2'
    tempo = '100'
    chords_without_points = [x for x in chords if x != '.'] #remove points from chords
    chords_variations = annotate_rythm_variations(chords_without_points, 4)
    (upper_staff, lower_staff) = convert_ly_notation_piano(chords_variations, tonality)
    file_name = "piano_salsa_output3"
    write_piano_ly(upper_staff, lower_staff, title, composer, copyright, tonality, time, tempo, file_name)
    generate_midi(file_name)
