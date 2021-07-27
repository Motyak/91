#!/usr/bin/env python3
from c import chiffrerStr
 
from sys import argv
import json
 
userInput = " ".join(argv[1:])
res = chiffrerStr(userInput)
# print(chiffrerStr(userInput))
print(json.dumps(res))
 