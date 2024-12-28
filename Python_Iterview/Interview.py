import copy
original = [[1, 2], [3, 4]]
shallow_copy = copy.copy(original)
shallow_copy[0][0] = 9  # Changes the original list as well
print(shallow_copy)
print(original)

import copy	
original = [[1, 2], [3, 4]]
print(original)
deep_copy = copy.deepcopy(original)
deep_copy[0][0] = 9  # Does not change the original list
print(deep_copy)
print(original)