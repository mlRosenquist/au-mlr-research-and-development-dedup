# from hex import float_to_hex, hex_to_float
import struct
import numpy as np

##########
# IEEE 754 Single precision (32 bits)
##########
def float_to_bin(f):
    return '0b' + format(struct.unpack('!I', struct.pack('!f', f))[0], '032b')

##########
# IEEE 754 Single precision (32 bits)
##########
def bin_to_float(b):
    return struct.unpack('!f',struct.pack('!I', int(b, 2)))[0]

def compress_float(f: np.single, deviation_bits=0, output="binary"):
    if (deviation_bits == 0):
        return f
    binary = float_to_bin(f)
    base = binary[:0-deviation_bits] + "0" * deviation_bits
    if (output == "float"):
        return np.single(bin_to_float(base))
    return base

def compress_float21(f: np.single, deviation_bits=0, output="binary"):
    binary = float_to_bin(f)
    base = binary[:-11-deviation_bits] + "0" * (deviation_bits + 11)
    if (output == "float"):
        return np.single(bin_to_float(base))
    return base

def compress_floatxx(f: np.single, float_bits=32, deviation_bits=0, output="binary"):
    binary = float_to_bin(f)
    base = binary[:-(32-float_bits)-deviation_bits] + "0" * (32 - float_bits + deviation_bits)
    if (output == "float"):
        return np.single(bin_to_float(base))
    return base


def compress_int_array(i_array, deviation_bits=0, output="binary"):
    res = []
    for i in i_array:
        i = int(i)
        if (deviation_bits == 0):
            res.append(i)
        base = bin(i)[:0-deviation_bits] + "0" * deviation_bits
        if (output == "integer"):
            res.append(int(base, 2))
    return res


def compress_int(i, deviation_bits=0, output="binary"):
    if (deviation_bits == 0):
        return i
    base = bin(i)[:0-deviation_bits] + "0" * deviation_bits
    if (output == "integer"):
        return int(base, 2)
    return base

def get_compressed_size_float32(num_bases, highest_base_count, deviation_bits, row_count):
    from math import ceil, log
    bases = num_bases * (32 - deviation_bits)
    ids_and_deviations = row_count * (ceil(log(num_bases, 2)) + deviation_bits)
    counts = num_bases * ceil(log(highest_base_count, 2)) 
    return(bases + ids_and_deviations + counts)

def get_compressed_size_float21(num_bases, highest_base_count, deviation_bits, row_count):
    from math import ceil, log
    bases = num_bases * (21 - deviation_bits)
    ids_and_deviations = row_count * (ceil(log(num_bases, 2)) + deviation_bits)
    counts = num_bases * ceil(log(highest_base_count, 2)) 
    return(bases + ids_and_deviations + counts)

def get_compressed_size_floatxx(num_bases, highest_base_count, deviation_bits, row_count, float_bits):
    from math import ceil, log
    bases = num_bases * (float_bits - deviation_bits)
    ids_and_deviations = row_count * (ceil(log(num_bases, 2)) + deviation_bits)
    counts = num_bases * ceil(log(highest_base_count, 2)) 
    return(bases + ids_and_deviations + counts)

def get_compressed_size(num_bases, highest_base_count, deviation_bits, row_count, number_of_bits):
    from math import ceil, log
    return((num_bases * (number_of_bits - deviation_bits)) + (row_count * (ceil(log(num_bases, 2)) + deviation_bits)) + (ceil(log(highest_base_count, 2))))

# value=55
# print(value)
# print(gd_compress_int(value))
