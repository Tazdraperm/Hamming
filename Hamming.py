import numpy
import random

encode_map = [x ^ (x << 1) ^ (x << 3) for x in range(16)]
decode_matrix = numpy.mat([[1, 0, 1], [1, 1, 1], [1, 1, 0], [0, 1, 1], [1, 0, 0], [0, 1, 0], [0, 0, 1]])
syndrome = [None, 0, 1, 3, 2, 6, 4, 5]


def encode(x):
    assert x in range(16), "Only 4-bit numbers can be encoded!"
    return encode_map[x]


def decode(y):
    assert y in range(128), "Only 7-bit numbers can be decoded!"
    s = sum([j << (2 - i) for i, j in enumerate(numpy.mod(numpy.mat([(y & (1 << i)) >> i for i in reversed(range(7))]) * decode_matrix, 2).tolist()[0])])
    return encode_map.index((y if syndrome[s] is None else y ^ (1 << syndrome[s])))

print(decode(encode(11) ^ (1 << random.randint(0, 6))))
