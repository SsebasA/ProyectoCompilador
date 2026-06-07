# Author: A01749694 Sebastián Antonio Almanza

from delta import Compiler, Phase

source = '#x0FF1ce'

c = Compiler("program")
c.realize(source, Phase.CODE_GENERATION)
print(c.wat_code)
