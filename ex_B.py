# Author: A01749694 Sebastián Antonio Almanza

from delta import Compiler, Phase

source = '1 <= 2 == 1 != 0 > 0 < 0 <= 1'

c = Compiler("program")
c.realize(source)
print(c.result)