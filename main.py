from RepositorioPacientes import RespositorioPacientes
from VistaPacientes import VistaPacientes
from ControladorPacientes import ControladorPacientes
from ObjectEncoder import ObjectEncoder

def main():
    conn=ObjectEncoder('pacientes.json')
    repo=RespositorioPacientes(conn)
    vista=VistaPacientes()
    ctrl=ControladorPacientes(repo, vista)
    vista.setControlador(ctrl)
    ctrl.start()
    ctrl.salirGrabarDatos()

if __name__ == "__main__":
    main()