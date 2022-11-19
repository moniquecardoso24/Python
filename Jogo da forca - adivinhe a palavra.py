# Criando um jogo da forca. Adivinhar a palavra correta

secreto = "perfume"
digitadas = [] #lista
chances = 3   # inicia com 3 chances, precisa subtrair a cada tentativa
while True:
    if chances <= 0:
        print("Você perdeu!")
        break
    letra = input("Digite uma letra: ")

    if len(letra) > 1:  # o len conta o número de caracteres
        print("Ah, não vale! Digite apenas uma letra!")
        continue

    digitadas.append(letra)         # o append incrementa a letra na lista. 

    if letra in secreto: #se está no secreto
        print(f"Uhuh, a letra {letra} existe na palavra secreta")
    else:
        print(f"Aff, a letra {letra} não existe na palavra secreta")
        digitadas.pop()  #pop remove a letra repetida no append. POP remove

    secreto_temporário = ""

    for letra_secreta in secreto:
        if letra_secreta in digitadas:   # se a letra secreta estiver na digitada
            secreto_temporário += letra_secreta
        else:
            secreto_temporário += "*"

    print(secreto_temporário)

    if secreto_temporário == secreto:
        print(f"Que legal, você ganhou o jogo!! A palavra era {secreto_temporário}.")
        break
    else:
        print(f"A palavra secreta está assim: {secreto_temporário}.")

    if letra not in secreto:
        chances -= 1   # subtrai 1, subtrai as tentativas
    print(f"Voce ainda tem {chances} chances.")






