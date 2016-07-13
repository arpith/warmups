def ee101(values):
    if 'i' in values and 'r' in values:
        i = values['i']
        r = values['r']
        return {'v': i * r}
    elif 'v' in values and 'r' in values:
        v = values['v']
        r = values['r']
        return {'i': v / r}
    elif 'v' in values and 'i' in values:
        v = values['v']
        i = values['i']
        return {'r': v / i}
