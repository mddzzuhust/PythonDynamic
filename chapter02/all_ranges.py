#所有
#1. 老大 选择一个 ，剩余的交给老二
#2. 选择一个， 剩余的交给老三

data_list = [1, 2, 3, 4, 5]
arranges = []
total = 0
def search(depth, datas):
    if depth == len(data_list)+1:
        print(arranges)
        global total
        total += 1
    else:
        for data in datas:
            #1. 设置现场
            arranges.append(data)
            #2. 递归
            next_datas = datas[:]
            next_datas.remove(data)
            search(depth+1, next_datas)
            #3. 恢复现场
            arranges.pop()
            
if __name__ == "__main__":
    search(1, data_list)
    print("有{}种排列方式".format(total))
