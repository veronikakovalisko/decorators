'''Task 1
Write a decorator that prints a function with arguments passed to it.
NOTE! It should print the function, not the result of its execution!
For example:
 "add called with 4, 5"

def logger(func):
    pass
@logger
def add(x, y):
    return x + y
@logger
def square_all(*args):
    return [arg ** 2 for arg in args]
'''


def logger(func):
    def gcd(*args):
        print(f'{func.__name__} викликана з {args}')
        result = func(args)
        print(f"результат: {result}")

    return gcd


@logger
def add(*args):
    return [i * 2 for i in args]


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


add(5, 7)

'''Task 2

Write a decorator that takes a list of stop words and replaces them with * inside the decorated function

def stop_words(words: list):

    pass

@stop_words(['pepsi', 'BMW'])

def create_slogan(name: str) -> str:

    return f"{name} drinks pepsi in his brand new BMW!"
    
assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
'''
from functools import wraps


def stop_words(words: list):
    def stop_words2(func):
        @wraps(func)
        def check(*args):
            rez: str = func(args)
            r = []
            for word in rez.rsplit():
                clear_word = word.strip('?/!,.')
                if clear_word in words:
                    r.append(word.replace(clear_word, '*'))
                else:
                    r.append(word)
            return ' '.join(r)

        return check

    return stop_words2


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{str(name).strip('()'',')} drinks pepsi in his brand new BMW!"


print(create_slogan('adam'))

'''Task 3

Write a decorator `arg_rules` that validates arguments passed to the function.

A decorator should take 3 arguments:

max_length: 15

type_: str

contains: [] - list of symbols that an argument should contain

If some of the rules' checks returns False, the function should return False and print the reason it failed; otherwise, return the result.

def arg_rules(type_: type, max_length: int, contains: list):
    pass

@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"
assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
'''


def arg_rules(type_=str, max_length=10, contains=[]):
    def rules(func):
        @wraps(func)
        def check(word):
            if isinstance(word, type_) == False:
                return False
            if len(word) >= max_length:
                return False
            for i in contains:
                if word.find(i) == -1:
                    return False
            return func(word)
        return check
    return rules




@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

# print(create_slogan('johndoe05@gmail.com'))
assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
