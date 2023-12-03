


# HOW TO RUN

```bash
./S0.py | ./S1.py | ./S2.py | ./s.py
```

```bash
2>/dev/null tabs 8 || true; ./S0.py | ./S1.py | ./S2.py | ./S3.py | ./rjust.sh 0 | column -xc80
```

```bash
./input_as_pipeline.sh S2 | ./s.py
```

```bash
./S0.py | ./S1.py | ./S2.py | ./S3.py | ./rjust.sh 0 | perl -e 'while (<> =~ /(..)(..)(..)/){ $sum = $1 + $2 + $3; print "$1$2$3 | $1 + $2 + $3 = $sum\n" }'
```
