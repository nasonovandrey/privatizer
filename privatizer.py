from inspect import currentframe


def privatizer(function):
    def wrapper(*args, **kwargs):
        prev_locals = currentframe().f_back.f_locals
        if not 'self' in prev_locals or args[0] != prev_locals['self']:
            raise Exception('Private function is called outside of the class where it was defined')
        function(*args, **kwargs)
    return wrapper

