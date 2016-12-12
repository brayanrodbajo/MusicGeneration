#Defines the rythm of each percusion instrument
def get_rythm_congas():
    staff = "cgh8 cgho ssh cgho cgh cgho cglo4 cgh8 cgho ssh cgho cgh cgho cglo cglo"
    return staff

def get_rythm_tim():
    staff = "cl4. cl8~ cl4 cl4~ cl4 cl4 cl2"
    return staff

def get_rythm_cam():
    staff = "cb4 cl8 cl cb4 cl8 cl cb4 cl8 cl cb4 cl"
    return staff

def get_rythm_gui():
    staff = "guil4 guis8 guis guil4 guis8 guis guil4 guis8 guis guil4 guis8 guis"
    return staff

def get_rythm_mar():
    staff = "cab8 mar cab cab cab mar cab cab cab mar cab cab cab mar cab cab"
    return staff

#Define the ly notation to a rythm in a number of measures
def ly_notation_percusion(rythm, measures):
    staff = "\\repeat volta "+str(int(measures/2))+ " {"+ rythm +"}"
    return staff

def define_staff(name):
    score = '\n '+name+'Part = \\new DrumStaff \\with {'
    score += '\n instrumentName = "'+name+'"'
    score += '\n shortInstrumentName = "'+name+'"'
    score += '\n drumStyleTable = #timbales-style'
    score += '\n \\override StaffSymbol #\'line-count = #2'
    score += '\n} \\unfoldRepeats {\\'+name+'}'
    return score


#To write in the ly file the staffs of the piano melody
#All the arguments must be strings
def write_percusion_ly(congas_staff, cam_staff, tim_staff, gui_staff, mar_staff, title, composer, copyright, tonality, time, tempo, file_name ):
    staff = '\n congas = \\drummode {'
    staff +='\n\\global'
    staff +='\n'+congas_staff
    staff +='\n}\n'
    staff += '\n tim = \\drummode {'
    staff +='\n\\global'
    staff +='\n'+tim_staff
    staff +='\n}\n'
    staff += '\n cam = \\drummode {'
    staff +='\n\\global'
    staff +='\n'+cam_staff
    staff +='\n}\n'
    staff += '\n gui = \\drummode {'
    staff +='\n\\global'
    staff +='\n'+gui_staff
    staff +='\n}\n'
    staff += '\n mar = \\drummode {'
    staff +='\n\\global'
    staff +='\n'+mar_staff
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


    score = define_staff("congas")+  define_staff("cam")+define_staff("tim") +define_staff("gui")+define_staff("mar")
    midi='\n\\score {'
    midi+='\n<<'
    midi+='\n\\camPart'
    midi+='\n\\congasPart'
    midi+='\n\\timPart'
    midi+='\n\\marPart'
    midi+='\n\\guiPart'
    midi+='\n>>'
    midi+='\n\\layout { }'
    midi+='\n\\midi {'
    midi+='\n\\tempo 2='+tempo
    midi+='\n}'
    midi+='\n}'

    whole_ly = header + globa +  staff + score +midi
    #write to a file
    f = open(file_name+".ly",'w')
    print(whole_ly, file=f)
    f.close()
