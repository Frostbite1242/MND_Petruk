from random import *
from pprint import *

n = int(input('Введіть максимальне значення для рандомного числа'))
mat = [[randint(1,n) for j in range(3)] for i in range(8)]
a0,a1,a2,a3 = [randint(1,n) for k in range(4)]

Y = [(a0+a1*mat[i][0]+a2*mat[i][1]+a3*mat[i][2]) for i in range(8)]
x1 = [mat[i][0] for i in range(8)]
x12 = (max(x1) + min(x1)) / 2
dx1 = x12 - min(x1)
x2 = [mat[i][1] for i in range(8)]
x22 = (max(x2) + min(x2)) / 2
dx2 = x22 - min(x2)
x3 = [mat[i][2] for i in range(8)]
x32 = (max(x3) + min(x3)) / 2
dx3 = x32 - min(x3)
x0 = [x12,x22,x32]
dx = [dx1, dx2, dx3]
matn = [[round((mat[i][j]-x0[j])/dx[j], 3) for j in range(3)] for i in range(8)]

print("----------НАШІ ТОЧКИ----------")
pprint(mat)
print("------------------------------\n а0 = {0}, a1 = {1}, a2 = {2}, a3 = {3}.".format(a0,a1,a2,a3))
print("------------------------------")
for i in range(8):
    print("Y{0} = ".format(i+1)+ str(Y[i]))
print("------------------------------")
for i in range(3):
    print("x0{0} = ".format(i + 1) + str(x0[i]))
print("------------------------------")
for i in range(3):
    print("dx{0} = ".format(i + 1) + str(dx[i]))
print("------------------------------\n Нормована матриця:")
pprint(matn)
print("------------------------------\n Y еталонне: "+ str(round((a0+a1*x12+a2*x22+a3*x32), 3)))
print("------------------------------\nmin(Y) = " + str(min(Y)))
print("------------------------------\n Значення Х, відповідні до min(Y):" + str(mat[Y.index(min(Y))]))