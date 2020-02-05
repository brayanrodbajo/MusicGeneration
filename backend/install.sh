#!/bin/bash

sudo apt-get install python-dev
sudo apt-get install python3-dev
sudo apt-get install libevent-dev


if ! which gcc
        then sudo apt-get install gcc
fi

if ! which python3
	then sudo apt-get install python3
fi

python3 -m pip install -r requirements.txt 


if ! which lilypond
	then sudo apt-get install lilypond
fi

if ! which timidity++
	then sudo apt-get install timidity++
fi

