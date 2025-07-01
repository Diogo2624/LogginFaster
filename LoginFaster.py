import os
import sys
import time
import pyautogui
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel,
    QLineEdit, QMessageBox, QHBoxLayout, 
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt
from cryptography.fernet import Fernet

CAMINHO_ICON = os.path.join(os.path.dirname(__file__), "logo.png")
CAMINHO_IMAGEM_PRINCIPAL = os.path.join(os.path.dirname(__file__), "logo.png")


PASTA = r"C:\Loggin"
ARQUIVO_CONTAS = os.path.join(PASTA, "Contas.txt")
ARQUIVO_CHAVE = os.path.join(PASTA, "key.key")
RESOLUCAO_BASE = (1920, 1080)
X_BASE = 461
Y_BASE = 400


def garantir_estrutura():
    os.makedirs(PASTA, exist_ok=True)
    if not os.path.exists(ARQUIVO_CONTAS):
        with open(ARQUIVO_CONTAS, "wb") as f:
            f.write(b"")
    if not os.path.exists(ARQUIVO_CHAVE):
        chave = Fernet.generate_key()
        with open(ARQUIVO_CHAVE, "wb") as f:
            f.write(chave)


def obter_fernet():
    with open(ARQUIVO_CHAVE, "rb") as f:
        chave = f.read()
    return Fernet(chave)


def salvar_conta(nome, usuario, senha):
    fernet = obter_fernet()
    dados = f"{nome}={usuario},{senha}\n"
    criptografado = fernet.encrypt(dados.encode())

    with open(ARQUIVO_CONTAS, "ab") as f:
        f.write(criptografado + b"\n")


def ler_contas():
    fernet = obter_fernet()
    contas = []
    try:
        with open(ARQUIVO_CONTAS, "rb") as f:
            linhas = f.readlines()
            for linha in linhas:
                try:
                    descriptografado = fernet.decrypt(linha.strip()).decode()
                    contas.append(descriptografado)
                except Exception:
                    continue
    except Exception:
        pass
    return contas


def remover_conta_por_indice(indice):
    contas = ler_contas()
    if 0 <= indice < len(contas):
        contas.pop(indice)
        fernet = obter_fernet()
        with open(ARQUIVO_CONTAS, "wb") as f:
            for conta in contas:
                f.write(fernet.encrypt(conta.encode()) + b"\n")


def posicao_convertida(x_base, y_base):
    largura, altura = pyautogui.size()
    return int((x_base / RESOLUCAO_BASE[0]) * largura), int((y_base / RESOLUCAO_BASE[1]) * altura)


def valorant():
    pyautogui.press("win")
    pyautogui.write("valorant")
    pyautogui.press("enter")

def logar_com_conta(indice):
    valorant()
    time.sleep(15)
    contas = ler_contas()
    if indice < len(contas):
        _, dados = contas[indice].split("=")
        usuario, senha = dados.split(",")
        pyautogui.write(usuario)
        pyautogui.press("tab")
        pyautogui.write(senha)
        pyautogui.press("enter")
        x, y = posicao_convertida(X_BASE, Y_BASE)
        pyautogui.moveTo(x, y, duration=0.5)
        time.sleep(15)
        pyautogui.click()
    else:
        QMessageBox.critical(None, "Erro", "Conta inválida.")


class JanelaAdicionarConta(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Faster")
        self.setFixedSize(400, 400)
        CAMINHO_ICON = os.path.join(os.path.dirname(__file__), "logo.png")
        self.setWindowIcon(QIcon(CAMINHO_ICON))
        self.setStyleSheet("background-color: #1e1e1e; color: white;")
        layout = QVBoxLayout()

        self.image_label = QLabel(self)
        try:
            pixmap = QPixmap(CAMINHO_IMAGEM_PRINCIPAL) 
            if pixmap.isNull():
                raise FileNotFoundError(f"Não foi possível carregar a imagem: {CAMINHO_IMAGEM_PRINCIPAL}. Verifique o caminho.")
            scaled_pixmap = pixmap.scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            self.image_label.setPixmap(scaled_pixmap)
            self.image_label.setAlignment(Qt.AlignCenter) 
            self.image_label.setStyleSheet("margin-bottom: 1px; margin-top: 10px;") 
        except FileNotFoundError as e:
            print(f"Erro: {e}")
            self.image_label.setText("Erro ao carregar imagem.")
            self.image_label.setAlignment(Qt.AlignCenter)
            self.image_label.setStyleSheet("color: red; font-size: 14px; margin-bottom: 20px;")
        layout.addWidget(self.image_label)
        self.label = QLabel("Adicione uma conta.  :)")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 20px; font-weight: bold; margin-top: 50px; margin-right: 150px;")
        layout.addWidget(self.label)

        self.nome = QLineEdit()
        self.nome.setPlaceholderText("Nome da Conta")
        self.nome.setStyleSheet("font-size: 12px; font-weight: bold;")
        layout.addWidget(self.nome)

        self.usuario = QLineEdit()
        self.usuario.setPlaceholderText("Usuário")
        self.usuario.setStyleSheet("font-size: 12px; font-weight: bold;")
        layout.addWidget(self.usuario)

        self.senha = QLineEdit()
        self.senha.setPlaceholderText("Senha")
        self.senha.setEchoMode(QLineEdit.Password)
        self.senha.setStyleSheet("font-size: 12px; font-weight: bold;")
        layout.addWidget(self.senha)

        self.btn_adicionar = QPushButton("Adicionar Conta")
        self.btn_adicionar.clicked.connect(self.adicionar_conta)
        layout.addWidget(self.btn_adicionar)
        self.btn_adicionar.setStyleSheet("""
                    QPushButton {
                        background-color: #D83667;
                        color: white;
                        font-size: 14px;
                        font-weight: bold;
                        padding: 10px;
                        margin-bottom: 5px;
                        border-radius: 6px;
                    }
                    QPushButton:hover {
                        background-color: #FF0000;
                    }
                """)

        self.btn_abrir = QPushButton("Abrir contas salvas")
        self.btn_abrir.clicked.connect(self.abrir_lista)
        layout.addWidget(self.btn_abrir)
        self.btn_abrir.setStyleSheet("""
                    QPushButton {
                        background-color: #D83667;
                        color: white;
                        font-size: 14px;
                        font-weight: bold;
                        padding: 10px;
                        margin-bottom: 5px;
                        border-radius: 6px;
                    }
                    QPushButton:hover {
                        background-color: #FF0000;
                    }
                """)

        self.setLayout(layout)

    def adicionar_conta(self):
        nome = self.nome.text().strip()
        usuario = self.usuario.text().strip()
        senha = self.senha.text().strip()
        if not nome or not usuario or not senha:
            QMessageBox.warning(self, "Erro", "Preencha todos os campos.")
            return
        salvar_conta(nome, usuario, senha)
        QMessageBox.information(self, "Sucesso", f"Conta '{nome}' adicionada com sucesso!")
        self.nome.clear()
        self.usuario.clear()
        self.senha.clear()

    def abrir_lista(self):
        if ler_contas():
            self.janela = JanelaSelecionarConta()
            self.janela.show()
        else:
            QMessageBox.information(self, "Sem contas", "Nenhuma conta adicionada ainda.")


class JanelaSelecionarConta(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Faster - Contas")
        self.setFixedSize(400, 500)
        self.setWindowTitle("Login Faster - Contas")
        self.setFixedSize(400, 500)
        self.setStyleSheet("background-color: #1e1e1e; color: white;")
        self.layout = QVBoxLayout()

        titulo = QLabel("Selecione a conta que deseja logar:")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("font-size: 18px; font-weight: bold; margin: 20px;")
        self.layout.addWidget(titulo)

        self.atualizar_lista()

        self.setLayout(self.layout)

    def atualizar_lista(self):
        contas = ler_contas()
        for i in range(len(contas)):
            nome = contas[i].split("=")[0]

            linha = QHBoxLayout()
            botao = QPushButton(nome)
            botao.setStyleSheet("""
                background-color: #D83667;
                color: white;
                padding: 10px;
                border-radius: 6px;
            }
            QPushButton:hover {
                    background-color: #FF0000;
                    }
            """)
            botao.clicked.connect(lambda _, idx=i: self.logar(idx))

            btn_remover = QPushButton("❌")
            btn_remover.setFixedSize(40, 30)
            btn_remover.clicked.connect(lambda _, idx=i: self.remover(idx))
            btn_remover.setStyleSheet("""
                background-color: #D83667;
                color: white;
                padding: 10px;
                border-radius: 6px;
            }
            QPushButton:hover {
                    background-color: #FF0000;
                    }
            """)

            linha.addWidget(botao)
            linha.addWidget(btn_remover)
            self.layout.addLayout(linha)

    def logar(self, idx):
        self.close()
        logar_com_conta(idx)

    def remover(self, idx):
        remover_conta_por_indice(idx)
        QMessageBox.information(self, "Removido", "Conta removida com sucesso!")
        self.close()
        nova = JanelaSelecionarConta()
        nova.show()


if __name__ == "__main__":
    garantir_estrutura()
    app = QApplication(sys.argv)
    janela = JanelaAdicionarConta()
    janela.show()
    sys.exit(app.exec())
