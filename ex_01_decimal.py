# Author: A01749694 Sebastián Antonio Almanza

from delta import Compiler, Phase

source = '42'
c = Compiler("program")
c.realize(source, Phase.CODE_GENERATION) 
print(c.wat_code)