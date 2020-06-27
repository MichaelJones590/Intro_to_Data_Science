# This tests assigning a function to a variable
#
def add_numbers(x,y):
    return x+y

a = add_numbers
a(1,2)

# my guess is this doesn't work because it needs the context of the other Jupyter Notebook cells that preceded it