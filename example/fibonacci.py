def fibonacci_recursion(n):
    """
    斐波拉契数列 递归生成
    """
    assert n > 0, "n > 0"
    if n <= 2:
        return 1
    else:
        return fibonacci_recursion(n - 2) + fibonacci_recursion(n - 1)


def fib_loop_while(n):
    """
    斐波拉契数列 递推法生成
    """
    assert n >= 1, "n > 0"
    a, b = 1, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a


def fib_generator(n):
    """
    斐波拉契数列 生成器生成
    """
    assert n >= 1, "n > 0"
    a, b = 1, 1
    for _ in range(n - 1):
        a, b = b, a + b
    yield a


class Fibonacci(object):
    """
    斐波拉契数列 利用魔法函数 迭代器生成
    ps: 自定义迭代器对象: 在类里面定义__iter__和__next__方法创建的对象就是迭代器对象
    """
    def __init__(self, n):
        self.n = n
        self.current = 0
        self.a = 0
        self.b = 1

    def __next__(self):
        """
        __iter__方法，被next()函数调用
        """
        if self.current < self.n:
            self.a, self.b = self.b, self.a + self.b
            self.current += 1
            return self.a
        else:
            raise StopIteration

    def __iter__(self):
        """
        __iter__方法要返回一个迭代器，自身即是一个迭代器，固返回自身
        可迭代对象身上的__iter__方法, 被iter()函数调用。
        """
        return self


# for循环的本质
# 首先获取可迭代对象
iterator = iter([1, 2, 3, 4, 5])
while True:
    try:
        next(iterator)
    except StopIteration:
        # 遇到StopIteration就跳出循环, 且自动频闭StopIteration异常
        break


import numpy as np


def fib_matrix(n):
    """
    斐波拉契数列 矩阵
    """
    for i in range(n):
        res = pow((np.matrix([[1, 1], [1, 0]], dtype='int64')), i) * np.matrix([[1], [0]])
        print(int(res[0][0]))


if __name__ == '__main__':
    # print(fibonacci_recursion(100))
    print(fib_loop_while(10))
    # print(fib_generator(100))
    # fib = Fibonacci(10)
    # for num in fib:
    #     print(num)
