from __future__ import annotations
from typing import TYPE_CHECKING
from ManejadorPacientes import ManejadorPacientes
from Paciente import Paciente
from RepositorioPacientes import RespositorioPacientes
if TYPE_CHECKING:
    from VistaPacientes import VistaPacientes, NuevoPaciente


class ControladorPacientes(object):
    def __init__(self, repo:RespositorioPacientes, vista:VistaPacientes):
        self.repo = repo
        self.vista:VistaPacientes = vista
        self.seleccion = -1
        self.pacientes = list(repo.obtenerListaPacientes())
    
    # comandos que se ejecutan a través de la vista
    def crearPaciente(self):
        from VistaPacientes import NuevoPaciente
        nuevoPaciente = NuevoPaciente(self.vista).show()
        if nuevoPaciente:
            paciente = self.repo.agregarPaciente(nuevoPaciente)
            self.pacientes.append(paciente)
            self.vista.agregarPaciente(paciente)
    
    def mostrarIMC(self):
        from VistaPacientes import VistaIMC
        paciente = self.pacientes[self.seleccion]
        VistaIMC(self.vista, paciente)
    
    def seleccionarPaciente(self, index):
        self.seleccion = index
        paciente = self.pacientes[index]
        self.vista.verPacienteEnForm(paciente)
    
    def modificarPaciente(self):
        if self.seleccion==-1:
            return
        rowid = self.pacientes[self.seleccion].rowid
        detallesPaciente = self.vista.obtenerDetalles()
        detallesPaciente.rowid = rowid
        paciente = self.repo.modificarPaciente(detallesPaciente)
        self.pacientes[self.seleccion] = paciente
        self.vista.modificarPaciente(paciente, self.seleccion)
        self.seleccion=-1
    
    def borrarPaciente(self):
        if self.seleccion==-1:
            return
        paciente = self.pacientes[self.seleccion]
        self.repo.borrarPaciente(paciente)
        self.pacientes.pop(self.seleccion)
        self.vista.borrarPaciente(self.seleccion)
        self.seleccion=-1
    
    def start(self):
        for c in self.pacientes:
            self.vista.agregarPaciente(c)
        self.vista.mainloop()

    def salirGrabarDatos(self):
        self.repo.grabarDatos()