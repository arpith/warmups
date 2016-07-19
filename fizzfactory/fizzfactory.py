def fizz(number, factory):
    ret = "" 
    for k, v in factory.iteritems():
        if number % k == 0:
            ret += v
    if ret == "":
        ret = str(number)
    return ret

def fizzfactory(factory):
    ret = []
    numbers_to_100 = list(range(101))[1:]
    ret = [fizz(number, factory) for number in numbers_to_100]
    return ret
