# Проверка Аргументов


from functools import wraps

def stop_kwargs(func):
    wraps(func)
    def wrapper(*args, **kwargs):
        if kwargs:
            raise ValueError("Key Word Arguments are on stop")
        return func(*args, **kwargs)
    return wrapper

@stop_kwargs
def print_Hello(name):
    print(f"Hello {name}!")
print_Hello("Jack")





















