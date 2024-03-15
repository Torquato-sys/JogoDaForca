import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def desenhar_forca(erros):
    forca = [
        """
           _____
          |     |
          |     
          |     
          |      
          |     
        __|__
        """,
        """
           _____
          |     |
          |     O
          |     
          |      
          |     
        __|__
        """,
        """
           _____
          |     |
          |     O
          |     |
          |      
          |     
        __|__
        """,
        """
           _____
          |     |
          |     O
          |    /|
          |      
          |     
        __|__
        """,
        """
           _____
          |     |
          |     O
          |    /|\\
          |      
          |     
        __|__
        """,
        """
           _____
          |     |
          |     O
          |    /|\\
          |    / 
          |     
        __|__
        """,
        """
           _____
          |     |
          |     O
          |    /|\\
          |    / \\
          |     
        __|__
        """
    ]
    return forca[erros]

def obter_palavra():
    palavra = input("Digite a palavra secreta: ").lower().strip()
    limpar_tela()
    return palavra

def imprimir_forca(palavra_secreta, letras_digitadas, erros):
    for letra in palavra_secreta:
        if letra in letras_digitadas:
            print(letra, end=' ')
        else:
            print('_', end=' ')
    print('\n')
    print(desenhar_forca(erros))

def verificar_fim_de_jogo(palavra_secreta, letras_digitadas, erros):
    for letra in palavra_secreta:
        if letra not in letras_digitadas:
            return False
    return True


def jogar_jogo_da_forca():
    limpar_tela()
    print("Bem-vindo ao Jogo da Forca!\n")
    palavra_secreta = obter_palavra()
    letras_digitadas = []
    erros = 0

    while True:
        imprimir_forca(palavra_secreta, letras_digitadas, erros)
        if verificar_fim_de_jogo(palavra_secreta, letras_digitadas, erros):
            print("Você ganhou! Parabéns!")
            break

        tentativa = input("Digite uma letra: ").lower().strip()
        limpar_tela()
        if tentativa in letras_digitadas:
            print("Você já tentou esta letra! Tente novamente.\n")
            continue
        elif len(tentativa) != 1 or not tentativa.isalpha():
            print("Por favor, digite apenas uma letra.\n")
            continue
        elif tentativa not in palavra_secreta:
            erros += 1
        letras_digitadas.append(tentativa)

        if erros == 6:
            imprimir_forca(palavra_secreta, letras_digitadas, erros)
            print("Você perdeu! A palavra secreta era '{}'.".format(palavra_secreta))
            break

if __name__ == "__main__":
    jogar_jogo_da_forca()
