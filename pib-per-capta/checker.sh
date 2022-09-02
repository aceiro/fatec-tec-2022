#!/bin/bash

python3.7 script-pib.py > output/saida.txt && diff output/fonte1.txt output/saida.txt