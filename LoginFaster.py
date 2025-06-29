import sys
import os
import time
import pyautogui
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QMessageBox, QHBoxLayout, QLineEdit
)
from PySide6.QtGui import Qt

caminho = r"C:\Loggin"
arquivo_nome = "Contas.txt"
caminho_arquivo = os.path.join(caminho, arquivo_nome)
x = 461
y = 400

# Função para abrir o Valorant
def valorant():
    pyautogui.press("win")
    pyautogui.write("valorant")
    pyautogui.press("enter")

# Função para fazer login com base no índice
def logar_com_conta(numero_conta):
    valorant()
    time.sleep(15)
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            linhas = f.readlines()
            if numero_conta < len(linhas):
                linha = linhas[numero_conta]
                _, dados = linha.strip().split("=")
                usuario, senha = dados.strip().split(",")
                pyautogui.write(usuario)
                pyautogui.press("tab")
                pyautogui.write(senha)
                pyautogui.press("enter")
                pyautogui.moveTo(x, y, duration=0.5)
                time.sleep(15)
                pyautogui.click()
            else:
                raise IndexError("Número da conta inválido.")
    except Exception as e:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Erro ao logar")
        msg.setInformativeText(str(e))
        msg.exec()

class TelaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Faster")
        self.setFixedSize(400, 500)
        self.setStyleSheet("background-color: #1e1e1e;")
        self.layout = QVBoxLayout()

        self.label = QLabel("Selecione a conta que deseja logar:")
        self.label.setStyleSheet("""
            font-size: 22px;
            font-weight: bold;
            margin-bottom: 1px;
            color: #FFFFFF;
        """)
        self.label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label)

        
        try:
            with open(caminho_arquivo, 'r', encoding='utf-8') as f:
                linhas = f.readlines()
                for idx, linha in enumerate(linhas):
                    if "=" in linha:
                        nome_conta = linha.strip().split("=")[0]
                        botao = QPushButton(nome_conta)
                        botao.setStyleSheet("""
                            QPushButton {
                                background-color: #D83667;
                                color: white;
                                padding: 10px 20px;
                                border: none;
                                border-radius: 5px;
                            }
                            QPushButton:hover {
                                background-color: #555;
                            }
                        """)
                        botao.clicked.connect(lambda _, i=idx: self.logar(i))
                        self.layout.addWidget(botao)
        except FileNotFoundError:
            aviso = QMessageBox()
            aviso.setIcon(QMessageBox.Warning)
            aviso.setText("Arquivo de contas não encontrado.")
            aviso.exec()

        self.setLayout(self.layout)

    def logar(self, indice):
        self.close()
        logar_com_conta(indice)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = TelaPrincipal()
    janela.show()
    sys.exit(app.exec())