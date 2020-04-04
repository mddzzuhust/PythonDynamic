#使用动态规划求解0-1背包问题
#老三
info = [
    [3, 8],
    [2, 5],
    [5, 12]
]
total = 5
#老三初始化
pre_max = [0]
for i in range(1, info[-1][0]):
    pre_max.append(0)
for i in range(info[-1][0], total+1):
    pre_max.append(info[-1][1])


for k in range(len(info)-1, -1, -1):
    new_pre_max = [0]
    start = 1
    # if k == 0:
    #     start = total
    for i in range(start, total + 1):
        value_list = []
        if i >= info[k-1][0]:
            value_list.append(info[k-1][1] + pre_max[i-info[k-1][0]])
        value_list.append(pre_max[i])
        new_pre_max.append(max(value_list))
    pre_max = new_pre_max

# #老二
# new_pre_max = [0]
# for i in range(1, total+1):
#     value_list = []
#     for j in range(0, i + 1):
#         #j代表留给自己
#         if j >= info[1][0]:
#             value_list.append(info[1][1]+pre_max[i-j])
#         else:
#             value_list.append(pre_max[i-j])
#     new_pre_max.append(max(value_list))
#
# #老大
# new_pre_max2 = [0]
# for i in range(total, total+1):
#     value_list = []
#     for j in range(0, total+1):
#         #j代表留给自己
#         if j >= info[0][0]:
#             value_list.append(info[0][1]+new_pre_max[i-j])
#         else:
#             value_list.append(new_pre_max[i-j])
#     new_pre_max2.append(max(value_list))

print(pre_max)

