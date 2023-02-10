"""4. Que son las expresiones regulares en Python?"""

print("\t-------------------Expresiones--------------------\n\n"
"\tLas expresiones son combinaciones de constantes,\n"
"\tvariables, simbolos y parentesis, que arrojan un valor\n" 
"\ttal y como se conocen en la notacion tradicional\n"
"\tde las matematematicas\n")

import re
palabra1 = 'hornos'
palabra2 = 'horno'
palabra3 = 'estudiar'
 
if re.match(palabra1, palabra2):
   print('palabra1 y palabra2 coinciden')
else:
   print('palabra1 y palabra2 no coinciden')
 
if re.match(palabra1, palabra3):
   print('palabra1 y palabra3 coinciden')
else:
   print('palabra1 y palabra3 no coinciden')