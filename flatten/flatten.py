def flatten(li):
    res = []
    for l in li:
        if isinstance(l, list):
            res += flatten(l)
        else:
            res.append(l)
    return res
