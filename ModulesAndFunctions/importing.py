"""Module for investigating importing and namespace
"""

import better_code
from better_code import area_of_square

# area = better_code.area_of_square(40)
area = area_of_square(40)
print(area)

namespace = globals().copy()
for key, value in namespace.items():
    print(f"{key}: {value}")
