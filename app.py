score = 0


print("Seja bem Vindo Ao Quiz!")

answer = str(input("Você quer jogar?"))
answer_first = answer[0].upper()

while answer_first != "S":
    print("Seja bem Vindo Ao Quiz!")
    answer = str(
        input("Está afim agora de jogar?"))
    answer_first = answer[0].upper()

print("Ok, vamos jogar então!")
print("Você tem 1 tentativa para cada pergunta")

print("Qual o menor e o maior país do mundo?")
print("a) Vaticano e Rússia, b) Nauru e China, c) Mônaco e Canadá, d) Malta e Estados Unidos, e) São Marino e Índia")
first_question = str(input("Resposta: "))
first_question_corrected = first_question[0].upper()
if first_question_corrected != "A":
    print("Alternativa errada! Tente acertar a próxima.")
else:
    print("Alternativa correta, parabéns!")
    print("Vamos para a próxima")

print("Qual o livro mais vendido no mundo depois da Bíblia?")
print("a) O Senhor dos Anéis, b) Dom Quixote, c) O Pequeno Príncipe, d) Ela, a Feiticeira, e) Um Conto de Duas Cidades")
second_question = str(input("Resposta: "))
second_question_corrected = second_question[0].upper()
if second_question_corrected != "B":
    print("Alternativa errada! Tente acertar a próxima.")
else:
    print("Alternativa correta, parabéns!")
    print("Vamos para a próxima")
