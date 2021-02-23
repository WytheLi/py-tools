import time


class TimeTrace(object):
    """
    上下文管理器实现计时器
    1、追踪一个函数执行耗时
    2、python中实现了__enter__和__exit__方法，即支持上下文管理器协议
        __enter__(self): 当with开始运行的时候触发此方法的运行
        __exit__(self, exc_type, exc_val, exc_tb): 当with运行结束之后触发此方法的运行
        exc_type如果抛出异常,这里获取异常的类型
        exc_val如果抛出异常,这里显示异常内容
        exc_tb如果抛出异常,这里显示所在位置
    """
    def __init__(self, func):
        self.func = func

    def _now(self):
        return time.time()

    def __enter__(self):
        self.start = self._now()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = self._now()
        print("cost {}".format(self.end - self.start))

    def __call__(self, n):
        """
        使得类实例对象可以像调用普通函数那样，以“对象名()”的形式使用
        """
        start = self._now()
        value = self.func(n)
        end = self._now()
        print("{}, {}, {}, cost: {} seconds.".format(self.func.__name__, n, value, (end - start)))
        return value


def fib_recursion(n):
    assert n >= 1, "n > 0"
    if n <= 2:
        return 1
    else:
        return fib_recursion(n-2) + fib_recursion(n-1)


if __name__ == '__main__':
    with TimeTrace(fib_recursion) as fib:
        print(fib(40))
