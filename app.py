score = 0


print("Seja bem Vindo Ao Quiz!")

answer = str(input("Você quer jogar?"))
answer_first = answer[0].upper()

while answer_first != "S":
    print("Tudo bem, volte quando quiser jogar!")
    print("Seja bem Vindo Ao Quiz!")
    answer = str(
        input("Está afim agora de jogar?"))
