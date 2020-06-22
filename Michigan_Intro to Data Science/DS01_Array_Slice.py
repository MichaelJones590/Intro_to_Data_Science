# This is a place to try out some slicing concepts
import numpy as np
#
r = np.arange(36)
r.resize((6,6))
print(r)
print()
print(r.reshape(36)[::7])
