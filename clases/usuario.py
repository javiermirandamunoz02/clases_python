


class Usuario:
    def __init__(self,username, email , password , activo):
        self.username = username
        self.email = email
        self.password = password
        self.activo = activo

    def leer(self):
        print(f"nombre:{self.username}email: {self.email}activo:{self.activo} ")    


    def login(self, passw):
        if self.password != passw:
            print("passsword incorrecta")
        else:
            print("password correcta")


    def desactivar(self):
        self.activo = False
        
            
 juanito = Usuario("juanito" , "correo@correo.cl" , "1234" ,True)           


juanito.datos