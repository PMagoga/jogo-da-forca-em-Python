# Importando as bibliotecas necessárias
import random
from os import system, name

# Função para limpar a tela a cada execução
def limpa_tela():
    
    # Se o usuário estiver com Windows
    if name == 'nt':
        _ = system('cls')
        
    # Se o usuário estiver com Mac ou Linux
    else:
        _ = system('clear')
        

# Função para iniciar o jogo
def game():
    
    limpa_tela()
    print("\nBem-vindo ao jogo da forca!")
    print("Tente adivinhar a palavra abaixo:\n")
    
    # Lista de palavras para o jogo
    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']
    
    # Escolhar randomicamente uma palavra
    palavra = random.choice(palavras)
    
    # Usando list comprehension para a palavra a ser descoberta
    letras_descobertas = ['_' for letra in palavra]
    
    # Exibir o número de chances
    chances = 6
    
    # Lista para as palavras erradas
    letras_erradas = []
    
    while chances > 0:
        
        print(" ".join(letras_descobertas))
        print("\nChances restantes:", chances)
        print("Letras erradas:", " ".join(letras_erradas))
        
        # Tentativa
        tentativa = input("\nDigite uma letra: ").lower()
        
        # Condicional para verificar se existe a letra
        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
            else:
                chances -= 1
                letras_erradas.append[tentativa]
                
                