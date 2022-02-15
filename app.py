import time
score = 0
answer_first = 0

while answer_first != "S":
    print("Seja bem Vindo Ao Quiz!")
    time.sleep(2)
    answer = str(
        input("Você quer jogar? "))
    answer_first = answer[0].upper()
    time.sleep(1)

print("Ok, vamos jogar então!")
print("Você tem 1 tentativa para cada pergunta")

time.sleep(3)
print("")
print("\033[1m1 - Qual o menor e o maior país do mundo?\033[m")
print("a) Vaticano e Rússia, b) Nauru e China, c) Mônaco e Canadá, d) Malta e Estados Unidos, e) São Marino e Índia")
first_question = str(input("Resposta: "))
if first_question[0].upper() != "A":
    print("\033[1;31mAlternativa errada!\033[m")
    print("Tente acertar a segunda questão.")
else:
    score += 1
    print("\033[1;32mAlternativa correta, parabéns!\033[m")
    print("Vamos para a segunda questão")

time.sleep(3)
print("")
print("\033[1m2 - Qual o livro mais vendido no mundo depois da Bíblia?\033[m")
print("a) O Senhor dos Anéis, b) Dom Quixote, c) O Pequeno Príncipe, d) Ela, a Feiticeira, e) Um Conto de Duas Cidades")
second_question = str(input("Resposta: "))
if second_question[0].upper() != "B":
    print("\033[1;31mAlternativa errada!\033[m")
    print("Tente acertar a terceira questão.")
else:
    score += 1
    print("\033[1;32mAlternativa correta, parabéns!\033[m")
    print("Vamos para a terceira questão")

time.sleep(3)
print("")
print("\033[1m3 - Quais os países que têm a maior e a menor expectativa de vida do mundo?\033[m")
print("a) Japão e Serra Leoa, b) Austrália e Afeganistão, c) Itália e Chade, d) Brasil e Congo, e) Estados Unidos e Angola")
third_question = str(input("Resposta: "))
if third_question[0].upper() != "A":
    print("\033[1;31mAlternativa errada!\033[m")
    print("Tente acertar a quarta questão.")
else:
    score += 1
    print("\033[1;32mAlternativa correta, parabéns!\033[m")
    print("Vamos para a quarta questão")

time.sleep(3)
print("")
print("\033[1m4 - Em que período da pré-história o fogo foi descoberto?\033[m")
print("a) Neolítico, b) Paleolítico, c) Idade dos Metais, d) Período da Pedra Polida, e) Idade Média")
fourth_question = str(input("Resposta: "))
if fourth_question[0].upper() != "B":
    print("\033[1;31mAlternativa errada!\033[m")
    print("Tente acertar a última.")
else:
    score += 1
    print("\033[1;32mAlternativa correta, parabéns!\033[m")
    print("Vamos para a última questão")

time.sleep(3)
print("")
print("\033[1m5 - Quem pintou o teto da capela sistina?\033[m")
print("a) Michelangelo, b) Leonardo da Vinci, c) Rafael, d) Sandro Botticelli, e) Donatello")
fifth_question = str(input("Resposta: "))
if fifth_question[0].upper() != "A":
    print("\033[1;31mAlternativa errada!\033[m")
else:
    score += 1
    print("\033[1;32mAlternativa correta, parabéns!\033[m")


percentage = (score / 5) * 100
print("")
print("Você chegou ao final do jogo!")
print("Calculando Resultados!")
time.sleep(3)
print("Você acertou {} questões.".format(str(score)))
print("Você teve uma porcentagem de acerto de {}%.".format(str(percentage)))
