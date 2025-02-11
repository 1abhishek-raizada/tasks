##
#EXCEPTION HANDLING 
##
def multiple_exceptions():
    a=int(input('enter the first number: '))
    b=int(input('enter the second number: '))

    try:    
        print(a/b)
        c=int(input('enter the first number: '))
        d=int(input('enter the second number: '))
        print('resources opened....')
   
    except Exception as e:
        print("you cant do this... ",f"\nname of the exception is: {e}")
    finally:
        print('resources closed....')   
# here above we are handling multiple exceptions


##
#raising an error 
##
def raising_error():
    def set(age):
        if age<=0:
            raise ValueError('Age cannot be zero')
        print(f'Age is set to {age}')

    try:
        set(0)
    except ValueError as e:
        print(e)


##
#user defined exceptions 
##
class InvalidAgeError(Exception):
    def __init__(self,age,msg='age is not in range'):
        self.age=age
        self.msg=msg
        #super().__init__(self.msg)
    def __str__(self):
        return f'{self.age} -> {self.msg}'
        
def set_age(age):
    if age<=0:
        raise InvalidAgeError(age)
    print(f'age is set to: {age}')
try:
    set_age(0)
except InvalidAgeError as e:
    print(e)        

##
#trying runtime error 
##
class NetworkError(RuntimeError):
    def __init__(self, args):
        self.args=args
try:
    raise NetworkError('error')
except NetworkError as e:
        print(e.args)        