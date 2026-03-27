





class Persona:
    def __init__(self,nombre,edad,rut):
        self.nombre = nombre
        self.edad = edad
        self.rut = rut

    def cumplir_anios(self):
        self.edad +=1    
                
    def saludar(self):
          print(f"hola mi nombre es : {self.nombre} y tengo {self.edad}")    

    def verificar_rut(self):
        if self.rut == 0:
            print("sin rut")
        else:
            print("rut listo")        

       
    


#instancia
juanito = Persona("juanito",34,111111111)
carlos = Persona("carlos",34,1111111)

print(juanito.saludar())
print(juanito.verificar_rut())
