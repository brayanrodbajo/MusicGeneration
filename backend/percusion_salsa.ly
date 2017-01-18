\version "2.18.2"
\header {
 title = "Automatic Generated Song"
 composer = "Grupo Niche"
 copyright = "Brayan Rodríguez"
}

global = {\key f \minor\time 2/2
}

 congas = \drummode {
\global
\repeat volta 103 {cgh8 cgho ssh cgho cgh cgho cglo4 cgh8 cgho ssh cgho cgh cgho cglo cglo}
}

 tim = \drummode {
\global
\repeat volta 103 {cl4. cl8~ cl4 cl4~ cl4 cl4 cl2}
}

 cam = \drummode {
\global
\repeat volta 103 {cb4 cl8 cl cb4 cl8 cl cb4 cl8 cl cb4 cl}
}

 gui = \drummode {
\global
\repeat volta 103 {guil4 guis8 guis guil4 guis8 guis guil4 guis8 guis guil4 guis8 guis}
}

 mar = \drummode {
\global
\repeat volta 103 {cab8 mar cab cab cab mar cab cab cab mar cab cab cab mar cab cab}
}

 congasPart = \new DrumStaff \with {
 instrumentName = "congas"
 shortInstrumentName = "congas"
 drumStyleTable = #timbales-style
 \override StaffSymbol #'line-count = #2
} \unfoldRepeats {\congas}
 camPart = \new DrumStaff \with {
 instrumentName = "cam"
 shortInstrumentName = "cam"
 drumStyleTable = #timbales-style
 \override StaffSymbol #'line-count = #2
} \unfoldRepeats {\cam}
 timPart = \new DrumStaff \with {
 instrumentName = "tim"
 shortInstrumentName = "tim"
 drumStyleTable = #timbales-style
 \override StaffSymbol #'line-count = #2
} \unfoldRepeats {\tim}
 guiPart = \new DrumStaff \with {
 instrumentName = "gui"
 shortInstrumentName = "gui"
 drumStyleTable = #timbales-style
 \override StaffSymbol #'line-count = #2
} \unfoldRepeats {\gui}
 marPart = \new DrumStaff \with {
 instrumentName = "mar"
 shortInstrumentName = "mar"
 drumStyleTable = #timbales-style
 \override StaffSymbol #'line-count = #2
} \unfoldRepeats {\mar}
\score {
<<
\camPart
\congasPart
\timPart
\marPart
\guiPart
>>
\layout { }
\midi {
\tempo 2=100
}
}
