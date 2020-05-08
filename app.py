from turing1 import tm1 # tm1 decides the language { w | w = 0 ** 2 ** n where n >= 0 }
from turing2 import tm2 # tm2 decides the language { w#w | w = {0, 1}* }
from turing3 import tm3 # tm3 decides the langauge { (a**i)(b**j)(c**k) | i * j = k and i, j, k >= 1 }
from turing4 import tm4 # tm4 decides the language { w | w contains an equal number of 0s and 1s }
from turing5 import tm5 # tm5 decides the language { w | w contains twice as many 0s as 1s }
from turing6 import tm6 # tm6 decides the language { w | w does not contain twice as many 0s as 1s }
from turing7 import tm7 # tm7 decides the language { w | w is a string accepted by dfa1 }
import sys

machines = {
    'tm1': tm1,
    'tm2': tm2,
    'tm3': tm3,
    'tm4': tm4,
    'tm5': tm5,
    'tm6': tm6,
    'tm7': tm7
}

if (len(sys.argv) != 3):
    print('Usage: py app.py [turing-machine] [input-string]')
    exit()

else:
    machine = machines.get(sys.argv[1])
    machine.print_desc()
    machine.load_input(sys.argv[2])
    user = input('Ready to execute, press ENTER to start machine...')
    if user == '':
        machine.start_machine()
    else:
        print('Aborting.')