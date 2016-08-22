def mods(l, n):
    ret = [[x for x in l if x % n == i] for i in xrange(n)]
    return ret
