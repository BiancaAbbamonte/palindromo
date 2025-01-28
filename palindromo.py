import string


def verificar_palindromo(texto):

    word = texto.replace(" ", "")
    word = word.translate(str.maketrans('', '', string.punctuation))
    word = word.lower()

    print(word)

    if word == word[::-1]:
        return f"{texto} é palindromo"
    else:
        return f"{texto} não é palindromo"

teste1 = verificar_palindromo("Anotaram a data da maratona")
print(teste1)
teste2 = verificar_palindromo("Amora")
print(teste2)
teste3 = verificar_palindromo("Ame o poema")
print(teste3)


#[::-1] significa:
#obj[início:fim:passo]

#"Comece do final e vá até o início, pegando os elementos de trás para frente."

#s = "python"
#print(s[::2]) => pto