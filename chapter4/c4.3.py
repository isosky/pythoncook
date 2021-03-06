# 用生成器创建新的迭代模式
def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment


for n in frange(0, 4, 0.5):
    print(n)


def countdown(n):
    print('Starting to count from', n)
    while n > 0:
        yield n
        n -= 1
        print('Done!')


c = countdown(3)
print(c)
print(next(c))
print(next(c))
