# 28 Escreva um programa que peça ao usuário para inserir uma palavra e verifique se ela tem mais de 5 letras.
#IAused

def main():
    palavra = input("Digite uma palavra: ")
    if len(palavra) > 5:
        print("A palavra tem mais de 5 letras.")
    else:
        print("A palavra não tem mais de 5 letras.")

if __name__ == "__main__":
    main()
