variables1 = {'scalar': 'Scalar variable',
              'LIST__list': ['List','variable']}
variables2 = {'scalar' : 'Some other value',
              'LIST__list': ['Some','other','value'],
              'extra': 'variables1 does not have this at all'}

def get_variables(arg='one'):
    if arg == 'one':
        return variables1
    else:
        return variables2