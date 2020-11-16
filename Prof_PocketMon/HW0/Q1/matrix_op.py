import numpy as np

fileA = open('./matrixA.txt', 'r')
fileB = open('./matrixB.txt', 'r')

strA = fileA.read()
list_strA = strA.split(',')
list_intA = list(map(int, list_strA))
matrixA = np.mat(list_intA)

strB = fileB.read()
list_strB = strB.split()
list_intB = [list(map(int, i.split(','))) for i in list_strB]
matrixB = np.mat(list_intB)

mul = np.matmul(matrixA, matrixB).tolist()
result = []
for i in mul:
    for j in i:
        result.append(j)
result = sorted(result, reverse=True)
np.savetxt('answer1.txt',result, fmt='%d')

