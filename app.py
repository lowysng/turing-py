from turing1 import tm1 # tm1 decides the language { w | w = 0 ** 2 ** n where n >= 0 }
from turing2 import tm2 # tm2 decides the language { w#w | w = {0, 1}* }
from turing3 import tm3 # tm3 decides the langauge { (a**i)(b**j)(c**k) | i * j = k and i, j, k >= 1 }
from turing4 import tm4 # tm4 decides the language { w | w contains an equal number of 0s and 1s }
from turing5 import tm5 # tm5 decides the language { w | w contains twice as many 0s as 1s }
from turing6 import tm6 # tm6 decides the language { w | w does not contain twice as many 0s as 1s }
import sys

machines = {
    'tm1': tm1,
    'tm2': tm2,
    'tm3': tm3,
    'tm4': tm4,
    'tm5': tm5,
    'tm6', tm6
}

if (len(sys.argv) != 3):
    print('Usage: py app.py [turing-machine] [input-string]')
    exit()

else:
    machine = machines.get(sys.argv[1])
    machine.load_input(sys.argv[2])
    machine.start_machine()