#!/bin/bash
mkdir .tmp
cd .tmp
cp ../*.py .
cp ../*.txt .

if [ ! -d deps ]
then
  pip3 install -t deps -r testrequirements.txt --no-cache
fi

cp -rf ../../realtimeawssecretsmngr ./deps
pytest -s -v *_test.py
