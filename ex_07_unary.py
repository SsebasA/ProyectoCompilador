# Author: A01749694 Sebastián Antonio Almanza

from delta import Compiler, Phase

source = '! - - - - - + 2 + 3'

c = Compiler('program')
c.realize(source)
print(c.result)