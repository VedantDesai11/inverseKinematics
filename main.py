import numpy as np
from math import cos, sin, radians, degrees


def rotateX(theta):
	rotMatix = [[1, 0, 0, 0],
	            [0, cos(theta), -sin(theta), 0],
	            [0, sin(theta), cos(theta), 0],
	            [0, 0, 0, 1]]

	return np.array(rotMatix)


def rotateZ(theta):
	rotMatix = [[cos(theta), -sin(theta), 0, 0],
	            [sin(theta), cos(theta), 0, 0],
	            [0, 0, 1, 0],
	            [0, 0, 0, 1]]

	return np.array(rotMatix)


def rotateY(theta):
	rotMatix = [[cos(theta), 0, -sin(theta), 0],
	            [0, 1, 0, 0],
	            [sin(theta), 0, cos(theta), 0],
	            [0, 0, 0, 1]]

	return np.array(rotMatix)


def translate(x=0, y=0, z=0):
	tmatrix = [[1, 0, 0, x],
	           [0, 1, 0, y],
	           [0, 0, 1, z],
	           [0, 0, 0, 1]]

	return np.array(tmatrix)


l0 = 0.25
l1 = 0.2
l2 = 0.2
l3 = 0.15
d1 = 0.04
d2 = 0.04

'''
Incorrect Kinematics !
Joint angles: 5.77830 3.57170 2.47309 2.44618 6.10502 0.00614
Location: -0.01960 0.05654 0.23625
fwd_kin:  1.77824 0.72048 2.77632

Incorrect Kinematics !
Joint angles: 3.87273 2.39098 4.34261 1.96399 3.51189 0.02203
Location: 0.06517 0.00472 -0.10308
fwd_kin:  -1.42622 -1.68370 -2.56009

Incorrect Kinematics !
Joint angles: 5.53469 2.41671 4.44583 2.33820 4.06978 0.00402
Location: -0.06050 0.11078 -0.06443
fwd_kin:  0.03634 2.56000 -1.72896

Incorrect Kinematics !
Joint angles: 4.73583 4.33541 3.12192 3.48684 3.50921 0.02458
Location: 0.03896 0.04494 0.39923
fwd_kin:  -2.16723 1.42637 1.60893
'''

test = '4.73583 4.33541 3.12192 3.48684 3.50921 0.02458'
# test = '0 0 0 0 0 0'
theta = test.split(' ')

theta = [float(item) for item in theta]

m0 = rotateX(theta[4])
m1 = translate(l3, 0, d2)
m2 = rotateY(theta[3])
m3 = translate(l2, d1, 0)
m4 = rotateY(theta[2])
m5 = translate(l1, 0, 0)
m6 = rotateY( + theta[1])
m7 = translate(0, 0, l0)
m8 = rotateZ(theta[0])

answer = np.matmul(m0, m1)
answer = np.matmul(answer, m2)
answer = np.matmul(answer, m3)
answer = np.matmul(answer, m4)
answer = np.matmul(answer, m5)
answer = np.matmul(answer, m6)
answer = np.matmul(answer, m7)
answer = np.matmul(answer, m8)

print(answer)
