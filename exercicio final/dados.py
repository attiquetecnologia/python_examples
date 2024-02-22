from datetime import date
medicoes = [
    {"caminhao": "12400", "data": date(2024,1,2), "medicao": 12980, "litros": 300}
    ,{"caminhao": "12300", "data": date(2024,1,2), "medicao": 12480, "litros": 300}
    ,{"caminhao": "12400", "data": date(2024,1,3), "medicao": 14285, "litros": 290}
    ,{"caminhao": "12300", "data": date(2024,1,3), "medicao": 13608, "litros": 240}
    ,{"caminhao": "12400", "data": date(2024,1,4), "medicao": 15695, "litros": 300}
    ,{"caminhao": "12300", "data": date(2024,1,4), "medicao": 14708, "litros": 220}
    ,{"caminhao": "12400", "data": date(2024,1,5), "medicao": 16145, "litros": 100}
    ,{"caminhao": "12300", "data": date(2024,1,5), "medicao": 15923, "litros": 270}
]

for i in range(5): # for (int i=0; i<=5; i++) {} ou for (element : elements ){}
    medicao = medicoes[i]

c12400 = [m for m in medicoes if m['caminhao']=='12400']

print("Data"+" "*6, "Caminhão", "Medição", "Litros", "KM  ", "Consumo")
for i,medicao in enumerate(c12400):
    consumo = 0
    km = 0
    if i>0:
        km = medicao["medicao"]-c12400[i-1]["medicao"]
        consumo = km/medicao['litros']

    print( medicao['data'], medicao["caminhao"]+" "*3, str(medicao["medicao"])+" "*2, str(medicao["litros"])+" "*3, km, consumo )