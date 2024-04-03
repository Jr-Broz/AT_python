import random
from perguntas import *

def randomizar_pergunta():
    pergunta = {
                1: pergunta_um, 
                2: pergunta_dois,
                3: pergunta_tres,
                4: pergunta_quatro,
                5: pergunta_cinco,
                6: pergunta_seis,
                7: pergunta_sete,
                8: pergunta_oito,
                9: pergunta_nove,
                10:pergunta_dez,
                11: pergunta_onze,
                12:pergunta_doze,
                13: pergunta_treze,
                14: pergunta_quatorze,
                15: pergunta_quinze
}

    while quantidade_acertos != 5 or quantidade_erros != 5:

        escolha_aleatoria = random.randint(1,15)
        
        x = pergunta[escolha_aleatoria]() # acessando no dicionário o valor referente a key que é gerada na variavel "Escolha_aleatoria" e sua função 
        
        if quantidade_acertos == 5:     
            print("Você Chegou ao final do JOGO PARABÉNS! ")        
            
            resposta = input("Quer jogar novamente?   ")
            
            if resposta == '1':
                
                randomizar_pergunta()
                
            if resposta == '2':
                print("Ok, obrigado por jogar")

        if quantidade_erros >= 5: 
            print("Voce perdeu, Obrigado por jogar.")
            break

...
randomizar_pergunta()