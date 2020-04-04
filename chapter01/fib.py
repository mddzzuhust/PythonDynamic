# 1. 什么地方递归调用本身
# 2. 什么时候终止递归
# 1 1 2 3 5 8 13

from collections import defaultdict
total = defaultdict(int)
def fib_test(k):
    #求解第k个数的值
    assert k > 0, "k必须大于0"
    if k in [1, 2]:
        return 1
    global total
    total[k] += 1
    return fib_test(k-1) + fib_test(k-2)


def fib_test2(k):
    #求解第k个数的值
    assert k > 0, "k必须大于0"
    if k in [1, 2]:
        return 1

    k_1 = 1
    k_2 = 1
    for i in range(3, k+1):
        tmp = k_1
        k_1 = k_1 + k_2
        k_2 = tmp

    return k_1


if __name__ == "__main__":
    from datetime import datetime
    # start_time = datetime.now()
    # print(fib_test(36))
    # print("递归耗时：{}".format((datetime.now()-start_time).total_seconds()))

    start_time = datetime.now()
    print(fib_test2(100))
    print("循环耗时：{}".format((datetime.now() - start_time).total_seconds()))
    print(total)
