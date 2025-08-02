import hashlib
import time

# --- Classe Bloco ---
class Block:
    def __init__(self, index, transactions, timestamp, previous_hash, nonce=0):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = nonce # Número usado para a Prova de Trabalho
        self.hash = self.calculate_hash() # Hash do bloco atual

    def calculate_hash(self):
        # Calcula o hash SHA256 do bloco
        block_string = f"{self.index}{self.transactions}{self.timestamp}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def __str__(self):
        return (f"Bloco #{self.index}\n"
                f"Timestamp: {self.timestamp}\n"
                f"Transações: {self.transactions}\n"
                f"Hash Anterior: {self.previous_hash}\n"
                f"Nonce: {self.nonce}\n"
                f"Hash: {self.hash}\n")

# --- Classe Blockchain ---
class Blockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.difficulty = 2 # Quantos zeros o hash deve começar (para Prova de Trabalho)
        self.create_genesis_block() # Cria o primeiro bloco

    def create_genesis_block(self):
        # O bloco gênese é o primeiro bloco da cadeia, sem hash anterior.
        genesis_block = Block(0, "Bloco Gênese", time.time(), "0")
        self.chain.append(genesis_block)
        print("Bloco Gênese criado!")

    def get_last_block(self):
        return self.chain[-1]

    def add_transaction(self, sender, recipient, amount):
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        }
        self.pending_transactions.append(transaction)
        print(f"Transação adicionada: {sender} -> {recipient}: {amount}")

    def proof_of_work(self, block):
        # A prova de trabalho: encontrar um nonce que faça o hash começar com 'difficulty' zeros
        target_prefix = '0' * self.difficulty
        while block.hash[:self.difficulty] != target_prefix:
            block.nonce += 1
            block.hash = block.calculate_hash()
        return block.hash

    def mine_pending_transactions(self):
        if not self.pending_transactions:
            print("Nenhuma transação pendente para minerar.")
            return False

        last_block = self.get_last_block()
        new_block_index = last_block.index + 1
        current_time = time.time()
        
        # Cria um novo bloco com as transações pendentes
        new_block = Block(new_block_index, 
                          self.pending_transactions.copy(), # Copia as transações
                          current_time, 
                          last_block.hash)

        print(f"\nMinerando Bloco #{new_block_index}...")
        mined_hash = self.proof_of_work(new_block)
        
        new_block.hash = mined_hash # Atualiza o hash do bloco com o encontrado pela PoW
        self.chain.append(new_block)
        self.pending_transactions = [] # Limpa as transações pendentes

        print(f"Bloco #{new_block_index} minerado com sucesso! Hash: {new_block.hash}")
        print("Transações pendentes limpas.")
        return True

    def is_chain_valid(self):
        # Verifica se a cadeia é válida (hashes e links estão corretos)
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            # 1. Verifica se o hash do bloco atual é válido
            if current_block.hash != current_block.calculate_hash():
                print(f"Erro: Hash inválido no Bloco #{current_block.index}")
                return False

            # 2. Verifica se o hash anterior aponta para o bloco correto
            if current_block.previous_hash != previous_block.hash:
                print(f"Erro: Link de hash inválido entre Bloco #{previous_block.index} e Bloco #{current_block.index}")
                return False

            # 3. Verifica a prova de trabalho (se o hash corresponde à dificuldade)
            target_prefix = '0' * self.difficulty
            if current_block.hash[:self.difficulty] != target_prefix:
                print(f"Erro: Prova de trabalho inválida no Bloco #{current_block.index}")
                return False

        return True

# --- Exemplo de Uso ---
if __name__ == "__main__":
    my_blockchain = Blockchain()

    # Adicionando algumas transações
    my_blockchain.add_transaction("Alice", "Bob", 10)
    my_blockchain.add_transaction("Bob", "Carol", 5)

    # Minerando o primeiro bloco de transações
    my_blockchain.mine_pending_transactions()

    # Adicionando mais transações
    my_blockchain.add_transaction("Carol", "David", 2)
    my_blockchain.add_transaction("David", "Alice", 3)

    # Minerando o segundo bloco de transações
    my_blockchain.mine_pending_transactions()

    print("\n--- Blockchain Atual ---")
    for block in my_blockchain.chain:
        print(block)
        print("-" * 30)

    # Verificando a validade da cadeia
    print("\nVerificando a validade da cadeia...")
    if my_blockchain.is_chain_valid():
        print("A blockchain é válida!")
    else:
        print("A blockchain é inválida!")

    # Exemplo de como uma alteração invalidaria a cadeia
    print("\n--- Tentando manipular o Bloco #1 ---")
    # ATENÇÃO: Nunca faça isso em uma blockchain real!
    # Apenas para fins de demonstração.
    try:
        my_blockchain.chain[1].transactions = "Transação Falsificada!"
        my_blockchain.chain[1].hash = my_blockchain.chain[1].calculate_hash() # Recalcula o hash do bloco alterado
        print("Transação do Bloco #1 alterada (para demonstração).")

        print("\nVerificando a validade da cadeia após a alteração...")
        if my_blockchain.is_chain_valid():
            print("A blockchain é válida! (Isso não deveria acontecer se a segurança funcionasse)")
        else:
            print("A blockchain é inválida! (Correto, a manipulação foi detectada!)")
    except IndexError:
        print("Não há blocos suficientes para demonstrar a alteração.")