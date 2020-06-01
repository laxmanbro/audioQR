import numpy as np
import math
# from scipy import special

from matplotlib import pyplot as plt
monalisa = np.load("mss.npy")
plt.imshow(monalisa, 'gray')
# plt.show()python


mona_arr = []
for i in range(400):  # changing as 1D array
    for j in range(300):
        mona_arr.append(monalisa[i][j])
mona_ar = np.array(mona_arr)


Gt = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [
              0, 1, 1, 0], [1, 0, 1, 0], [1, 1, 1, 0], [1, 1, 0, 1], [1, 0, 1, 1], [0, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 1]])
x = 0
ch_enc_arr = []
puppy = 0

# print(mona_ar)
for i in range(30000):
    x = np.array([mona_ar[puppy], mona_ar[puppy+1],
                  mona_ar[puppy+2], mona_ar[puppy+3]])
    y = np.matmul(Gt, x)
    for j in range(12):
        ch_enc_arr.append(y[j])
    puppy = puppy+4

# print(ch_enc_arr)
ch_enc_arr = np.array(ch_enc_arr)
ch_enc_arr = ch_enc_arr % 2
# print(ch_enc_arr)


ch_enc_arr = -2*ch_enc_arr+1  # x to +1 or -1 conversion


# print(mona_ar)
# t = np.arange(0, 0.0055, 0.000001/50)

fc = 2000000.00  # carrier frequency
Ts = 1/50000000.00  # sampling time
St = []

# print(St[2])
n = 0


for i in range(180000):  # defining S(t)
    for j in range(50):
        St.append(ch_enc_arr[2*i]*np.cos(2*np.pi*fc*n*Ts) +
                  ch_enc_arr[2*i+1]*np.sin(2*np.pi*fc*n*Ts))
        n = n+1

# print n
St_arr = np.array(St)

# St_square = St_arr*St_arr
# Eb = np.sum(St_square)/(2*5500)

T = 0.000001
n = 12.00
k = 4.00
Eb = T/2.00*n/k  # energy per bit
# print Eb
x = 4.00  # Eb/No in decibels


std = np.sqrt(Eb*1/Ts*0.5*pow(10.00, -x/10.00))  # standard deviation


# St_arr = St_arr*St_arr
# sum = np.sum(St_arr)
# print(sum)
samples = np.random.normal(0, std, 180000*50)  # white gaussian noise

rt = St_arr + samples   # recived signal

# print(rt)


def z1(n):  # 4-QAM constellations
    return (np.cos(2*np.pi*fc*n*Ts) + np.sin(2*np.pi*fc*n*Ts))


def z2(n):
    return (-np.cos(2*np.pi*fc*n*Ts) + np.sin(2*np.pi*fc*n*Ts))


def z3(n):
    return (-np.cos(2*np.pi*fc*n*Ts) - np.sin(2*np.pi*fc*n*Ts))


def z4(n):
    return (np.cos(2*np.pi*fc*n*Ts) - np.sin(2*np.pi*fc*n*Ts))


countZ1 = 0
countZ2 = 0
countZ3 = 0
countZ4 = 0

n = 0
new_arr = []


for j in range(180000):
    a1 = 0
    a2 = 0
    a3 = 0
    a4 = 0
    for i in range(50):
        a1 = a1 + (rt[n]-z1(n))**2
        # print((rt[n]-z1(n))**2)
        # print(a1)
        a2 = a2 + (rt[n]-z2(n))**2
        a3 = a3 + (rt[n]-z3(n))**2
        a4 = a4 + (rt[n]-z4(n))**2
        n = n+1

    d1 = np.sqrt(a1)
#     print d1
    d2 = np.sqrt(a2)
    d3 = np.sqrt(a3)
    d4 = np.sqrt(a4)

    min_dist = min([d1, d2, d3, d4])  # minimum distance calculation

#     print min_dist

    if min_dist == d1:
        new_arr.append(1)
        new_arr.append(1)
    elif min_dist == d2:
        new_arr.append(-1)
        new_arr.append(1)
    elif min_dist == d3:
        new_arr.append(-1)
        new_arr.append(-1)
    else:
        new_arr.append(1)
        new_arr.append(-1)


# print(new_arr)

new = np.array(new_arr)
new_arr = (new-1)/-2

# print len(new_arr)


# rows, cols = (110, 100)
# ans_arr = [[0]*cols]*rows
# p = 0

# print(new_arr)


ch1 = np.array(np.matmul(Gt, np.array([0, 0, 0, 0]))) % 2
ch2 = np.array(np.matmul(Gt, np.array([0, 0, 0, 1]))) % 2
ch3 = np.array(np.matmul(Gt, np.array([0, 0, 1, 0]))) % 2
ch4 = np.array(np.matmul(Gt, np.array([0, 0, 1, 1]))) % 2
ch5 = np.array(np.matmul(Gt, np.array([0, 1, 0, 0]))) % 2
ch6 = np.array(np.matmul(Gt, np.array([0, 1, 0, 1]))) % 2
ch7 = np.array(np.matmul(Gt, np.array([0, 1, 1, 0]))) % 2
ch8 = np.array(np.matmul(Gt, np.array([0, 1, 1, 1]))) % 2
ch9 = np.array(np.matmul(Gt, np.array([1, 0, 0, 0]))) % 2
ch10 = np.array(np.matmul(Gt, np.array([1, 0, 0, 1]))) % 2
ch11 = np.array(np.matmul(Gt, np.array([1, 0, 1, 0]))) % 2
ch12 = np.array(np.matmul(Gt, np.array([1, 0, 1, 1]))) % 2
ch13 = np.array(np.matmul(Gt, np.array([1, 1, 0, 0]))) % 2
ch14 = np.array(np.matmul(Gt, np.array([1, 1, 0, 1]))) % 2
ch15 = np.array(np.matmul(Gt, np.array([1, 1, 1, 0]))) % 2
ch16 = np.array(np.matmul(Gt, np.array([1, 1, 1, 1]))) % 2

# print ch1

y = []
final_arr = []
temp = 0

for i in range(30000):
    gandu = np.array([new_arr[temp], new_arr[temp+1], new_arr[temp+2], new_arr[temp+3],
                      new_arr[temp+4], new_arr[temp+5], new_arr[temp+6], new_arr[temp+7], new_arr[temp+8], new_arr[temp+9], new_arr[temp+10], new_arr[temp+11]])
    a1 = np.sum(np.bitwise_xor(ch1, gandu))
    a2 = np.sum(np.bitwise_xor(ch2, gandu))
    a3 = np.sum(np.bitwise_xor(ch3, gandu))
    a4 = np.sum(np.bitwise_xor(ch4, gandu))
    a5 = np.sum(np.bitwise_xor(ch5, gandu))
    a6 = np.sum(np.bitwise_xor(ch6, gandu))
    a7 = np.sum(np.bitwise_xor(ch7, gandu))
    a8 = np.sum(np.bitwise_xor(ch8, gandu))
    a9 = np.sum(np.bitwise_xor(ch9, gandu))
    a10 = np.sum(np.bitwise_xor(ch10, gandu))
    a11 = np.sum(np.bitwise_xor(ch11, gandu))
    a12 = np.sum(np.bitwise_xor(ch12, gandu))
    a13 = np.sum(np.bitwise_xor(ch13, gandu))
    a14 = np.sum(np.bitwise_xor(ch14, gandu))
    a15 = np.sum(np.bitwise_xor(ch15, gandu))
    a16 = np.sum(np.bitwise_xor(ch16, gandu))

    A = min([a1, a2, a3, a4, a5, a6, a7, a8, a9,
             a10, a11, a12, a13, a14, a15, a16])
    if A == a1:
        final_arr.append(0)
        final_arr.append(0)
        final_arr.append(0)
        final_arr.append(0)
    elif A == a2:
        final_arr.append(0)
        final_arr.append(0)
        final_arr.append(0)
        final_arr.append(1)
    elif A == a3:
        final_arr.append(0)
        final_arr.append(0)
        final_arr.append(1)
        final_arr.append(0)
    elif A == a4:
        final_arr.append(0)
        final_arr.append(0)
        final_arr.append(1)
        final_arr.append(1)
    elif A == a5:
        final_arr.append(0)
        final_arr.append(1)
        final_arr.append(0)
        final_arr.append(0)
    elif A == a6:
        final_arr.append(0)
        final_arr.append(1)
        final_arr.append(0)
        final_arr.append(1)
    elif A == a7:
        final_arr.append(0)
        final_arr.append(1)
        final_arr.append(1)
        final_arr.append(0)
    elif A == a8:
        final_arr.append(0)
        final_arr.append(1)
        final_arr.append(1)
        final_arr.append(1)
    elif A == a9:
        final_arr.append(1)
        final_arr.append(0)
        final_arr.append(0)
        final_arr.append(0)
    elif A == a10:
        final_arr.append(1)
        final_arr.append(0)
        final_arr.append(0)
        final_arr.append(1)
    elif A == a11:
        final_arr.append(1)
        final_arr.append(0)
        final_arr.append(1)
        final_arr.append(0)
    elif A == a12:
        final_arr.append(1)
        final_arr.append(0)
        final_arr.append(1)
        final_arr.append(1)
    elif A == a13:
        final_arr.append(1)
        final_arr.append(1)
        final_arr.append(0)
        final_arr.append(0)
    elif A == a14:
        final_arr.append(1)
        final_arr.append(1)
        final_arr.append(0)
        final_arr.append(1)
    elif A == a15:
        final_arr.append(1)
        final_arr.append(1)
        final_arr.append(1)
        final_arr.append(0)
    else:
        final_arr.append(1)
        final_arr.append(1)
        final_arr.append(1)
        final_arr.append(1)

    temp = temp + 12

# print(final_arr)

# print np.bitwise_xor(ch1, x)
final_arr = np.array(final_arr)


d = final_arr.reshape(400, 300)


# final = np.array(ans_arr)

# print(final.size)
# ffff = (final-1)/-2

####################################################################

plt.imshow(d, 'gray')
plt.show()

#######################################################################

monalisaaaa = np.load("mss.npy")
y = d - monalisaaaa
y[y < 0] = 1
print(np.sum(y))  # BER*11000

# print math.erfc((2.00*pow(10.00, x/10.00))/np.sqrt(2.00))/2.00

# print(np.sqrt(sum))
