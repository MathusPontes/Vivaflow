class Usuario:
    def __init__(self, nome, email, telefone, senha):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.senha = senha
        self.logado = False

    def exibir_informacoes(self):
        return f"Paciente: {self.nome}, Email: {self.email}, Telefone: {self.telefone}"

    def login(self, email, senha):
        if self.email == email and self.senha == senha:
            self.logado = True
            return "Login realizado com sucesso."
        else:
            return "Credenciais inválidas."

    def logout(self):
        self.logado = False
        return "Logout realizado com sucesso."

    def alterar_perfil(self, novo_nome=None, novo_email=None, novo_telefone=None):
        if novo_nome:
            self.nome = novo_nome
        if novo_email:
            self.email = novo_email
        if novo_telefone:
            self.telefone = novo_telefone
        return "Dados do perfil atualizados com sucesso."

    def recuperar_senha(self, email):
        if self.email == email:
            return f"Sua senha é: {self.senha}"
        else:
            return "Email não encontrado."
