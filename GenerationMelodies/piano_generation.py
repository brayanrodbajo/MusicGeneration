from __future__ import print_function #To write file by print
import os, sys


chords = ['VII', 'i', 'i', 'i', 'i', 'i', 'i', 'i', 'i', '.', 'i', 'i', 'III', 'i', 'V7', 'V7', 'V7', 'VII', 'VII', 'V7', 'VII', 'VII', 'i', 'i', 'VI', 'VI', 'VI', 'iv', 'iv', 'iv', 'iv', 'VI', 'VII', 'VII', '.', 'III', 'i', 'iv', 'VI', 'V7', 'V7', 'V7', 'V7', 'VII', 'VII', 'VII', 'V7', 'VI', 'VII', 'i', 'i', 'i', 'III', 'iv', 'VII', 'V7', 'V7', 'V7', 'V7', 'V7', 'VII', 'VII', 'V7', 'VII', 'i', 'i', 'iv', 'V7', 'V7', 'iv', 'ii', 'VII', 'V7', 'III', 'i', 'iv', 'iv', 'VII', 'VII', 'III', 'i', 'iv', 'iv', 'V7', 'V7', 'V7', 'VII', 'i', 'i', 'VII', 'ii', 'i', 'i', 'V7', 'VI', 'ii', 'V7', 'V7', '.', 'i', 'i', 'i', 'VI', 'V7', 'V7', 'VII', 'V7', 'i', 'i', 'i', 'i', 'i', 'III', 'i', 'i', 'VII', 'VII', 'i', 'i', 'i', 'i', '.', 'i', 'i', 'V7', 'IV7', 'VII', 'V7', 'iv', 'V7', 'iv', 'III', 'i', 'iv', 'VI', 'V7', 'V7', 'VII', 'IV7', 'i', 'i', '.', 'i', 'III', 'i', 'i', 'i', 'III', 'i', 'i', 'iv', 'V7', 'i', 'i', 'i', 'i', 'i', 'i', 'VI', 'V7', 'V7', 'V7', 'VII', '.', 'VI', 'IV7', 'III', 'i', 'i', 'III', 'VII', 'III', 'i', 'i', 'III', 'iv', 'ii', 'ii', 'ii', 'VII', 'i', 'ii', 'V7', 'V7', 'III', 'i', 'VII', 'i', 'i', 'i', 'i', 'VI', 'iv', 'iv', 'VI', 'IV7', 'V7', 'V7', 'IV7', 'i', 'i', 'VII', 'i', 'i', 'i', 'III', 'V7', 'IV7', 'i', 'i', 'VI', 'V7', 'VII', 'i', 'i', 'i', 'i', 'VII', 'VII', 'i', 'i', 'III', 'i', 'V7', 'V7', 'i', 'III', 'VI', 'IV7', 'V7', 'V7', 'VII', 'III', 'III', '.', 'VI', '.']

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

def generate_midi():
	os.popen('lilypond '+file_name+'.ly')

if __name__ == '__main__':
  tonality='D'
  title = 'Automatic Generated Song'
  composer ='Grupo Niche'
  copyright = 'Brayan Rodríguez'
  time= '2/2'
  tempo = '100'
  chords_without_points = [x for x in chords if x != '.']
  chords_variations = annotate_rythm_variations(chords_without_points)
  (upper_staff, lower_staff) = convert_ly_notation(chords_variations, tonality)
  file_name = "piano_salsa"
  write_piano_ly(upper_staff, lower_staff, title, composer, copyright, time, tempo, file_name)
  generate_midi()
