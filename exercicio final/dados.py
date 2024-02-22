from datetime import date
medicoes = [
    {"caminhao": "12400", "data": date(2024,1,2), "medicao": 12980, "litros": 300}
    ,{"caminhao": "12300", "data": date(2024,1,2), "medicao": 12480, "litros": 300}
    ,{"caminhao": "12400", "data": date(2024,1,3), "medicao": 14285, "litros": 290}
    ,{"caminhao": "12300", "data": date(2024,1,3), "medicao": 13608, "litros": 240}
    ,{"caminhao": "12400", "data": date(2024,1,4), "medicao": 15695, "litros": 300}
    ,{"caminhao": "12400", "data": date(2024,1,4), "medicao": 14708, "litros": 220}
    ,{"caminhao": "12400", "data": date(2024,1,5), "medicao": 16145, "litros": 100}
    ,{"caminhao": "12400", "data": date(2024,1,5), "medicao": 15923, "litros": 270}
]

for i in range(5): # for (int i=0; i<=5; i++) {} ou for (element : elements ){}
    medicao = medicoes[i]

print("Data"+" "*6,"Caminhão", "Medição", "Litros", "Consumo")
for i,medicao in enumerate(medicoes):
    consumo = 0
    if i>0 and medicoes[i-1]['caminhao']==medicao['caminhao']:
        consumo = (medicao["medicao"]-medicoes[i-1]["medicao"])/medicao['litros']

    print( medicao['data'], medicao["caminhao"]+" "*3, str(medicao["medicao"])+" "*2, medicao["litros"], consumo )