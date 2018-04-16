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
