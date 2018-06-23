

def get_var_dict(upper, lower, genes, keys):
    var = {}
    length = len(keys)
    for i in xrange(length):
        var[keys[i]] = genes[i] * (upper[i] - lower[i]) + lower[i]
    return var
    
