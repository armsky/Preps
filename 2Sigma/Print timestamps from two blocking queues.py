"""
给两个independent queue，每个queue都存着timestamp，只能有getNext()来取queue里面的timestamp，
每个timestamp只能被取一次，比较这两个queue里的timestamp，如果差值<1，print这两个timestamp。
例如：
Q1 0.2, 1.4, 3.0
Q2 1.0 1.1, 3.5
output: (0.2, 1.0), (1.4, 1.0), (0.2, 1.1), (1.4, 1.1), (3.0, 3.5)
最后用了两个thread,两个thread-safe queue来实现. 每次call getNext(), 和另一个queue里存的
每个item相比, 相差大于一就删除, 否则输出
"""
We use two threads, to avoid being blocked.

def retrieve_from_queue1(stream):. 涓€浜�-涓夊垎-鍦帮紝鐙鍙戝竷
    ts = stream.getNext() 鏉ユ簮涓€浜�.涓夊垎鍦拌鍧�.
    calculate_pairs(q2, q1, ts)

Same thing for queue2.

Meanwhile, two threads are modifying the same data structure — q1 and q2, so we
need lock.. 
- lock = threading.Lock()
- modify calculate_pair to “with lock:”
- finally start the threads, and run

try:
    thread.start_new_thread(thread1, (s1, ))
    thread.start_new_thread(thread2, (s2, ))
except:
    print "Couldn't start threads."
