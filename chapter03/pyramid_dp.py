pyramid = [
    [13],
    [11, 8],
    [12, 7, 26],
    [6, 14, 15, 8],
    [12, 17, 13, 24, 11]
]

for j in range(4, 0, -1):
    for i in range(j):
        pyramid[j-1][i] += max(pyramid[j][i], pyramid[j][i + 1])

print(pyramid[0][0])
#第四层
# for i in range(4):
#     pyramid[3][i] += max(pyramid[4][i], pyramid[4][i+1])
# print(pyramid[3])
#
# #第三层
# for i in range(3):
#     pyramid[2][i] += max(pyramid[3][i], pyramid[3][i+1])
# print(pyramid[2])
#
# #第二层
# for i in range(2):
#     pyramid[1][i] += max(pyramid[2][i], pyramid[2][i+1])
# print(pyramid[1])
#
# print(pyramid[0][0]+max(pyramid[1][0], pyramid[1][1]))