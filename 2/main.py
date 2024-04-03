saldo = 0

def inserir_saldo():
    
            
    novo_saldo = int(input("Quanto pretende adicionar ao seu saldo ?  "))
    global saldo
    saldo_antigo = saldo
    saldo += novo_saldo
    print(f"Seu saldo antigo R${saldo_antigo} , novo saldo R${saldo}")
    
    resposta = input("Vai querer adicionar novamente? [1] sim [2] nao  ")
        
    if resposta == '1': 

        inserir_saldo()
        
        if resposta == '2': 
            
            menu()
        
def anotar_receitas():
    
    aumento_receita = int(input("Valor ganho:  "))
    fonte_financeira = input("Fonte financeira?:  ")

    global saldo
    saldo_antigo = saldo
    saldo += aumento_receita 

    with open("relatorio_receitas.txt", 'a') as f:
        
        f.writelines(f"Fonte da nova receita: {fonte_financeira} || Valor: {aumento_receita} || Saldo antes do aumento: {saldo_antigo} || Saldo após aumento: {saldo}")
                
    voltar = input("Voltar ao menu ?  [1] Sim  [2] Anotar mais alguma receita:  ")
    
    if voltar == '1': menu()
    if voltar == '2': anotar_receitas()         

def anotar_despesas():
    
    categoria = input("Categoria do gasto:  ").capitalize()
    gasto = int(input("Valor do gasto:  "))
    descricao = input("Motivo do gasto:  ")
    global saldo
    saldo_antigo = saldo
    saldo -= gasto

    if categoria == "lazer".capitalize():    
        
        with open("relatorio_lazer.txt", 'a') as f:
            
            
            f.writelines(f"Categoria: {categoria} , Valor: {gasto} ; {descricao} ;Saldo antes: {saldo_antigo} , Saldo Atual: {saldo} ")
    
    if categoria == "transporte".capitalize():
        
         with open("relatorio_transporte.txt", 'a') as f:
            
            f.writelines(f"categoria: {categoria} , valor: {gasto} ; {descricao} ")
    
    
    elif categoria == "alimentacao".capitalize():
        
         with open("relatorio_alimentacao.txt", 'a') as f:
            
            f.writelines(f"categoria: {categoria} , valor: {gasto} ; {descricao} ")
    
    
def listar_receitas():
        
    with open("relatorio_receitas.txt", 'r') as ler:
        
        print(ler.readlines())
        


def listar_despesas():
    
    resposta = input("Qual categoria voce quer listar?  [1] Lazer [2] Transporte , [3] Alimentacao ")
    
    match(resposta):
        
        case '1':
            lazer()
        case '2':
            transporte()
        case '3':
            alimentacao()
    


def lazer():
    
    with open("relatorio_lazer.txt", 'r') as f:

            print(f.readlines())

def transporte():
 with open("relatorio_transporte.txt", 'r') as f: print(f.readlines())

def alimentacao():
    with open("relatorio_alimentacao.txt", 'r') as f:

            print(f.readlines())
    
    
    
def menu():
    
    while True:
    
        print("\n[1] Adicionar saldo \n[2] Anotar alguma receita \n[3] Listar todas as receitas  \n[4] Anotar despesa \n[5] Listar despesas")
        print('-' * 30)
        resposta = int(input("Escolha:  "))
    
        match(resposta):
                
            case 1:
                inserir_saldo()
            case 2:
                anotar_receitas()
            case 3:
                listar_receitas()
            case 4:
                anotar_despesas()
            case 5:
                listar_despesas()


# anotar_despesas()

menu()