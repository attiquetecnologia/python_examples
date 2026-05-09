"""
Arquivo de funcções especiais
Autor: Rodrigo Attique
Email: rodrigoatique@gmail.com
"""

# Padrão de escrita snake-case
def formata_cpf(cpf: str):
    """
    cpf: Recebe um cpf e devolve formatado
        XXXXXXXXXXX
    return: XXX.XXX.XXX-XX
    """
    return f"{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}"

if __name__ == "__main__":
    print(formata_cpf("10910810784"))