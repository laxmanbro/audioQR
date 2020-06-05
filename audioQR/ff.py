import numpy as np
import math

def decode_binary_string(s):
    return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))

def encode_string(s):
    return ''.join('{0:08b}'.format(ord(x), 'b') for x in s)

Str = str(input())
bin_str = encode_string(Str)
bin_arr = np.array(list(bin_str), dtype=int)
bin_arr = -2*bin_arr+1

fc = 2000000.00  # carrier frequency
Ts = 1/50000000.00  # sampling time
St = []
print(bin_arr)
