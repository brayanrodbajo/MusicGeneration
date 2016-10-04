from __future__ import print_function #To write file by print
import os, sys


# chords = ['III', 'i', 'VI', 'iv', 'i', 'i', 'i', 'i', 'i', 'i', 'iv', 'iv', 'VI', 'VI', 'iv', 'iv', 'V7', 'V7', 'V7', 'V7', 'V7', 'V7', 'VII', 'V7', 'i', 'i', 'iv', 'i', 'i', 'i', 'III', 'i', 'i', 'i', 'i', 'ii', 'ii', 'V7', 'i', 'iv', 'VI', 'iv', 'VI', 'ii', 'VI', 'VI', 'VI', 'III', 'i', 'iv', '.', 'i', 'i', 'ii', 'iv', 'VI', 'VI', 'V7', 'VI', 'iv', 'VI', 'VI', 'V7', 'i', 'i', 'VI', 'iv', 'VII', 'V7', 'V7', 'VII', 'VI', 'iv', 'V7', 'VII', 'V7', 'VII', 'i', 'i', 'i', 'i', 'i', 'III', 'i', 'i', 'iv', 'V7', 'VII', 'IV7', 'VII', 'VI', 'iv', 'V7', 'V7', 'i', 'i', 'iv', 'VI', 'VI', 'iv', 'V7', 'VII', 'VII', 'V7', 'V7', 'V7', 'V7', 'V7', 'VI', 'ii', 'V7', 'V7', 'III', 'iv', 'ii', 'VII', 'VII', 'V7', 'VII', 'i', 'i', 'VII', 'VI', 'i', 'i', 'i', 'i', 'i', 'III', 'i', 'III', 'IV7', 'V7', 'VII', 'V7', '.', 'III', 'i', 'i', 'i', '.', 'VII', 'V7', 'iv', 'VI', 'VI', 'ii', 'VII', 'iv', 'iv', 'V7', 'V7', 'VII', 'V7', 'VI', 'VI', 'iv', 'VI', 'VII', 'V7', 'V7', 'V7', 'V7', 'VII', 'VII', 'VII', 'VI', 'iv', 'ii', 'ii', 'V7', 'iv', 'iv', 'VI', 'VI', 'IV7', 'VI', 'VI', 'VII', 'V7', 'i', 'i', 'ii', '.', 'i', 'i', 'VII', 'VII', 'i', 'i', 'i', 'i', 'iv', 'VI', 'VI', 'iv', 'IV7', '.', 'III', 'i', 'ii', 'VI', 'VII', 'VII', 'VII', 'VII', '.', 'VI', 'VII', 'V7', 'III', 'III', 'VI', 'iv', 'V7', 'i', 'i', 'i', 'i', 'iv', 'iv', 'VI', 'iv', 'V7', 'i', 'i', 'ii', 'V7', 'V7', 'III', 'i', 'i', 'III', 'III', 'III', 'i', 'III', 'i', 'i', 'i', 'i', 'i', 'III', 'i', 'i', 'i', 'i', 'iv', 'VI', 'V7', 'V7', 'IV7', 'V7', 'i', 'i', 'i', 'i', 'III', 'i', 'iv', 'V7', 'V7', 'V7', 'VII', 'V7', 'VII', 'III', 'i', 'i', 'i', 'ii', 'V7', 'V7', 'V7', 'V7', 'i', 'V7', 'VII', 'i', 'III', 'VI', 'VI', 'VI', 'VI', 'V7', 'i', 'i', 'i', 'i', 'ii', 'VII', 'VII', 'VII', 'VII', 'VII', 'VII', 'V7', 'VII', 'III', 'III', 'iv', 'VI', 'VI', 'iv', 'V7', 'VII', 'i', 'i', 'VII', 'V7', 'VII', 'VII', 'V7', 'V7', 'VII', 'VII', 'i', 'i', 'i', 'i', '.', 'III', 'i', 'i', 'i', 'ii', 'V7', 'VII', 'i', 'III', 'iv', 'ii', 'VI', 'iv', 'V7', 'V7', 'V7', 'V7', '.', 'III', 'i', 'iv', 'V7', 'V7', 'V7', 'V7', 'V7', 'V7', 'VII', 'VII', 'V7', 'V7', 'i', 'i', 'i', 'i', 'III', 'III', 'VI', 'iv', 'iv', 'iv', 'V7', 'ii', 'V7', 'VII', 'i', 'i', 'i', 'i', 'III', 'III', 'i', 'i', 'i', 'III', 'III', 'i', 'ii', 'V7', 'ii', 'VI', 'VII', 'V7', 'V7', 'V7', 'i', 'III', 'i', 'i', 'III', 'III', 'i', 'i', 'i', 'i', 'iv', 'VI', 'IV7', 'VI', 'V7', 'VII', 'i', 'i', 'i', 'i', 'i', 'i', 'III', 'III', 'i', 'i', 'III', 'i', 'i', 'i', 'i', 'i', 'ii', 'V7', 'iv', 'iv', 'iv', 'iv', 'VII', 'i', 'i', 'i', 'i', '.', 'III', 'i', 'VI', 'iv', 'V7', 'i', 'VI', 'VII', '.', 'i', 'III', 'iv', 'VI', 'V7', 'V7', 'III', 'i', 'iv', 'V7', 'V7', 'IV7', 'VII', 'i', 'III', 'i', 'i', 'ii', 'iv', 'VI', 'iv', 'V7', 'VII', 'V7', 'V7', 'i', 'i', 'iv', 'V7', 'V7', 'VII', 'VII', 'i', 'i', 'V7', 'i', 'i', 'VI', 'iv', 'VI', 'VI', 'V7', 'i', 'III', 'VI', 'iv', 'VI', 'VI', 'V7', 'i', 'ii', 'iv', 'ii', 'VI', 'V7', 'V7', 'V7', 'VII', 'i', 'i', '.']

#The rythmic circle is the third and the fourth chord of every four chords set has one specific variation of the default rythm respectively
def annotate_rythm_variations(chords):
  chords_variations=[chords[0]+'p']
  for i in range(1,len(chords)):
    if i%4==2:
      chords_variations.append(chords[i]+'1')
    elif i%4==3:
      chords_variations.append(chords[i]+'2')
    else: #first and second case
      chords_variations.append(chords[i])

  return chords_variations

#The chords are converted into the lilypond notation according to the set rythm in every chord
def convert_ly_notation(chords, ton):
  if ton=='C':
    i='c'
    ii='d'
    iii='ees'
    iv='f'
    v='g'
    vi='aes'
    vis='a'
    vii='bes'
    viis='b'
  elif ton=='D':
    i='d'
    ii='e'
    iii='f'
    iv='g'
    v='a'
    vi='bes'
    vis='b'
    vii='c'
    viis='cis'

  #p para el compas que empieza de primero
  #1 para el acorde que empieza con dos corcheas en octava
  #2 para el acorde que empieza con dos corcheas en octava y la tercera, quinta simultaneas en corchea y octava corchea
  # default para que empieza
  char2notes = {
    #1st grade
    'ip':("<"+v+"' "+v+"''>8 "+i+"'8 "+iii+"'8 ",i+"4. "),
    'i':("<"+v+"' "+v+"''>4 "+i+"'8 "+iii+"'8 ", i+"2 "),
    'i1':("<"+v+"' "+v+"''>8 <"+v+"' "+v+"''>8 "+i+"'8 "+iii+"'8 ", i+"2 "),
    'i2':("<"+v+"' "+v+"''>8 <"+v+"' "+v+"''>8 <"+i+"' "+iii+"'>8 <"+v+"' "+v+"''>8 ", i+"2 "),
    #2nd grade
    'iip':("<"+vi+"' "+vi+"''>8 "+ii+"'8 "+iv+"'8 ",ii+"4. "),
    'ii':("<"+vi+"' "+vi+"''>4 "+ii+"'8 "+iv+"'8 ", ii+"2 "),
    'ii1':("<"+vi+"' "+vi+"''>8 <"+vi+"' "+vi+"''>8 "+ii+"'8 "+iv+"'8 ", ii+"2 "),
    'ii2':("<"+vi+"' "+vi+"''>8 <"+vi+"' "+vi+"''>8 <"+ii+"' "+iv+"'>8 <"+vi+"' "+vi+"''>8 ", ii+"2 "),
    #3rd grade
    'IIIp':("<"+v+"' "+v+"''>8 "+vii+"'8 "+iii+"'8 ",iii+"4. "),
    'III':("<"+v+"' "+v+"''>4 "+vii+"'8 "+iii+"'8 ", iii+"2 "),
    'III1':("<"+v+"' "+v+"''>8 <"+v+"' "+v+"''>8 "+vii+"'8 "+iii+"'8 ", iii+"2 "),
    'III2':("<"+v+"' "+v+"''>8 <"+v+"' "+v+"''>8 <"+vii+"' "+iii+"'>8 <"+v+"' "+v+"''>8 ", iii+"2 "),
    #4th grade
    'ivp':("<"+vi+"' "+vi+"''>8 "+i+"'8 "+iv+"'8 ",iv+"4. "),
    'iv':("<"+vi+"' "+vi+"''>4 "+i+"'8 "+iv+"'8 ", iv+"2 "),
    'iv1':("<"+vi+"' "+vi+"''>8 <"+vi+"' "+vi+"''>8 "+i+"'8 "+iv+"'8 ", iv+"2 "),
    'iv2':("<"+vi+"' "+vi+"''>8 <"+vi+"' "+vi+"''>8 <"+i+"' "+iv+"'>8 <"+vi+"' "+vi+"''>8 ", iv+"2 "),
    #4th grade
    'IV7p':("<"+vis+"' "+vis+"''>8 "+i+"'8 "+iv+"'8 ",iv+"4. "),
    'IV7':("<"+vis+"' "+vis+"''>4 "+i+"'8 "+iv+"'8 ", iv+"2 "),
    'IV71':("<"+vis+"' "+vis+"''>8 <"+vis+"' "+vis+"''>8 "+i+"'8 "+iv+"'8 ", iv+"2 "),
    'IV72':("<"+vis+"' "+vis+"''>8 <"+vis+"' "+vis+"''>8 <"+i+"' "+iv+"'>8 <"+vis+"' "+vis+"''>8 ", iv+"2 "),
    #5th grade
    'V7p':("<"+v+"' "+v+"''>8 "+viis+"'8 "+ii+"'8 ",v+"4. "),
    'V7':("<"+v+"' "+v+"''>4 "+viis+"'8 "+ii+"'8 ", v+"2 "),
    'V71': ("<"+v+"' "+v+"'>8 <"+v+"' "+v+"'>8 "+viis+"'8 "+ii+"'8 ", v+"2 "),
    'V72': ("<"+v+"' "+v+"'>8 <"+v+"' "+v+"'>8 <"+viis+"' "+ii+"'>8 <"+v+"' "+v+"'>8", v+"2 "),
    #6th grade
    'VIp':("<"+vi+"' "+vi+"''>8 "+i+"'8 "+iii+"'8 ",vi+"4. "),
    'VI':("<"+vi+"' "+vi+"''>4 "+i+"'8 "+iii+"'8 ", vi+"2 "),
    'VI1':("<"+vi+"' "+vi+"''>8 <"+vi+"' "+vi+"''>8 "+i+"'8 "+iii+"'8 ", vi+"2 "),
    'VI2':("<"+vi+"' "+vi+"''>8 <"+vi+"' "+vi+"''>8 <"+i+"' "+iii+"'>8 <"+vi+"' "+vi+"''>8 ", vi+"2 "),
    #7th grade
    'VIIp':("<"+vii+"' "+vii+"''>8 "+ii+"'8 "+iv+"'8 ",vii+"4. "),
    'VII':("<"+vii+"' "+vii+"''>4 "+ii+"'8 "+iv+"'8 ", vii+"2 "),
    'VII1':("<"+vii+"' "+vii+"''>8 <"+vii+"' "+vii+"''>8 "+ii+"'8 "+iv+"'8 ", vii+"2 "),
    'VII2':("<"+vii+"' "+vii+"''>8 <"+vii+"' "+vii+"''>8 <"+ii+"' "+iv+"'>8 <"+vii+"' "+vii+"''>8 ", vii+"2 "),

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
def write_piano_ly(upper_staff, lower_staff, title, composer, copyright, time, tempo, file_name ):
  staff = '\\version "2.18.2"'
  staff += "\n\score{"
  staff += "\n\\new PianoStaff << \n"
  staff += "  \\new Staff {\scoreTempo \\time "+time+" {" + upper_staff + "}}\n"
  staff += "  \\new Staff { \clef bass \scoreTempo \\time "+time+" {" + lower_staff + "}}\n"
  staff += ">>\n"
  staff += "\\midi{} \n}\n"

  header = '\header {'
  header+= '\n title = "' +title+'"'
  header+= '\n composer = "'+composer+'"'
  header += '\n tagline = "Copyright: '+copyright+'"'
  header+= '\n}'

  scoreTempo = "scoreTempo= \\tempo 2="+tempo

  whole_ly = header +"\n"+scoreTempo+ "\n"+staff
  #write to a file
  f = open(file_name+".ly",'w')
  print(whole_ly, file=f)
  f.close()

def generate_midi(file_name):
	os.popen('lilypond '+file_name+'.ly')

if __name__ == '__main__':
  tonality='D'
  title = 'Automatic Generated Song'
  composer ='Grupo Niche'
  copyright = 'Brayan Rodríguez'
  time= '2/2'
  tempo = '100'
  chords_without_points = [x for x in chords if x != '.'] #remove points from chords
  chords_variations = annotate_rythm_variations(chords_without_points)
  (upper_staff, lower_staff) = convert_ly_notation(chords_variations, tonality)
  file_name = "piano_salsa"
  write_piano_ly(upper_staff, lower_staff, title, composer, copyright, time, tempo, file_name)
  generate_midi()
