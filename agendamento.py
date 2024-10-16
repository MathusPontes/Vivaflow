from consulta import Consulta

class Agendamento:
    def __init__(self):
        self.consultas = []

    def agendar_consulta(self, paciente, medico, data):
        consulta = Consulta(paciente, medico, data)
        self.consultas.append(consulta)
        return consulta

    def listar_agendamentos(self):
        return [consulta.exibir_detalhes() for consulta in self.consultas]

    def excluir_consulta(self, consulta):
        if consulta in self.consultas:
            self.consultas.remove(consulta)
            return consulta.excluir_consulta()
        else:
            return "Consulta não encontrada."
