class Medico:
    def __init__(self, nome, especialidade, crm, email):
        self.nome = nome
        self.especialidade = especialidade
        self.crm = crm
        self.email = email

    def __str__(self):
        return f"Dr. {self.nome} - Especialidade: {self.especialidade} - CRM: {self.crm} - Email: {self.email}"

