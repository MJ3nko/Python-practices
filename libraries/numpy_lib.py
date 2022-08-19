import numpy


def reverse_array(array: list):
    array.reverse()
    array = numpy.array(array, float)
    return array


array = input().strip().split(' ')
array = reverse_array(array)
print(array)
