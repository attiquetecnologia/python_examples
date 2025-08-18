import requests
from bs4 import BeautifulSoup

def consultar_processo_tjsp(url):
    """
    Consulta a página do processo judicial no TJSP e extrai as movimentações.
    
    Args:
        url (str): A URL do processo a ser consultado.
    
    Returns:
        list: Uma lista de tuplas contendo (data, movimentacao), ou uma string de erro.
    """
    
    # Adicionar um User-Agent para simular um navegador real
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        # Fazer a requisição HTTP com um timeout para evitar que o script trave
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Levanta um erro para códigos de status HTTP 4xx/5xx
        
        # Analisar o conteúdo HTML da página
        soup = BeautifulSoup(response.text, 'html.parser')
        
        movimentacoes = []
        
        # Encontrar a tabela que contém as movimentações
        tabela_movimentacoes = soup.find('div', id='tabelaMovimentacoes')
        
        if tabela_movimentacoes:
            # Encontrar todas as linhas (tr) da tabela de movimentações
            linhas = tabela_movimentacoes.find_all('tr', class_='fundocinza1')
            
            for linha in linhas:
                # Extrair a data da primeira célula (td)
                data_tag = linha.find('td', width='140', style='text-align:left')
                data = data_tag.get_text(strip=True) if data_tag else "Data não encontrada"
                
                # Extrair a movimentação da segunda célula (td)
                movimentacao_tag = linha.find('td', width='*', class_='mensagem')
                movimentacao = movimentacao_tag.get_text(strip=True) if movimentacao_tag else "Movimentação não encontrada"
                
                movimentacoes.append((data, movimentacao))
        else:
            return "Não foi possível encontrar a tabela de movimentações. O layout da página pode ter mudado ou a página não contém essa seção."

        return movimentacoes
        
    except requests.exceptions.HTTPError as err_http:
        return f"Erro HTTP: {err_http}"
    except requests.exceptions.ConnectionError as err_conn:
        return f"Erro de Conexão: {err_conn}"
    except requests.exceptions.Timeout as err_timeout:
        return f"Tempo de espera esgotado: {err_timeout}"
    except requests.exceptions.RequestException as err:
        return f"Ocorreu um erro: {err}"
    except Exception as e:
        return f"Um erro inesperado ocorreu: {e}"

# Exemplo de uso
url_processo = "https://esaj.tjsp.jus.br/cpopg/show.do?processo.codigo=1U00089A10000&processo.foro=66&processo.numero={processo}"
resultado = consultar_processo_tjsp(url_processo)

if isinstance(resultado, list):
    for data, movimentacao in resultado:
        print(f"Data: {data}\nMovimentação: {movimentacao}\n")
else:
    print(resultado)