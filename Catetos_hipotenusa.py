from math import sin, cos, tan, radians, trunc
angulo = float(input('Digite o angulo que você deseja: '))
print('Seno:{:.2f} \nCosseno:{:.2f} \nTangente:{:.2f}'.format(sin(radians(angulo)),cos(radians(angulo)),tan(radians(angulo))))