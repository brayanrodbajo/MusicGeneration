#!/bin/bash

# Set up term colors
blue='\033[1;36m'
green='\033[1;32m'
red='\033[0;31m'
white='\033[1;37m'
yellow='\033[1;33m'
NC='\033[0m' # No Color

# Find out where we launched from.
echo -e "${white}Installing SOC UI template.${NC}"
START_DIR=`pwd`

if [ ! -f package.json ]
then
    echo "The root of your SOC UI template repository does not actually appear to be a SOC UI template repository: \033[1;31mABORTING\033[0m"
    exit 1
fi

WSMTool_DIR=$PWD

# Remove any existing modules, this may be a reinstall.
echo -e "${yellow}Removing legacy node modules.${NC}"
cd $WSMTool_DIR
rm -Rf node_modules
rm -Rf src/app/vendor

# Run npm install to get final dependencies and execute postinstall scripts.
echo -e "${white}Installing NPM dependencies.${NC}"
cd $WSMTool_DIR
npm install

echo -e "${white}Installing UI Dependencies.${NC}"
cd $WSMTool_DIR
node_modules/bower/bin/bower install

echo -e "${white}Compiling CSS${NC}"
cd $WSMTool_DIR
npm run less

# Return to where the user executed this script from.
cd $WSMTool_DIR
echo -e "${green}Installing SOC UI template Installation Complete!${NC}"
exit 0
