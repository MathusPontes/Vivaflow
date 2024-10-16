from usuario import Usuario
from medico import Medico
from agendamento import Agendamento

class SistemaHospitalar:
    def __init__(self):
        self.usuarios = []
        self.medicos = []
        self.agendamento = Agendamento()

    def cadastrar_usuario(self, nome, email, telefone, senha):
        usuario = Usuario(nome, email, telefone, senha)
        self.usuarios.append(usuario)
        return usuario
    
    def cadastrar_medico(self, nome, especialidade, crm, email):
        medico = Medico(nome, especialidade, crm, email)  
        print(f"Médico {nome} cadastrado com sucesso.")
        return medico

    def agendar_consulta(self, paciente, medico, data):
        return self.agendamento.agendar_consulta(paciente, medico, data)

    def listar_agendamentos(self):
        return self.agendamento.listar_agendamentos()

    def excluir_consulta(self, consulta):
        return self.agendamento.excluir_consulta(consulta)

    def encontrar_usuario(self, email):
        for usuario in self.usuarios:
            if usuario.email == email:
                return usuario
        return None
