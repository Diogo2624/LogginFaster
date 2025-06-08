import pyautogui
import os
import time

contas = {
    "Conta 1": "Ahsay",
    "Conta 2": "Insomianics",
    "Conta 3": "The Gui is Gay",
    "Conta 4": "NicosNic",
    "Conta 5": "NadaBom155costaGold",
    "Conta 6": "Xoxotopolis",
}

print("Eai Chefia, em qual conta quer logar?")
for chave, nome in contas.items():
    print(f"{chave}: {nome}")

caminho = r"C:\Loggin"
arquivo_nome = "Contas.txt"
caminho_arquivo = os.path.join(caminho, arquivo_nome)
posicao = pyautogui.position()
x = 461
y = 400

def valorant():
    pyautogui.press("win")
    pyautogui.write("valorant")
    pyautogui.press("enter")

def conta1():
    valorant()
    time.sleep(15)
    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        linhas = f.readlines()
        linha = linhas[0]
        _, dados = linha.split("=")
        usuario, senha = dados.strip().split(",")
        pyautogui.write(usuario)
        pyautogui.press("tab")
        pyautogui.write(senha)
        pyautogui.press("enter")
        pyautogui.moveTo(x, y, duration= 0.5)
        time.sleep(15)
        pyautogui.click()
        

def conta2():
    valorant()
    time.sleep(15)
    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        linhas = f.readlines()
        linha = linhas[1]
        _, dados = linha.split("=")
        usuario, senha = dados.strip().split(",")
        pyautogui.write(usuario)
        pyautogui.press("tab")
        pyautogui.write(senha)
        pyautogui.press("enter")
        pyautogui.moveTo(x, y, duration= 0.5)
        time.sleep(15)
        pyautogui.click()
        

def conta3():
    valorant()
    time.sleep(15)
    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        linhas = f.readlines()
        linha = linhas[2]
        _, dados = linha.split("=")
        usuario, senha = dados.strip().split(",")
        pyautogui.write(usuario)
        pyautogui.press("tab")
        pyautogui.write(senha)
        pyautogui.press("enter")
        pyautogui.moveTo(x, y, duration= 0.5)
        time.sleep(15)
        pyautogui.click()

def conta4():
    valorant()
    time.sleep(15)
    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        linhas = f.readlines()
        linha = linhas[3]
        _, dados = linha.split("=")
        usuario, senha = dados.strip().split(",")
        pyautogui.write(usuario)
        pyautogui.press("tab")
        pyautogui.write(senha)
        pyautogui.press("enter")
        pyautogui.moveTo(x, y, duration= 0.5)
        time.sleep(15)
        pyautogui.click()

def conta5():
    valorant()
    time.sleep(15)
    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        linhas = f.readlines()
        linha = linhas[4]
        _, dados = linha.split("=")
        usuario, senha = dados.strip().split(",")
        pyautogui.write(usuario)
        pyautogui.press("tab")
        pyautogui.write(senha)
        pyautogui.press("enter")
        pyautogui.moveTo(x, y, duration= 0.5)
        time.sleep(15)
        pyautogui.click()

def conta6():
    valorant()
    time.sleep(15)
    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        linhas = f.readlines()
        linha = linhas[5]
        _, dados = linha.split("=")
        usuario, senha = dados.strip().split(",")
        pyautogui.write(usuario)
        pyautogui.press("tab")
        pyautogui.write(senha)
        pyautogui.press("enter")
        pyautogui.moveTo(x, y, duration= 0.5)
        time.sleep(15)
        pyautogui.click()

        
def escolha():
    opcao = input("Digite o número da conta que quer logar: ")
    if opcao == "1":
        conta1()
    elif opcao == "2":
        conta2()
    elif opcao == "3":
        conta3()
    elif opcao == "4":
        conta4()
    elif opcao == "5":
        conta5()
    elif opcao == "6":
        conta6()
    else:
        print("Por favor, digite um número válido")
        return escolha()
    

escolha()

