from typing import List

from numpy import indices
from Paciente import Paciente

class ManejadorPacientes:
    __indice = 0
    __pacientes = None
    
    def __init__(self) -> None:
        self.__pacientes:List[Paciente] = []
        self.__indice = 0
    
    def agregarPaciente(self, unPaciente:Paciente):
        unPaciente.rowid = self.__indice
        self.__indice += 1
        self.__pacientes.append(unPaciente)
    
    def getListaPacientes(self):
        return self.__pacientes
    
    def deletePaciente(self, paciente):
        indice = self.obtenerIndicePaciente(paciente)
        self.__pacientes.pop(indice)
    

    def updatePaciente(self, paciente):
        indice = self.obtenerIndicePaciente(paciente)
        self.__pacientes[indice] = paciente

    
    def obtenerIndicePaciente(self, paciente):
        bandera = False
        i = 0
        while not bandera and i<len(self.__pacientes):
            if self.__pacientes[i].rowid == paciente.rowid:
                bandera = True
            else:
                i += 1
        return i
    

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            pacientes=[unPaciente.toJSON() for unPaciente in self.__pacientes]
        )
        return d