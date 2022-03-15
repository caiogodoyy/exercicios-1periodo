nota = float(input())
quantListas = int(input())
notasListas = []

i = 0
while quantListas > i:
    notasListas.append(float(input()))
    i = i + 1

x = sum(notasListas)
mediaListas = x / quantListas

notaFinal = (nota * 70 + mediaListas * 30) / 100
print(f"{notaFinal:5.2f}")
if notaFinal >= 0 and notaFinal < 3:
    print("RED ZONE!")
if notaFinal >= 3 and notaFinal < 5:
    print("DA PARA RECUPERAR!")
if notaFinal >= 5 and notaFinal < 7:
    print("QUASE LA!")
if notaFinal >= 7 and notaFinal < 9:
    print("TA FAVORAVEL!")
if notaFinal >= 9:
    print("EXCELENTE!")