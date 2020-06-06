import numpy as np
import math


def decode_binary_string(s):
    return ''.join(chr(int(s[i*8:i*8+8], 2)) for i in range(len(s)//8))


def encode_string(s):
    return ''.join('{0:08b}'.format(ord(x), 'b') for x in s)


def z1(n):  # 4-QAM constellations
    return (np.cos(2*np.pi*fc*n*Ts) + np.sin(2*np.pi*fc*n*Ts))


def z2(n):
    return (-np.cos(2*np.pi*fc*n*Ts) + np.sin(2*np.pi*fc*n*Ts))


def z3(n):
    return (-np.cos(2*np.pi*fc*n*Ts) - np.sin(2*np.pi*fc*n*Ts))


def z4(n):
    return (np.cos(2*np.pi*fc*n*Ts) - np.sin(2*np.pi*fc*n*Ts))


Str = str(input())
bin_str = encode_string(Str)
bin_arr = np.array(list(bin_str), dtype=int)
bin_arr = -2*bin_arr+1

fc = 2000000.00  # carrier frequency 2Mhz
Fs = 50000000.00  # samplig frequency = 50Mhz
Ts = 1/50000000.00  # sampling time
St = []  # modulated signal
n = 0

for i in range(int(len(bin_str)/2)):  # defining S(t)
    for j in range(50):
        St.append(bin_arr[2*i]*np.cos(2*np.pi*fc*n*Ts) +
                  bin_arr[2*i+1]*np.sin(2*np.pi*fc*n*Ts))
        n = n+1

St_arr = np.array(St)

T = 0.000001
Eb = T/2.00  # energy per bit
x = 5.00  # Eb/No in decibels
std = np.sqrt(Eb*1/Ts*0.5*pow(10.00, -x/10.00))  # standard deviation
samples = np.random.normal(0, std, len(bin_str)*25)  # white gaussian noise

rt = St_arr + samples  # recived signal

##################################################################################################
n = 0
new_arr = []
for j in range(int(len(bin_str)/2)):
    a1 = 0
    a2 = 0
    a3 = 0
    a4 = 0
    for i in range(50):
        a1 = a1 + (rt[n]-z1(n))**2
        a2 = a2 + (rt[n]-z2(n))**2
        a3 = a3 + (rt[n]-z3(n))**2
        a4 = a4 + (rt[n]-z4(n))**2
        n = n+1

    min_dist = min([a1, a2, a3, a4])  # minimum distance calculation

    if min_dist == a1:
        new_arr.append(1)
        new_arr.append(1)
    elif min_dist == a2:
        new_arr.append(-1)
        new_arr.append(1)
    elif min_dist == a3:
        new_arr.append(-1)
        new_arr.append(-1)
    else:
        new_arr.append(1)
        new_arr.append(-1)

bin_recv = np.array(new_arr)
bin_recv = ((bin_recv-1)/-2)
bin_recv = bin_recv.astype(int)
text = ""
for x in bin_recv:
    text = text + str(bin_recv[x])

out_str = decode_binary_string(text)

print(out_str)
