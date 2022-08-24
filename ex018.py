from math import sin, cos, tan, radians
ang = int(input('Digite o ângulo que deseja: '))
sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print('INFORMAÇÕES:\nSEN____{:.2f}\nCOS____{:.2f}\nTAN____{:.2f} '.format(sen, cos, tan))
