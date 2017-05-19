#!/bin/bash
if ! which python3
	then sudo apt-get install python3
fi

pip3 install -r requirements.txt 


if ! which lilypond
	then sudo apt-get install lilypond
fi

if ! which timidity++
	then sudo apt-get install timidity++
fi

