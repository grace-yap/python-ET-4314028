# library
# - there's no real formal definition of a library in python; it's more of a general computer science word
# - it just means imported files, code that you're referencing that lives somewhere else
# - when people say python libraries, they could either be talking aobut a module or a package, but usually they're talking about a package

# module
# - literally just a python file

# package
# - simply a collection of modules
# - a collection of related python files all bundled up into a single package
# - the modules in these packages are generally related in functionality, so it can be useful to let them reference each other

# __init__.py (in /11_02_b/numbers folder)
# - completely blank inside
# - required to tell python this is a package, not just a random collection of python files in a folder
# - like the constructor or the initialization function of class has 2 underscores before and after the init
# - so when this __init__.py is in the directory, it allows us to do imports
# - if you delete the __init__.py file, you'll get the error: "ModuleNotFoundError: No module named 'numbers.factors'; 'numbers' is not a package
#       now it's just some random directory, so it's very important to have that __init__.py file there
