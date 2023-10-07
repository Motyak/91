./S0.py | ./S1.py | ./S2.py | ./s.py | grep -oP --color=never -- "- = 0.\(?\K[0-9]{6}" | paste -sd'\n@' | sed 's/@/\n\n/g' | less
