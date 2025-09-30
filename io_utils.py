"""
Utilidades de Entrada/Saída (E/S) para leitura do arquivo de entrada
no formato exigido pelo simulador de substituição de páginas.

Formato esperado do arquivo:
- Primeira linha: número de quadros (frames) disponíveis na memória.
- Demais linhas: sequência de referências a páginas (um inteiro por linha).
"""

# Importa tipos de anotações para melhor legibilidade (List, Tuple, TextIO)
from typing import List, Tuple, TextIO

# Importa módulo sys para conseguir acessar a entrada padrão (stdin)
import sys


def _ler_inteiros(f: TextIO) -> List[int]:
    """
    Lê todas as linhas de um arquivo (ou stdin) e converte em uma lista de inteiros.

    Parâmetros:
    - f (TextIO): arquivo de texto aberto ou entrada padrão (stdin).

    Retorna:
    - List[int]: lista com os valores inteiros lidos.

    Exceções:
    - ValueError: se alguma linha não for um inteiro válido.
    """
    valores = []  # Cria uma lista vazia para armazenar os números lidos

    # Percorre cada linha do arquivo de entrada
    for linha in f:
        s = linha.strip()  # Remove espaços em branco e quebras de linha
        if s == "":
            # Se a linha estiver em branco, simplesmente ignora
            continue
        try:
            valores.append(int(s))  # Converte a string para inteiro e adiciona à lista
        except ValueError:
            # Se a conversão falhar, lança um erro indicando a linha inválida
            raise ValueError(
                f"Linha inválida no arquivo de entrada: '{linha.strip()}' (não é inteiro)"
            )
    return valores  # Retorna a lista de números inteiros lidos


def carregar_entrada(caminho: str) -> Tuple[int, List[int]]:
    """
    Lê os dados de entrada a partir de um arquivo ou stdin.

    Parâmetros:
    - caminho (str): caminho do arquivo de entrada.
      Se for '-', os dados serão lidos da entrada padrão (stdin).

    Retorna:
    - Tuple[int, List[int]]:
        * frames: número de quadros disponíveis na memória (primeiro valor do arquivo).
        * referencias: sequência de referências a páginas (restante do arquivo).
    
    Exceções:
    - ValueError: se o arquivo estiver vazio ou mal formatado.
    """
    if caminho == '-':
        # Caso o caminho seja '-', lê os dados diretamente da entrada padrão (stdin)
        valores = _ler_inteiros(sys.stdin)
    else:
        # Caso contrário, abre o arquivo informado e lê os números
        with open(caminho, 'r', encoding='utf-8') as f:
            valores = _ler_inteiros(f)

    if not valores:
        # Se a lista de valores estiver vazia, significa que o arquivo não tem dados válidos
        raise ValueError("Arquivo de entrada vazio.")

    frames = valores[0]        # O primeiro número do arquivo é a quantidade de quadros
    referencias = valores[1:]  # Os demais números representam as referências de páginas

    # Retorna uma tupla contendo a quantidade de quadros e a lista de referências
    return frames, referencias
