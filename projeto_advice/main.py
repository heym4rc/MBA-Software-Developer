import requests
from deep_translator import GoogleTranslator
from datetime import datetime

# --- Constantes e Objetos Globais ---
# Definir constantes e objetos fora das funções melhora a organização e a performance,
# pois não são recriadas a cada chamada.
API_URL = 'https://api.adviceslip.com/advice'
TRANSLATOR = GoogleTranslator(source='auto', target='pt')

def buscar_conselho_traduzido():
    """Busca um conselho na API, traduz e retorna a frase."""
    try:
        response = requests.get(API_URL)
        # Lança uma exceção HTTPError para respostas de erro (4xx ou 5xx)
        response.raise_for_status()

        # Converte a resposta JSON para um dicionário Python
        dados = response.json()

        # Extrai o conselho em inglês
        conselho_em_ingles = dados['slip']['advice']

        # Traduz o texto para o idioma de destino
        traducao = TRANSLATOR.translate(conselho_em_ingles)

        return traducao
    except requests.exceptions.RequestException as e:
        return f"Erro de conexão: {e}"
    except KeyError:
        return "Erro: Formato de resposta inesperado da API."
    except Exception as e:
        return f"Erro durante a tradução: {e}"

if __name__ == "__main__":
    conselho = buscar_conselho_traduzido()
    print(conselho)

    # Salvar o conselho em um arquivo de texto, somente se não for um erro.
    if conselho and not conselho.startswith("Erro"):
        try:
            # Obtém a data e hora atuais para adicionar ao arquivo
            timestamp = datetime.now().strftime('%M-%d')

            with open('conselho.txt', 'a', encoding='utf-8') as arquivo:
                # Escreve a data, seguida pelo conselho
                arquivo.write(f"[{timestamp}] {conselho}\n")
            print("\nConselho salvo com sucesso em conselho.txt")
        except Exception as e:
            print(f"Erro ao salvar o conselho no arquivo: {e}")