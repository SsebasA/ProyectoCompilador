# Author: A01749694 Sebastián Antonio Almanza

from delta import Compiler, Phase

source = '''
    var x, y;
    y = 20;
    x = x + 1;
    x + y

'''

c = Compiler("program")
c.realize(source, Phase.EVALUATION)
#print(c.parse_tree_str)
print(c.result)
