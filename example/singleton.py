import threading
import time


class Singleton(object):
    _lock = threading.Lock()

    # def __new__(cls, *args, **kwargs):
    #     if not hasattr(Singleton, '_instance'):
    #         # cls._instance = super().__new__(cls)
    #         cls._instance = object.__new__(cls)
    #     return cls._instance

    @classmethod
    def instance(cls, *args, **kwargs):
        """
        自定义类方法创建单例
        ps: 这种方法无法支持多线程，需要加锁，以兼容多线程
        """
        if not hasattr(Singleton, '_instance'):     # 加锁创建实例前多做一次判断，避免已经创建实例了，但我们还是加了锁
            with cls._lock:     # 上锁, 当我们实现单例时，为了保证线程安全需要在内部加入锁。未加锁部分并发执行,加锁部分串行执行
                if not hasattr(cls, '_instance'):
                    cls._instance = Singleton()
        return cls._instance

    def __init__(self):
        time.sleep(3)
        super().__init__()


def task(arg):
    # obj = Singleton()
    obj = Singleton.instance()
    print(obj)


if __name__ == '__main__':
    for i in range(20):
        # obj = Singleton()
        # print(obj)
        t = threading.Thread(target=task, args=[i, ])
        t.start()