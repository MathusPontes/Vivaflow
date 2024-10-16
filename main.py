from sistemahospitalar import SistemaHospitalar
from interface import InterfaceSistemaHospitalar
from bdd import BancoDados

def executar_casos_de_teste():
    sistema = SistemaHospitalar()
    banco_dados = BancoDados()

    print("CT001 - Cadastro de Paciente")
    usuario1 = sistema.cadastrar_usuario("João Silva", "joao@gmail.com", "123456789", "senha123")
    print(usuario1.exibir_informacoes())

    print("\nCT002 - Agendamento de Consulta")
    medico1 = sistema.cadastrar_medico("Dra. Maria", "Cardiologia", "CRM987654")
    consulta1 = sistema.agendar_consulta(usuario1, medico1, "07-11-2024")
    print(consulta1.exibir_detalhes())

    print("\nCT003 - Login de Usuário")
    print(usuario1.login("joao@gmail.com", "senha123"))

    print("\nCT004 - Acesso ao Perfil de Usuário")
    print(usuario1.exibir_informacoes())

    print("\nCT005 - Cadastro de Médico")
    medico2 = sistema.cadastrar_medico("Dr. Paulo", "Neurologia", "CRM123")

if __name__ == "__main__":
    InterfaceSistemaHospitalar()
    executar_casos_de_teste()