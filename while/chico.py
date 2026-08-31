def main():
    juca = 1.10
    chico = 1.50
    ano = 0

    while juca < chico:
        juca = juca + 0.03
        chico = chico + 0.02
        ano = ano + 1

    print("Serão necessários", ano, "anos para que Juca seja maior que Chico.")

if __name__ == "__main__":
    main()
