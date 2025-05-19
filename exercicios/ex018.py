import math
ang = int(input('Qual o ângulo? '))
rad = math.radians(ang)
sen = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)
print('O valor do seno é {:.2f}, o valor do cosseno é {:.2f}, e o valor da tangente é {:.2f}.'.format(sen, cos, tan))
