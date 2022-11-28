import random
import time
import ctypes
import NumPy as np


random.seed()


def python_generate_random_matrix(m, n):
    result = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(random.randint(-10, 10))
        result.append(row)

    return result


def print_beautifully_python(arr):
    print("--------------------------------")
    for row in arr:
        for elem in row:
            print(str(elem).rjust(4, " "), "|", end="")
        print()
    print("--------------------------------")


def python_matrix_multi(mtrx1, mtrx2):
    if len(mtrx1) == len(mtrx2[0]) and len(mtrx1) <= len(mtrx2):
        multi_result = []
        for i in range(len(mtrx1)):
            row = []
            for j in range(len(mtrx2[0])):
                sum = 0
                for n in range(len(mtrx1[i])):
                    sum += mtrx1[i][n] + mtrx2[n][j]
                row.append(sum)
            multi_result.append(row)
        return multi_result
    else:
        return f"False,data is incorrect"


def C_mat_mult(a, b):

    libmatmult = ctypes.CDLL.LoadLibrary("./matmult.so")

    dima = len(a) * len(a)
    dimb = len(b) * len(b)

    array_a = ctypes.c_float * dima
    array_b = ctypes.c_float * dimb
    array_c = ctypes.c_float * dima

    suma = array_a()
    sumb = array_b()
    sumc = array_c()

    inda = 0
    for i in range(0, len(a)):
        for j in range(0, len(a[i])):
            suma[inda] = a[i][j]
            inda = inda + 1
    for i in range(0, len(b)):
        indb = 0
        for j in range(0, len(b[i])):
            sumb[indb] = b[i][j]
            indb = indb + 1

    libmatmult.matmult(ctypes.byref(suma), ctypes.byref(sumb), ctypes.byref(sumc), 2);

    res = numpy.zeros([len(a), len(a)])
    indc = 0
    for i in range(0, len(sumc)):
        res[indc][i % len(a)] = sumc[i]
        if i % len(a) == len(a) - 1:
            indc = indc + 1

    return res

if __name__ == "__main__":
    a = python_generate_random_matrix(3, 4)
    d = python_generate_random_matrix(4, 3)
    start_time = time.time()
    python_matrix_multi(a, d)
    print("--- %s seconds ---" % (time.time() - start_time))



