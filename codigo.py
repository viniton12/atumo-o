#entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
# fazer login
# importar a base de dados
# cadastrar um produto
# repetir para todos os produtos

import pyautogui
import time
import pandas as pd
# determina a velocidade que o programa vai rodar
pyautogui.PAUSE = 1

# abrir o edge
pyautogui.press("Win")
pyautogui.write("Edge")
pyautogui.press("enter")

#digite o site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(4) # determina um tempo de espera apenas para essa função
print(pyautogui.position()) # indica a posiçaõ do mouse na tela

# fazer login
pyautogui.click(x=746, y=437)# a posição em que o programa deve clicar com o mouse para fazer login
pyautogui.write("viniciuscalisto09@gmail.com")

#preecher a senha
pyautogui.press("tab")
pyautogui.write("minhasenha1213")

#logar
pyautogui.press("tab")
pyautogui.press("enter")

#espera de 4 para a próxima pagina carregar
time.sleep(4)

#importar uma base de dados
pd.read_csv("produtos.csv")


df = pd.read_csv("produtos.csv") #armazena o arquivo na variável
print(df)


#cadastrar um produto
for linha in df.index: # o programa vai percorrer todas as linhas das tabela
    time.sleep(4)
    pyautogui.click(x=658, y=450)

    codigo = str(df.loc[linha, "codigo"])
    pyautogui.write(codigo)

    pyautogui.press("tab")
    marca = df.loc[linha, "marca"] #indica a linha e a coluna para ser percorrida
    pyautogui.write(marca)

    pyautogui.press("tab")
    tipo = str(df.loc[linha, 'tipo'])
    pyautogui.write(tipo)

    pyautogui.press("tab")
    categoria = str(df.loc[linha, 'categoria'])
    pyautogui.write(categoria)

    pyautogui.press("tab")
    preco_unitario = str(df.loc[linha, 'categoria'])
    pyautogui.write(preco_unitario)

    pyautogui.press("tab")
    custo = str(df.loc[lin ha, 'custo'])
    pyautogui.write(custo)

    pyautogui.press("tab")
    obs = str(df.loc[linha, 'obs'])
    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(10000) # números negativos fazem a tela rolar para baixo e  número positivos rolam a tela para cima
