import re

n = int(input())
matrix = [str(input()) for i in range(n)]
matrix2 = []


def check_string(pattern, input_string):

    match = re.match(pattern, input_string)

    if match:
        return True
    else:
        return False

def rotate_matrix_clockwise(matrix):
    return [list(reversed(col)) for col in zip(*matrix)]



def clean(matrix):
    continuecharacter = []
    n = len(matrix)
    m = len(matrix[0])
    matrix3 = []
    for i in range(n):
        if ("#" in matrix[i]):
            matrix3.append(matrix[i])
    if matrix3 == []:
        return "X"
    for i in range(n):
        if ("#" in matrix[i]):
            continuecharacter.append(i)
    matrix2 = []
    for i in range(n):
        if ("#" in matrix[i]):
            if (i+1 <= n -1) and (m*"." in matrix[i+1]) and (i+1 < max(continuecharacter)) :
                return "X"
            else:
                matrix2.append(matrix[i])
    return matrix2

def checkI(matrix):
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        if matrix[i] != m*"#":
            return False
    return True

def checkC(matrix):
    n = len(matrix)
    m = len(matrix[0])

    control_string = ""
    if (matrix[0] == m * "#" and matrix[-1] == m * "#") == False:
        return False
    for i in range(n):
        if check_string(r'^\#+\.+$', matrix[i]):
            control_string = matrix[i]
            break
    num1 = 0
    count1 = 0
    while (matrix[num1] == m * "#"):
        count1 += 1
        num1 += 1

    num2 = num1
    count2 = 0
    while (matrix[num2] == control_string and control_string != ""):
        count2 += 1
        num2 += 1

    num3 = num2
    count3 = 0
    while (num3 <= n-1 and matrix[num3] == m * "#"):
        count3 += 1
        num3 += 1
    if count1 + count2 + count3 == n:
        return True
    else:
        return False

def checkO(matrix):
    n = len(matrix)
    m = len(matrix[0])

    control_string = ''
    if (matrix[0] == m*"#" and matrix[-1] == m*"#") == False:
        return False
    for i in range(n):
        if check_string(r'^\#+\.+\#+$',matrix[i]):
            control_string = matrix[i]
            break
    num1 = 0
    count1 = 0
    while (matrix[num1] == m * "#"):
        count1 += 1
        num1 += 1

    num2 = num1
    count2 = 0
    while (matrix[num2] == control_string and control_string != ""):
        count2 += 1
        num2 += 1

    num3 = num2
    count3 = 0
    while ( num3 <= n-1 and matrix[num3] == m * "#"):
        count3 += 1
        num3 += 1
    if count1 + count2 + count3 == n:
        return True
    else:
        return False

def checkH(matrix):
    n = len(matrix)
    m = len(matrix[0])

    control_string = ''
    for i in range(n):
        if check_string(r'^\#+\.+\#+$', matrix[i]):
            control_string = matrix[i]
            break
    if (matrix[0] == control_string and matrix[-1] == control_string and control_string != "") == False:
        return False
    num1 = 0
    count1 = 0
    while (matrix[num1] == control_string and control_string != ""):
        count1 += 1
        num1 += 1

    num2 = num1
    count2 = 0
    while (num2 <= n - 1 and matrix[num2] == m * "#" ):
        count2 += 1
        num2 += 1

    num3 = num2
    count3 = 0
    while (num3 <= n - 1 and matrix[num3] == control_string and control_string != ""):
        count3 += 1
        num3 += 1
    if count1 + count2 + count3 == n:
        return True
    else:
        return False
def checkL(matrix):
    n = len(matrix)
    m = len(matrix[0])

    control_string = ''
    for i in range(n):
        if check_string(r'^\#+\.+$', matrix[i]):
            control_string = matrix[i]
            break
    num1 = 0
    count1 = 0
    while (matrix[num1] == control_string and control_string != ""):
        count1 += 1
        num1 += 1

    num2 = num1
    count2 = 0
    while (num2 <= n - 1 and matrix[num2] == m * "#"):
        count2 += 1
        num2 += 1


    if count1 + count2  == n:
        return True
    else:
        return False
def checkP(matrix):
    n = len(matrix)
    m = len(matrix[0])

    control_string1 = ''
    control_string2 = ''
    for i in range(n):
        if check_string(r'^\#+\.+\#+$', matrix[i]):
            control_string1 = matrix[i]
            break
    for i in range(n):
        if check_string(r'^\#+\.+$', matrix[i]):
            control_string2 = matrix[i]
            break
    if (matrix[0] == m*"#" and matrix[-1] == control_string2 and control_string2 != "") == False:
        return False
    if (control_string2.rfind("#") + 1)* "#" not in control_string1:
        return False

    num1 = 0
    count1 = 0
    while (num1 <= n - 1 and matrix[num1] == m * "#"):
        count1 += 1
        num1 += 1

    num2 = num1
    count2 = 0
    while (num2 <= n - 1 and matrix[num2] == control_string1 and control_string1 != ""):
        count2 += 1
        num2 += 1

    num3 = num2
    count3 = 0
    while (num3 <= n - 1 and matrix[num3] == m * "#"):
        count3 += 1
        num3 += 1

    num4 = num3
    count4 = 0
    while (num4 <= n - 1 and matrix[num4] == control_string2 and control_string2 != ""):
        count4 += 1
        num4 += 1
    if count1 + count2 + count3 + count4 == n:
        return True
    else:
        return False


matrix2 = clean(matrix)
if matrix2 != "X":
    rotated_matrix = rotate_matrix_clockwise(matrix2)
    rotated_matrix2 = ["".join(rotated_matrix[i]) for i in range(len(rotated_matrix))]
    matrix3pochti = clean(rotated_matrix2)
    if matrix3pochti != "X":
        matrix3 = rotate_matrix_clockwise(rotate_matrix_clockwise(rotate_matrix_clockwise(matrix3pochti)))
        matrix4 = ["".join(matrix3[i]) for i in range(len(matrix3))]
        if checkI(matrix4):
            print("I")
        elif checkO(matrix4):
            print("O")
        elif checkC(matrix4):
            print("C")
        elif checkH(matrix4):
            print("H")
        elif checkL(matrix4):
            print("L")
        elif checkP(matrix4):
            print("P")
        else:
            print("X")
    else:
        print("X")
else:
    print("X")






