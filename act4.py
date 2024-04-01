def func1(a,b):
    return a+b,a,b

def func2(a,b):
    c = func1(a,b)
    return a-b,a,b,c

if __name__ == '__main__':
    print(func2(1,2))