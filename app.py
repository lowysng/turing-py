from turing1 import tm1 # Turing Machine 1 decides the language A = { w | w = 0 ** 2 ** n where n >= 0 }
from turing2 import tm2 # Turing Machine 2 decides the language B = { w#w | w = {0, 1}* }
from turing3 import tm3 # Turing Machine 3 decides the langauge C = { (a**i)(b**j)(c**k) | i * j = k and i, j, k >= 1 }
import sys

machines = {
    'tm1': tm1,
    'tm2': tm2,
    'tm3': tm3
}

if (len(sys.argv) != 3):
    print('Usage: py app.py [turing-machine] [input-string]')
    exit()

else:
    machine = machines.get(sys.argv[1])
    machine.load_input(sys.argv[2])
    machine.start_machine()