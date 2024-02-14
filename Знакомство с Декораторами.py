# Знакомство с Декораторами

# def simple_function():
#     #print("Some Code Before")
#     print("Simple Function Code")
#     #print("Some Code After")
#
# simple_function()

def decorator_function(original_function):
    def wrap_function():
        print("Some Code Before")
        original_function()
        print("Some Code After")
    return wrap_function


# decorated_function = decorator_function(simple_function)

# decorated_function()

@decorator_function
def simple_function():
    print("Simple function Code")

simple_function()


def make_compliment(func):
    def wrapper(*args, **kwargs):
        print("Nice to meet you")
        func(*args, **kwargs)
        print("You look great")
    return wrapper


#@make_compliment
def ask_name():
    print("What your name?")
ask_name()

@make_compliment
def say_name(name):
    print("Me name is " + name)

say_name("Jack")

@make_compliment
def order(food, drink):
    print(f"Give me {food} and {drink}")
order("chips", "kola")

