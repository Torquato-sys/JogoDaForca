import os



palavra = input("Digite a palavra secreta: ").lower().strip()
os.system('clear')

digitados = []
acertos = []
erros = 0

while True:
    try:
        senha = ""
        for letra in palavra:
            senha += letra if letra in acertos else "."
        print(senha)
        if senha == palavra:
            print("Você acertou!")
            break
        while True:
            tentativa = input("\nDigite uma letra: ").lower().strip()
            os.system('clear')
            if len(tentativa) != 1 or not tentativa.isalpha():
                print("Por favor, digite apenas uma letra.")
                continue
            elif tentativa in digitados:
                print("Você já tentou esta letra!")
                continue
            else:
                break
        digitados += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print("Você errou!")
        print("X==:==\nX  :  ")
        print("X  0  " if erros >= 1 else "X")
        linha2 = ""
        if erros == 2:
            linha2 = "  |  "
        elif erros == 3:
            linha2 = " /|  "
        elif erros >= 4:
            linha2 = " /|\ "
        print(f"X{linha2}")
        linha3 = ""
        if erros == 5:
            linha3 += " /  "
        elif erros >= 6:
            linha3 += " / \ "
        print(f"X{linha3}")
        print("X\n=========")
        if erros == 6:
            print("Enforcado!")
            break
    except ValueError as e:
        print("Erro:", e)
