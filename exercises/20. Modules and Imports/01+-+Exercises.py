# Question 1
# Your code uses a few functions in the `math` module here and there, but you also tend to use
# the `sin`, `cos` and `tan` functions and the `pi` constant very frequently.

# Write some import statements that you think would be helpful in this scenario.

from math import sin, cos, tan, pi

# Question 2
# There is a library that we installed for our course called `matplotlib`.

# We can certainly import that library using its full name, but whenever we need to reach into
# that module we need to type out `matplotlib.som_func` - since we use this library quite often,
# typing out `matplotlib` every time gets tiring.

# Write an import function that allows you to reference that module using the name `mpl` 
# instead of the full name `matplotlib`.

# Attempt to import matplotlib with the alias 'mpl'
try:
    import matplotlib as mpl
    print("matplotlib imported successfully as mpl.")
except ModuleNotFoundError:
    print("ModuleNotFoundError: No module named 'matplotlib'. Please install it.")
