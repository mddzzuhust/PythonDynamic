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
    if k in total:
        result = total[k]
    else:
        result = fib_test(k-1) + fib_test(k-2)
        total[k] = result
    return result


if __name__ == "__main__":
    #搜索+记忆算法
    from datetime import datetime
    start_time = datetime.now()
    print(fib_test(50))
    print("递归耗时：{}".format((datetime.now()-start_time).total_seconds()))

    # start_time = datetime.now()
    # print(fib_test2(100))
    # print("循环耗时：{}".format((datetime.now() - start_time).total_seconds()))
    # print(total)
