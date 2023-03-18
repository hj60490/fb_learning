def rotate(matrix):
    n = len(matrix[0])
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
            matrix[j][n - 1 - i] = temp


n = int(input())
matrix = []
for i in range(n):
    row_list = []
    row = input().split()
    for j in row:
        row_list.append(int(j))
    matrix.append(row_list)

temp = matrix
temp2 = matrix
rotate1 = 0
ok = True
# count =0
sum_a = 0
while ok:
    x = input()
    if x == "-1":
        # print("count"+str(count))
        ok = False
        break
    # count+=1
    s = x.split()
    if s[0] == "R":
        times = int(s[1]) / 90
        sum_a += int(s[1])
        while times:
            rotate(matrix)
            times -= 1
            rotate1 += 1

    elif s[0] == 'Q':
        # print(matrix)
        print(matrix[int(s[1])][int(s[2])])
    else:
        hogya = False
        x = temp[int(s[1])][int(s[2])]
        for i in range(len(matrix[0])):
            for j in range(len(matrix[0])):
                if matrix[i][j] == x:
                    matrix[i][j] = int(s[3])
                    hogya = True
                    break
            if hogya:
                break
        rotate_by = sum_a
        ro = rotate_by / 90
        while ro:
            rotate(matrix)
            # sum_a += 90
            ro -= 1




