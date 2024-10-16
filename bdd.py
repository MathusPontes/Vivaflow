import sqlite3

class BancoDados:
    def __init__(self, db_name='sistema_hospitalar.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS medicos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    especialidade TEXT NOT NULL,
                    crm TEXT NOT NULL,
                    email TEXT NOT NULL
                )
            ''')
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS agendamentos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome_paciente TEXT NOT NULL,
                    nome_medico TEXT NOT NULL,
                    data TEXT NOT NULL
                )
            ''')

    def cadastrar_medico(self, nome, especialidade, crm, email):
        with self.conn:
            self.conn.execute('''
                INSERT INTO medicos (nome, especialidade, crm, email)
                VALUES (?, ?, ?, ?)
            ''', (nome, especialidade, crm, email))

    def obter_medicos(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM medicos')
        return cursor.fetchall()

    def agendar_consulta(self, nome_paciente, nome_medico, data):
        with self.conn:
            self.conn.execute('''
                INSERT INTO agendamentos (nome_paciente, nome_medico, data)
                VALUES (?, ?, ?)
            ''', (nome_paciente, nome_medico, data))

    def obter_agendamentos(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT nome_paciente, nome_medico, data FROM agendamentos')
        return cursor.fetchall()

    def fechar_conexao(self):
        self.conn.close()
