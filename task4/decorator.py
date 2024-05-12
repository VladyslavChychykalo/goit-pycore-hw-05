def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return "Enter the argument for the command."
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "No such contact found."
       

    return inner