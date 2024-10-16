import tkinter as tk
from tkinter import ttk
from bdd import BancoDados

class InterfaceSistemaHospitalar:
    def __init__(self):
        self.banco_dados = BancoDados() 
        self.janela = tk.Tk()
        self.janela.title("Viva Flow - Sistema Hospitalar")
        self.janela.geometry("800x600")
        self.janela.configure(bg="#0f3157")

        self.frame_cabecalho = tk.Frame(self.janela, bg="#53c89b", height=100)
        self.frame_cabecalho.pack(fill="x")

        self.titulo = tk.Label(
            self.frame_cabecalho,
            text="Viva Flow - Sistema Hospitalar",
            font=("Helvetica", 24, "bold"),
            fg="#ffffff",
            bg="#53c89b"
        )
        self.titulo.pack(pady=20)

        self.frame_conteudo = tk.Frame(self.janela, bg="#0f3157")
        self.frame_conteudo.pack(pady=20)

        self.abas = ttk.Notebook(self.frame_conteudo)
        self.abas.pack(fill='both', expand=True)

        self.pagina_agendamento = ttk.Frame(self.abas)
        self.abas.add(self.pagina_agendamento, text='Agendar Consulta')
        self.criar_tela_agendamento()

        self.pagina_visualizacao = ttk.Frame(self.abas)
        self.abas.add(self.pagina_visualizacao, text='Visualizar Agendamentos')
        self.criar_tela_visualizacao()

        self.janela.mainloop()

    def criar_tela_agendamento(self):
        self.label_agendamento = tk.Label(
            self.pagina_agendamento, 
            text="Agendar Consulta", 
            font=("Helvetica", 18, "bold"), 
            fg="#ffffff", 
            bg="#0f3157"
        )
        self.label_agendamento.grid(row=0, column=0, pady=10, padx=10)

        self.entry_nome_paciente = self.criar_input("Nome do Paciente:", 1)
        self.entry_nome_medico = self.criar_input("Nome do Médico:", 2)
        self.entry_data = self.criar_input("Data da Consulta:", 3)

        self.botao_agendar = tk.Button(
            self.pagina_agendamento, 
            text="Agendar", 
            width=20, 
            bg="#53c89b", 
            fg="#ffffff", 
            font=("Helvetica", 12, "bold"),
            command=self.agendar_consulta
        )
        self.botao_agendar.grid(row=4, column=1, pady=20)

    def criar_input(self, texto, linha):
        label = tk.Label(self.pagina_agendamento, text=texto, fg="#ffffff", bg="#0f3157")
        label.grid(row=linha, column=0, pady=5, padx=10, sticky="w")
        entry = tk.Entry(self.pagina_agendamento, width=30)
        entry.grid(row=linha, column=1, pady=5, padx=10)
        return entry

    def agendar_consulta(self):
        nome_paciente = self.entry_nome_paciente.get()
        nome_medico = self.entry_nome_medico.get()
        data = self.entry_data.get()

        self.banco_dados.agendar_consulta(nome_paciente, nome_medico, data)
        print(f"Consulta agendada para {nome_paciente} com o Dr. {nome_medico} no dia {data}.")
        
        self.atualizar_visualizacao()

    def criar_tela_visualizacao(self):
        self.label_visualizacao = tk.Label(
            self.pagina_visualizacao, 
            text="Agendamentos Cadastrados", 
            font=("Helvetica", 18, "bold"), 
            fg="#ffffff", 
            bg="#0f3157"
        )
        self.label_visualizacao.pack(pady=10)

        self.treeview_agendamentos = ttk.Treeview(self.pagina_visualizacao, columns=("Paciente", "Médico", "Data"), show='headings')
        self.treeview_agendamentos.heading("Paciente", text="Paciente")
        self.treeview_agendamentos.heading("Médico", text="Médico")
        self.treeview_agendamentos.heading("Data", text="Data")

        self.treeview_agendamentos.pack(fill='both', expand=True)

        self.atualizar_visualizacao()

    def atualizar_visualizacao(self):
        for item in self.treeview_agendamentos.get_children():
            self.treeview_agendamentos.delete(item)

        agendamentos = self.banco_dados.obter_agendamentos()
        for agendamento in agendamentos:
            self.treeview_agendamentos.insert("", "end", values=agendamento)
