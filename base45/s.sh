#!/bin/sh
 
#./encrypt.py test | ./decrypt.py
 
./encrypt.py lenombremagique > out
./decrypt.py < out
 