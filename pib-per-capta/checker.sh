#!/bin/bash

python3.7 script-pib-client.py > output/saida.txt && diff output/fonte1.txt output/saida.txt