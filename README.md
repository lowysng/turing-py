# Turing Machine

This repo contains code for a Turing Machine implemented in Python.

## Usage

```
$ py app.py [turing-machine] [input-string]
```

## Example
```
$ python app.py tm2 01#01

This Turing Machine decides the language B = { w#w | w = {0, 1}* }
Loading input 01#01 ...
Ready to execute, press ENTER to start machine...
Starting Turing Machine...
C: [q1]=>01#01
C: x[q2]=>1#01
C: x1[q2]=>#01
C: x1#[q4]=>01
C: x1[q6]=>#x1
C: x[q7]=>1#x1
C: [q7]=>x1#x1
C: x[q1]=>1#x1
C: xx[q3]=>#x1
C: xx#[q5]=>x1
C: xx#x[q5]=>1
C: xx#[q6]=>xx
C: xx[q6]=>#xx
C: x[q7]=>x#xx
C: xx[q1]=>#xx
C: xx#[q8]=>xx
C: xx#x[q8]=>x
C: xx#xx[q8]=>[]
C: xx#xx[][q_accept]=>[]
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

L(tm7) = { w | w is a string accepted by dfa1 }
# dfa1 accepts strings that start with a 0 and end with a 1
```
