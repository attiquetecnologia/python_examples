
# Exemplo 01
# Receba a previsão do tempo do usuário (chuva, sol, nublado) 
# se ele digitar algo diferente exiba a mensagem 
# “opção inválida”, se chuva exiba a mensagem 
# “use guarda chuvas”, se sol “não esqueça o filtro solar” 
# se nublado “O tempo está ótimo”.
tempo = input("Digite a previsão do tempo (chuva, sol, nublado): ")
match tempo:
    case "chuva":
        print("Use guarda chuvas.")
    case "sol":
        print("Não esqueça o filtro solar.")
    case "nublado":
        print("O tempo está ótimo.")
    case _:
        print("Opção inválida.")

# Exemplo 02
# Crie um programa que receba do usuário a sigla de um 
# estado do brasil e imprima o nome completo do estado 
# ou sigla inválida.
estado = input("Digite a sigla de um estado do Brasil: ")
match estado:
    case "AC":
        print("Acre")
    case "AL":
        print("Alagoas")
    case "AP":
        print("Amapá")
    case "AM":
        print("Amazonas")
    case "BA":
        print("Bahia")
    case "CE":
        print("Ceará")
    case "DF":
        print("Distrito Federal")
    case "ES":
        print("Espírito Santo")
    case "GO":
        print("Goiás")
    case "MA":
        print("Maranhão")
    case "MT":
        print("Mato Grosso")
    case "MS":
        print("Mato Grosso do Sul")
    case "MG":
        print("Minas Gerais")
    case "PA":
        print("Pará")
    case "PB":
        print("Paraíba")
    case "PR":
        print("Paraná")
    case "PE":
        print("Pernambuco")
    case "PI":
        print("Piauí")
    case "RJ":
        print("Rio de Janeiro")
    case "RN":
        print("Rio Grande do Norte")
    case "RS":
        print("Rio Grande do Sul")
    case "RO":
        print("Rondônia")
    case "RR":
        print("Roraima")
    case "SC":
        print("Santa Catarina")
    case "SP":
        print("São Paulo")
    case "SE":
        print("Sergipe")
    case "TO":
        print("Tocantins")
    case _:
        print("Sigla inválida.")