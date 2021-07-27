#!/usr/bin/env python3
from c import dechiffrerToStr
 
import json
 
jsonStr = input()
input = json.loads(jsonStr)
res = dechiffrerToStr([tuple(n) for n in input])
 
print(res)
