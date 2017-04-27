def double(val):
    if isinstance(val, str):
        raise ValueError('bad')
    return val * 2