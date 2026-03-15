import sqlite3
from tkinter import messagebox

class SistemaDeRegistro:
    def __init__(self):
        self.com = sqlite3.connect('estudante.db')
        self.cursor = self.com.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS estudantes (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                nome TEXT NOT NULL,
                                email TEXT NOT NULL,
                                tel TEXT NOT NULL,
                                sexo TEXT NOT NULL,
                                data_nascimento TEXT NOT NULL,
                                endereco TEXT NOT NULL,
                                curso TEXT NOT NULL,
                                picture TEXT NOT NULL)''')
    def register_student(self, estudantes):
        self.cursor.execute("INSERT INTO estudantes(nome, email, tel, sexo, data_nascimento, endereco, curso, picture) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (estudantes))
        self.com.commit()

        messagebox.showinfo("Sucesso", "Estudante registrado com sucesso!")

    def view_all_students(self):
        self.cursor.execute("SELECT * FROM estudantes")
        dados = self.cursor.fetchall()

        return dados

    def search_student(self, id):
        self.cursor.execute("SELECT * FROM estudantes WHERE id=?", (id,))
        dados = self.cursor.fetchone()
        
        return dados

    
    def update_student(self, novo_valores):
        query = "UPDATE estudantes SET nome=?, email=?, tel=?, sexo=?, data_nascimento=?, endereco=?, curso=?, picture=? WHERE id=? "
        self.cursor.execute(query,novo_valores)
        self.com.commit()
        
        messagebox.showinfo("Sucesso", f"Estudante com ID:{novo_valores[8]} foi atualizado!")

    def delete_student(self, id):
        self.cursor.execute("DELETE FROM estudantes WHERE id=?", (id,))
        self.com.commit()

        messagebox.showinfo("Sucesso", f"Estudante com ID:{id} foi Deletado!")

sistema_de_registro = SistemaDeRegistro()