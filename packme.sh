#!/usr/bin/env bash
OUR_WORKDIR=$(pwd)
ZIPFILE=$OUR_WORKDIR/deployment-pkg.zip
WEBSITE=$OUR_WORKDIR/website-pkg.zip
LOCAL_PKG=packages

UPDATE_ONLY={:-}

echo "*** Cleanup ***"
rm -f $ZIPFILE $WEBSITE
rm -rf $LOCAL_PKG

echo "*** Packing website ***"
zip -r $WEBSITE **/*.py **/*.html

#
# Store environment
# Variant 1, heavy loaded with unused stuff
#
#PATH_TO_ENV=$VIRTUAL_ENV/lib/python3.9/site-packages
#cd $PATH_TO_ENV
#ls -la
#zip -r $ZIPFILE . -x setuptools \*.dist-info pip py
#cd $OUR_WORKDIR

#
# Store environment
# Variant 2, lightweight via pip
#
echo "*** Packing environment ***"
pipenv lock --requirements > requirements.txt
pip install -r requirements.txt --prefix $LOCAL_PKG
PACKAGES_DIR=$(find . -name site-packages)
cd $PACKAGES_DIR
zip -r $ZIPFILE .
cd $OUR_WORKDIR
#
# Store code
#
echo "*** Packing code ***"
zip -gr $ZIPFILE **/*.py *.py

echo "Done. Find zips here: "
ls *.zip