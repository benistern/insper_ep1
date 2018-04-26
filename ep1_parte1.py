<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 11:10:38 2018

@author: beni stern
"""

controle_estoque = {}
aberto = True
while aberto:
    print("0 - sair")
    print("1 - adicionar item")
    print("2 - remover item")
    print("3 - alterar item")
    print("4 - imprimir estoque")
    # aqui o usuario escolhe a acao
    
    a = int(input("Faça sua escolha: "))
    
    if a == 0:
        print("Até mais")
        aberto = False
  
    # adicionar item
    elif a == 1:
        b = str(input("Nome do produto: "))
        if b in controle_estoque:
            print("Produto já cadastrado")
        else:
            c = int(input("Quantidade inicial: "))
            if c < 0:
                print("A quantidade inicial não pode ser negativa")
            if b not in controle_estoque and c>0:
                controle_estoque[b]= {"quantidade": c}  
    
    #remover item        
    elif a == 2:
        d = str(input("Nome do produto: "))
        if d not in controle_estoque:
            print("Elemento não encontrado")
        else:
            del controle_estoque[d]
    
    
   #alterar item
    elif a == 3:
        e = str(input("Nome do produto: "))
        if e not in controle_estoque:
            print("Elemento não encontrado")
        else:
            f = int(input("Quantidade: "))
            controle_estoque[e]["quantidade"] += f
                        
            
            
    #imprimir estoque
    elif a==4:
        for i in controle_estoque:
            print(str(i)+(": ")+str(controle_estoque[i]["quantidade"]))
    
    
    
    
    
    
    
    
    
    
    
        
    
            
        
=======
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 11:10:38 2018

@author: beni stern
"""

controle_estoque = {}
aberto = True
while aberto:
    print("0 - sair")
    print("1 - adicionar item")
    print("2 - remover item")
    print("3 - alterar item")
    print("4 - imprimir estoque")
    # aqui o usuario escolhe a acao
    
    a = int(input("Faça sua escolha: "))
    
    if a == 0:
        print("Até mais")
        aberto = False
  
    # adicionar item
    elif a == 1:
        b = str(input("Nome do produto: "))
        if b in controle_estoque:
            print("Produto já cadastrado")
        else:
            c = int(input("Quantidade inicial: "))
            if c < 0:
                print("A quantidade inicial não pode ser negativa")
            if b not in controle_estoque and c>0:
                controle_estoque[b]= {"quantidade": c}  
    
    #remover item        
    elif a == 2:
        d = str(input("Nome do produto: "))
        if d not in controle_estoque:
            print("Elemento não encontrado")
        else:
            del controle_estoque[d]
    
    
   #alterar item
    elif a == 3:
        e = str(input("Nome do produto: "))
        if e not in controle_estoque:
            print("Elemento não encontrado")
        else:
            f = int(input("Quantidade: "))
            controle_estoque[e]["quantidade"] += f
                        
            
            
    #imprimir estoque
    elif a==4:
        for i in controle_estoque:
            print(str(i)+(": ")+str(controle_estoque[i]["quantidade"]))
    
    
    
    
    
    
    
    
    
    
    
        
    
            
        
>>>>>>> 9528fa8e20879c8ce7e17bc4ba225dedd950a964
    