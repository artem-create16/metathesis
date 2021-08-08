def decorator(s):
    def wrap(function):
        def called():
             return function(s)
        return called
    return wrap


@decorator('example')
def f(num):
    print(num, 'ex here')


f()
