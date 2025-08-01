import os

class FileVerify:
    def __init__(self):
        self.alunos = {}
        # self.path: str = input("Qual diretorio? ")
        self.path = "terceiroano/lista01"
        self.extract()        
    
    def get_files_dir(self):
        # lista de arquivos
        arquivos = os.listdir(os.path.join(os.getcwd(), self.path))
        arquivos = [file for file in arquivos if file.endswith('.html')]
        print(f"Arquivos no diretorio raiz: \n{arquivos}")
        return arquivos

    def get_file_content(self, filename):
        with open(os.path.join(os.getcwd(), self.path, filename), 'r') as file:
            print(f"Abrindo arquivo {filename}")
            trimstr = file.read().replace(" ", "").replace("\n", "")
            # verificar tags html
            tags = ('<header>', '<nav>', '<main>', '<section>', '<articule>', '<aside>', '<footer>', '<figure>', '<figcaption>', '<ul>')
            for t in tags:
                if t not in trimstr:
                    print(f"O arquivo {filename} não possui a tag {t}")
            return trimstr

    def add_content(self, filename, content):
        if filename not in self.alunos.keys():
            self.alunos[filename] = content

    def extract(self):
        for f in self.get_files_dir():
            self.add_content(f, self.get_file_content(f))

    def check(self, chave, valor):
        iguais = []
        for k, v in self.alunos.items():
            if len(v) == len(valor):
                iguais.append(k)
        return iguais
    
    def save_file(self, copias:str):
        with open('copias.txt', 'w', encoding="UTF-8") as file:
            import json
            file.write(json.dumps(copias))

    def verify(self):
        iguais = []
        # Tente usar recursão
        for k,v in self.alunos.items():
            # quando percorre a lista precisa remover caso tenha encontrado cópia
            i = self.check(k, v)
            if len(i)>0:
                iguais.append(tuple(set(i)))
        print(f"Arquivos iguais encontrados: {iguais}")
        self.save_file(iguais)
        

if __name__== "__main__":
    fileVerify = FileVerify()
    fileVerify.verify()
    a = list(fileVerify.alunos.keys())
    
    def contar(num, lista, alunos):
        def remove_duplicados():
            pass
        """
            num: indice
            lista: lista de chaves
            alunos: dicionário de alunos

            Percorre recursivamente os alunos e identifica cópias de arquivos.
        """
        duplicados = fileVerify.check(lista[num], alunos) or []# verifica cópias
        # se encontrar uma cópia precisa remover os sucessores na lista
        for d in duplicados:
            del alunos[d]

        if num < len(lista)-1:
            return contar(num+1, lista, alunos)
        
    contar(0, a, fileVerify.alunos)