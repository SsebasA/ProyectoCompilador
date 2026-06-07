# Author: A01749694 Sebastián Antonio Almanza

from delta import Compiler, Phase

source = '''
// A line comment.

0

/* 
   A block
   comment.
*/
'''

c = Compiler('program')
c.realize(source)
print(c.result)