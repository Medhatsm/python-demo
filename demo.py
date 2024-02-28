def method1():
    method2()

def method2():
    print("hello world")
    from demo2 import method1
    method1()


if __name__ == '__main__':
    method1()