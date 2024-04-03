import random
def criar_senha():
    
    """
    Funcao que cria uma senha aleatória, baseada no tamanho que o usuário quer criptografa com a cifra de césar
    """
    caracteres = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z',
                  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z',
                  '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                  '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', '\\',
                  ';', ':', "'", '"', ',', '.', '/', '<', '>', '?', '`', '~']

    resposta_tamanaho = int(input('Qual tamanho da senha que vc quer ? : '))

    palavras_aleatorias = random.choices(caracteres, weights=None, cum_weights=None, k=resposta_tamanaho)
    palavras_aleatorias = str.join('', palavras_aleatorias)

    print(f'Sua senha gerada é: "{palavras_aleatorias}"')
    print('obrigado por utilizar este software.')
    
    print("---------------------------------------------")
    
        
def criptografar():
    
    """
    Função que recebe 3 inputs do usuário, criptografa os dados e os salva em um arquivo de texto, 
    seguindo cada qual categoria de gasto.

    O método ord() retorna o número do caracter passado como parametro presente na tabela ASCII.
    
    O método chr() retorna o caracter baseado no parâmetro da tabela ASCII.
    """
    
    senha_para_criptografia = input("Qual senha vc quer criptografa:  ")
    username = input("Username:  ")
    servico = input("servico:  ")
    
    numero_de_troca_posicao = int(input("Escreva o número de troca de posição, de 2 a 6:  "))    
    
    senha_criptografada = []
    username_criptografado = []
    servico_criptografado = []
    
    print("-" * 30)
    
    for c in senha_para_criptografia:
        crip = ord(c) + numero_de_troca_posicao
        senha_criptografada.append(chr(crip))
    
    for c in username:
        crip = ord(c) + numero_de_troca_posicao
        username_criptografado.append(chr(crip))
    
    for c in servico:
        crip = ord(c) + numero_de_troca_posicao
        servico_criptografado.append(chr(crip))
    
    checar_username = input("Escreva seu username, por favor para checarmos se podes visualizar sua senha:  ")
    checar_servico = input("Escreva seu serviço, por favor:  ")

    if checar_username == username and checar_servico == servico:
        print("Acesso concedido! , pode acessar seus dados! ")
        
        with open('dados_criptografados.txt', 'w') as arquivo:

            arquivo.write(f"Senha criptografada: {''.join(senha_criptografada)}\n")
            arquivo.write(f"Username criptografado: {''.join(username_criptografado)}\n")
            arquivo.write(f"Servico criptografado: {''.join(servico_criptografado)}\n")
            arquivo.write("---------------------------------------------------------------")
        
   
        print(f"Senha: {senha_para_criptografia}")
        print(f"Username: {username}")
        print(f"Servico: {servico}")
    else:
        print("Você não tem permissão para acessar esta conta.")
                
def menu():
    
    
    while True:
        resposta = input("[1] Para gerar senha e [2] para criptografa-lá:, [3] Para sair  ")
        
        match(resposta):
                
                case '1':
                    criar_senha()
                
                case '2':
                    criptografar()
                                        
                case '3': # Case _ é o equivalente a un else em um if-elif-else
                    break
                
                case _:
                    print("Comando não reconhecido")                
        
menu()