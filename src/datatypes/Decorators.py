def check_type_match(func):
    '''
    Checks to see if the arguments for a function of two
    arguments have the same type
    '''
    def wrapper(self, other):
        # check to see if the arguments match
        if type(self) != type(other):
            raise Exception
        else:
            return func(self, other)
    return wrapper
