import numpy as np
#add

__all__ = ['rand_array']


def rand_array(shape):
    return np.random.rand(*shape)
