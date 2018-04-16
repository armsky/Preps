"""多线程问题，给一个冰箱，里面可以放milk，butter，和一个奇怪但是没有人要的东西，有五个人，
三个人只负责吃，两个人只负责放。由于吃的人time interval是350L，放的人time interval是200L，
全部并行处理，这个时候就出现多线程冲突的问题了，一开始我直接给function加sync发现不管用，
我在就给每个冰箱的item加了一个violiate，设置是否被occupy了，不过这个方法还是有小问题，
因为有一堆人是要sleep 一会之后再操作，那么这个item就被他占了，其他人无法操作。所以最好的
解决方案应该是用AtomicInteger来判断有多少个人在同时操作，并且给操作的那个变量sync即可解决
多线程问题，但是我没想到这点，这个是面试官提示的。所以我这轮也有可能挂了。"""

"""第二问是冰箱问题，五个人共用冰箱，三个人不断从冰箱里取，两个人不断往冰箱里加。冰箱里有几个不同的
non-blocing queue会放不同的东西，比如苹果，梨，香蕉，每个queue有上限最多放几个。取得人会有自己
的preference，总是先取preference，如果没有再取别的，如果什么都没有就直接返回。放的人会查看是
不是每一种都放满了，没有的话就去买回来放进去。这题让你看代码找bug，然后问你怎么加synchronization。
因为是non-blocking所以不需要唤醒机制，直接说一下怎么加mutex就行，不用具体跑程序。
"""
"""
_Mutexes_ are typically used to serialise access to a section of re-entrant code
that cannot be executed concurrently by more than one thread. A mutex object only
allows one thread into a controlled section, forcing other threads which attempt
to gain access to that section to wait until the first thread has exited from
that section.(A mutex is really a semaphore with value 1.)

_Semaphore_ restricts the number of simultaneous users of a shared resource up
to a maximum number.
"""
mutex = threading.Lock()
mutex.acquire()
mutex.release()

class AtomicInteger():
    def __init__(self, value=0):
        self._value = value
        self._lock = threading.Lock()

    def inc(self):
        with self._lock:
            self._value += 1
            return self._value

    def dec(self):
        with self._lock:
            self._value -= 1
            return self._value


    @property
    def value(self):
        with self._lock:
            return self._value

    @value.setter
    def value(self, v):
        with self._lock:
            self._value = v
            return self._value
