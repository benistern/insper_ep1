# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 13:00:32 2018

@author: felip
"""
import json
from firebase import firebase
firebase = firebase.FirebaseApplication('https://ep1-dsoft-b6125.firebaseio.com/ep1-dsoft-b6125', None)
result = firebase.get('https://ep1-dsoft-b6125.firebaseio.com/ep1-dsoft-b6125', None)
controle_loja = result
with open('ep1.json','r') as arquivo:
    conteudo = arquivo.read().strip()
if conteudo:
    controle_loja = json.loads(conteudo)
else:
    controle_loja = {}

lojas = []
controle_estoque = {}
aberto = True
aberto2 = True
while aberto:
    print("0 - Nova loja\n1 - Selecionar loja")
    x = int(input("Faça sua escolha: "))
 
    if x == 1:
        if lojas != []:
            for i in range(len(lojas)):
                print(i," - ",lojas[i])
            n = int(input('Escolha a loja: '))
            if 0 <= n < len(lojas):
                controle_loja[lojas[n]] = controle_estoque
        else:
            print("Nenhuma loja cadastrada\n")
            print("0 - Nova loja\n1 - Selecionar loja")
            x = int(input("Faça sua escolha: "))    
    
    if x == 0:
        nome = input("Nome da loja: ")
        while nome in controle_loja:
            print("Loja já cadastrada")
            nome = input("Nome da loja: ")
        else:
            lojas.append(nome)
            controle_loja[nome] = controle_estoque

    while aberto2:
        print("\nControle de estoque\n\n0 - sair\n1 - adicionar item\n2 - remover item\n3 - alterar item\n4 - imprimir estoque")
        # aqui o usuario escolhe a acao
    
        a = (input("Faça sua escolha: "))
    
        # se o usuario colocar algo diferente de 0, 1, 2, 3, 4 o codigo fala que nao pode
        try:
            a=int(a)
            if a>4 or a != int(a):
                print("Valor inválido")
            

        #se o programa for trava ele printa valor invalido        
        except:
            print("Valor inválido")
        
            
        if a == 0:
            print("Até mais")
            aberto = False
            aberto2 = False
        
        # adicionar item
        elif a == 1:
            produto = str(input("Nome do produto: "))
            if produto in controle_estoque:
                print("Produto já cadastrado")
            else:
                c = int(input("Quantidade inicial: "))
                while c < 0:
                    print("A quantidade inicial não pode ser negativa")
                    c = int(input("Quantidade inicial: "))
                j = float(input("Preço unitário: "))
                while j < 0:
                    print("O preço unitário não pode ser negativo")
                    j = float(input("Preço unitário: "))
                if produto not in controle_estoque and c>0 and j>0:
                    controle_estoque[produto]= {"quantidade": c, "preço": j}  
    
        #remover item        
        elif a == 2:
            d = str(input("Nome do produto: "))
            if d not in controle_estoque:
                print("Elemento não encontrado")
            else:
                del controle_estoque[d]
    
    
        #alterar item
        elif a == 3:
            print("0 - Alterar quantidade")
            print("1 - Alterar Preço unitário")
            k = int(input("Faça sua escolha: "))
        
            if k == 0:
                e = str(input("Nome do produto: "))
                while e not in controle_estoque:
                    print("Elemento não encontrado")
                    e = str(input("Nome do produto: "))
                else:
                    f = int(input("Quantidade: "))
                    controle_estoque[e]["quantidade"] += f
            elif k == 1:
                e = str(input("Nome do produto: "))
                while e not in controle_estoque:
                    print("Elemento não encontrado")
                    e = str(input("Nome do produto: "))
                else:           
                    f = float(input("Novo preço: "))
                    controle_estoque[e]["preço"] = f
            
        #imprimir estoque
        elif a==4:
            quantidade_negativa = []
            valor_monetario = 0
            for i in controle_estoque:
                print("{0}: Quantidade: {1}, Preço unitário: R${2}".format(i,controle_estoque[i]["quantidade"],controle_estoque[i]["preço"]))
                if controle_estoque[i]["quantidade"] < 0:
                    quantidade_negativa.append(i)
                for i in controle_estoque.values():
                    if i["quantidade"] > 0:
                        valor_monetario += i["quantidade"]*i["preço"]
                if quantidade_negativa != []:
                    print("Os produtos com quantidade de estoque negativa são: {}".format(', '.join(quantidade_negativa)))
            print("O valor monetário total em estoque é: {}".format(valor_monetario))
        
        
with open('ep1.json', 'w') as arquivo2:
    arquivo2.write(json.dumps(controle_loja))
firebase.put('https://ep1-dsoft-b6125.firebaseio.com/', 'ep1-dsoft-b6125', controle_loja)

  