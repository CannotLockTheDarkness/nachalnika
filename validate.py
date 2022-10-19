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
