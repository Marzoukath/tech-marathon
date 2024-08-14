def start_end_decorator(func):  

    def wrapper ():
        print('Start')
        func()
        print('End')
    return wrapper
@start_end_decorator 
def print_name():
    print('Marzoukath')


print_name()