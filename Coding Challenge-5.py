# DAILY CODING CHALLENGE 5
# Question asked by:JANE STREET
# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For
# example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.Implement car and cdr.


# Step 1: Defining the already implemented cons function to get the pair as result
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


# Step 2: Implementing the "car" and "cdr" function
def car(pair):
    return pair(lambda a, b: a)


def cdr(pair):
    return pair(lambda a, b: b)


# Step 3: Calling the main function which calls these above functions and displays the result
result = cons(3,4)
car_result = car(result)
cdr_result = cdr(result)
print(car_result)
print(cdr_result)
