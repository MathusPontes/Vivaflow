class Consulta:
    def __init__(self, paciente, medico, data):
        self.paciente = paciente
        self.medico = medico
        self.data = data

    def exibir_detalhes(self):
        return f"Consulta de {self.paciente.nome} com {self.medico.nome} no dia {self.data}"

    def excluir_consulta(self):
        return f"Consulta de {self.paciente.nome} com {self.medico.nome} foi excluída."
