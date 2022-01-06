N = int(input())

arr1 = list(input())
arr2 = list(input())

alpha = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0}

if len(arr1) < len(arr2):
    for i in range(len(arr2)):
        alpha[arr2[i]] =