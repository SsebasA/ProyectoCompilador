from delta import Compiler, Phase

source = '12+34-56'
c = Compiler("program")
c.realize(source, Phase.CODE_GENERATION)
print(c.wat_code)
#print(c.result)