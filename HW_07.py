import random
import time
import ctypes

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
    if len(mtrx1) == 0 or len(mtrx2[0]) == 0:
        return []
    else:
        return f"False,data is incorrect"


# def C_mat_mult(a, b):
#
#     libmatmult = ctypes.CDLL.LoadLibrary("./matmult.so")
#
#     dima = len(a) * len(a)
#     dimb = len(b) * len(b)
#
#     array_a = ctypes.c_float * dima
#     array_b = ctypes.c_float * dimb
#     array_c = ctypes.c_float * dima
#
#     suma = array_a()
#     sumb = array_b()
#     sumc = array_c()


def test_functions():
    assert python_matrix_multi([[-7, 3, 5, -8], [-3, -2, -3, 10], [6, -4, 6, -4]], [[9, 9, 10], [-5, -8, -5], [-6, -10, 9], [2, 9, -5]]) == list([[-7, -7, 2], [2, 2, 11], [4, 4, 13]]), False
    assert python_matrix_multi([[4, 4, 7, 2], [-8, -3, -8, -3], [3, 3, 0, 2]], [[-5, -7, -6], [-6, -2, -7], [-4, -8, 1], [6, -4, 2]]) == list([[8, -4, 7], [-31, -43, -32], [-1, -13, -2]]), False
    assert python_matrix_multi([[7, -1, 5, 0], [9, 8, 4, -1], [-1, 9, -7, -1], [-4, -9, -6, -10]], [[-1, -7, -7, -2], [-5, 5, 5, -9], [3, -3, 8, -10], [3, -3, -6, -9]]) == list([[11, 3, 11, -19], [20, 12, 20, -10], [0, -8, 0, -30], [-29, -37, -29, -59]]), False
    assert python_matrix_multi([[10]], [[2], [-6]]) == list([[12]]), False
    assert python_matrix_multi([[-1]], [[1, 7]]) == "False,data is incorrect", False
    assert python_matrix_multi([], [[3, 6]]) == list([1]), False  # Должно быть неверно
    assert python_matrix_multi([], [[3, 6]]) == list([0]), False  # Должно быть верно


if __name__ == "__main__":
    a = python_generate_random_matrix(0, 0)
    d = python_generate_random_matrix(1, 2)
    start_time = time.time()
    python_matrix_multi(a, d)
    print("--- %s seconds ---" % (time.time() - start_time))
    test_functions()





