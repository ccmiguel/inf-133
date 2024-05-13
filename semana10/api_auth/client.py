from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper (*args,**kwargs):
        print("Antes dellamar a ala funcion")
        result

