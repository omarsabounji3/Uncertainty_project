def geo_mean(x):
    from numpy import log, mean, exp
    
    geometric_mean = exp(mean(log(x)))
    
    return geometric_mean