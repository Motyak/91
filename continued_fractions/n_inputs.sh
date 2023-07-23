#!/usr/bin/env bash
cd "$(dirname "$0")"
../orderNaturally.py | perl -ne 'print if s/\[(.*9, 81.*)\]/$1/' | tr -d ','
