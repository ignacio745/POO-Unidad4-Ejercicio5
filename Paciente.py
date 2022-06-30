import re

class Paciente:
    telefonoRegex = re.compile(r"\([0-9]{3}\)[0-9]{7}")
    __apellido = None
    __nombre = None
    __telefono = None
    __altura = None
    __peso = None
    def __init__(self, apellido:str, nombre:str, telefono:str, altura:int, peso:int) -> None:
        self.__apellido = self.requerido(apellido, "Apellido es un valor requerido")
        self.__nombre = self.requerido(nombre, "Nombre es un valor requerido")
        self.__telefono = self.formatoValido(telefono, Paciente.telefonoRegex, "Teléfono no tiene un formato correcto")
        self.__altura = self.validarEntero(altura, "La altura debe ser un entero")
        self.__peso = self.validarEntero(peso, "El peso debe ser un entero")
    
    def getApellido(self):
        return self.__apellido
    
    def getNombre(self):
        return self.__nombre
    
    def getTelefono(self):
        return self.__telefono
    
    def getAltura(self):
        return self.__altura
    
    def getPeso(self):
        return self.__peso
    
    def getIMC(self) -> float:
        return self.__peso / (self.__altura/100)**2
    

    def getComposicionCorporal(self) -> str:
        imc = self.getIMC()
        if imc < 18.5:
            cadena = "Peso inferior al normal"
        elif 18.5<= imc < 25:
            cadena = "Peso normal"
        elif 25 <= imc < 29.9:
            cadena = "Peso superior al normal"
        else:
            cadena = "Obesidad"
        return cadena
    

    def requerido(self, valor, mensaje):
        if not valor:
            raise ValueError(mensaje)
        return valor
    
    def formatoValido(self, valor, regex:re.Pattern, mensaje):
        if not valor or not regex.match(valor):
            raise ValueError(mensaje)
        return valor
    
    def validarEntero(self, valor, mensaje):
        if not isinstance(valor, int):
            raise ValueError(mensaje)
        return valor
    
    
    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__= dict(
                apellido=self.__apellido,
                nombre=self.__nombre,
                telefono=self.__telefono,
                altura=self.__altura,
                peso=self.__peso
            )
        )
        return d