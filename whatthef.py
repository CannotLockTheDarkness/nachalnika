class Human:
    'Человек разумный'
    nucleus = 'eukaryotic'
    chromosomes = 46
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Dog():
    def set_parametrs(self, n,w):
        self.n = n
        self.w = w
    def get_parametrs(self):
        return (self.n , self.w)
bobik= Dog()
bobik.set_parametrs('Bobik', 50)
print(bobik.get_parametrs())

class A():
    def __init__(self):
        self.__priv = "I am private"
        self._prot = "I am protected"
        self.pub = "I am public"
    def get_parametrs(self):
        return (self.pub, self._prot, self.__priv)

class User:
    key = '3140i3e32jroho'
    def __init__(self,name,base_password):
        self.name = name
        self.base_password = self.crypt_password(base_password)
    @classmethod
    def crypt_password(cls,input_password):
        crypt_password = ''
        for i in input_password:
            crypt_password += i + cls.key
        return crypt_password
    def get_paramets(self):
        return (self.name, self.base_password)

class Post:
    def __init__(self,date, text):
        self.date = date
        self.text = text

    @staticmethod
    def check_login(login, password, user: User):
        if login == user.name and user.crypt_password(password) == user.base_password:
            return True
        else:
            return False

    @staticmethod
    def validate_user(func):
        def wrapper(self,login,password, user):
            if self.check_login(login,password,user):
                return func(self)
            else:
                return "Please login"
        return wrapper

    @validate_user
    def get_parametrs(self):
        return (self.date, self.text)


Dee = User('Dee', '12345')
message = Post('20.12.2022','Hello World')

print(Dee.get_paramets())
print(message.get_parametrs('Dee', '78', Dee))
