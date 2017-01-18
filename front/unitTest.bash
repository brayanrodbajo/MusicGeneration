#!/usr/bin/env bash

BASEDIR=`pwd`
EXTLIB_DIR=$BASEDIR/src/ext

FIX=${1-false}
JENKINS=${2-false}

if ${JENKINS}; then
    sh build/install.sh
fi

npm run single_test

if [[ $? -ne 0 ]]; then
  echo "something had a problem. See above."

  exit 1
fi

exit 0
