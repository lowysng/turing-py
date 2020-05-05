# Turing Machine

This repo contains code for a Turing Machine implemented in Python.

## Usage

```
$ py app.py [turing-machine] [input-string]
```

## Example
```
$ py app.py tm1 0000
Loading input 0000 ...
Starting Turing Machine...
C: [q1]=>0000
C: [][q2]=>000
C: []x[q3]=>00
C: []x0[q4]=>0
C: []x0x[q3]=>[]
C: []x0[q5]=>x[]
C: []x[q5]=>0x[]
C: [][q5]=>x0x[]
C: [q5]=>[]x0x[]
C: [][q2]=>x0x[]
C: []x[q2]=>0x[]
C: []xx[q3]=>x[]
C: []xxx[q3]=>[]
C: []xx[q5]=>x[]
C: []x[q5]=>xx[]
C: [][q5]=>xxx[]
C: [q5]=>[]xxx[]
C: [][q2]=>xxx[]
C: []x[q2]=>xx[]
C: []xx[q2]=>x[]
C: []xxx[q2]=>[]
C: []xxx[][q_accept]=>[]
-------------------------------------------
Machine halted in the ACCEPT configuration.
-------------------------------------------
```

List of available Turing Machines:

```
L(tm1) = { w | w = 0 ** 2 ** n where n >= 0 }
# accepts strings with number of zeroes that are powers of 2

L(tm2) = { w#w | w = {0, 1}* }
# tests for equality of two strings separated by hash (#)

L(tm3) = { (a**i)(b**j)(c**k) | i * j = k and i, j, k >= 1 }
# computes arithmetic  a * b = c

L(tm4) = { w | w contains an equal number of 0s and 1s }

L(tm5) = { w | w contains twice as many 0s as 1s }

L(tm6) = { w | w does not contain twice as many 0s as 1s }
```