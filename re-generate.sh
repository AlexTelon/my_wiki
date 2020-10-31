#!/bin/bash 
pygmentize -S default -f html > output/codehilite.css
source .env/Scripts/activate
python main.py