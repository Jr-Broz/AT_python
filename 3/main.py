import random

# Probability = element_weight/ sum of all weights -> Sendo weight(2 param de choices) a probabilidade de cada elemento se repetir.

def filmes():
    
    """
    Função que lista de forma aleatória os filmes em cartazes.
    
    Começa como uma lista, entretanto, o método random.choices() não inibe a possibilidade de duplicatas, por isso,
    existe uma conversão para a estrutura de dados SET, que não aceita duplicatas e a remove caso haja alguma.
    Após isso é retornada para uma lista.
    """

    filmes = ["A felicidade nao se compra", "Batman cavaleiro das trevas", "Garota Interrompida", "Jogo da Imitação", "Missão impossível", "Os Incriveis", "Lilo e Stitch", "Dr Estranho", "MIB homens de preto", "2012", "Velozes e Furiosos"]
    filmes_escolhidos =  random.choices(filmes, None, k=3)

    # Transformei em set pra que caso haja duplicatas, ele naturalmente irá remove-las.
    filmes_pre_aprovados = set(filmes_escolhidos) 
    filmes_aprovados = list(filmes_pre_aprovados) #Coloquei novamente em listas caso seja necessário manipula-lás depois

    print(f"Filmes em Cartaz:  {filmes_aprovados}")


def menu():
    
    print("-" * 20)
    """
    Função que simula uma pequena interface gráfica para o usuário.
    """
    
    escolha = input("[1] Para iniciar a compra dos ingressos.   ")
    
    match(escolha):
    
        case '1':
            comprar_ingressos()

def comprar_ingressos():
    
    """
    Função que pega os dados do cliente, nome, quantidade de ingressos, escolha do filme, fileira e qual o identificador da poltrona e os guarda num arquivo.txt
    """
    
    filmes()
    print('-' * 30)
    
    escolha = input("Qual filme você quer escolher ?   ")
    quantidade = int(input("Quantos ingressos você deseja comprar?  "))

    print("-----------------------")
    print("Escolha seu assento abaixo:  sendo x lugares ocupados e _ lugares disponíveis")    
    print("==================================")                
    print("A|xx_xxxxx_x_x_xx_xxxxxx__x_x|1")    
    print("B|___xxx_x_x_xx__x__x__x_xxx_|2")    
    print("C|xx_xx_x_x_x*x_xxxxxx__x_xxx|3")
    print("D|x__xx_xx_x_x_xxxxxx__x_x_xx|4")
    print("E|xx xxxxx_x_x_x*x_xx_xxx__x_|5")
    print("F|____________x______________|6")
 
    print("G|EM MANUTENÇÃO...|7")
    print("H|EM MANUTENÇÃO...|8")
    print("J|EM MANUTENÇÃO...|9")
    print("===================================")
    
    fileira = input("Qual fileira você deseja escolher:  ")
    identificador_poltrona = input("Cada poltrona possui um numero identificador, a direita qual o seu ?   ")

    nome = input("Qual o seu nome?   ")

    print("-" * 30)
    print(f"\nNome do cliente: {nome} | \nFilme: {escolha} | \nQuantidade de ingressos: {quantidade} | \nFileira: {fileira} | \nIdentificador de Poltrona {identificador_poltrona}")
    print("-" * 30)
    print("Obrigado, bom filme.")

    with open ("ingresso_cliente.txt", 'w') as arquivo:
        
        arquivo.write(f"\nNome do cliente: {nome}")
        arquivo.write(f"\nFilme: {escolha}")
        arquivo.write(f"\nQuantidade de ingressos: {quantidade}")
        arquivo.write(f"\nIdentificador de poltrona: {identificador_poltrona}")


#Função que faz a união entre comprar_ingressos() e filmes()
menu()