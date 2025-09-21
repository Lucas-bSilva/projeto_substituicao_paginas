"""
Utilidades de Entrada/Saída (E/S) para leitura do arquivo de entrada
no formato exigido pelo simulador de substituição de páginas.

Formato esperado do arquivo:
- Primeira linha: número de quadros (frames) disponíveis na memória.
- Demais linhas: sequência de referências a páginas (um inteiro por linha).
"""

from typing import List, Tuple, TextIO
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
    valores = []
    for linha in f:
        s = linha.strip()  # remove espaços em branco e quebras de linha
        if s == "":
            # Ignora linhas em branco
            continue
        try:
            valores.append(int(s))  # converte para inteiro e adiciona
        except ValueError:
            # Se a conversão falhar, lança erro explicando o problema
            raise ValueError(
                f"Linha inválida no arquivo de entrada: '{linha.strip()}' (não é inteiro)"
            )
    return valores


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
        # Lê dados da entrada padrão (útil para redirecionamento via terminal)
        valores = _ler_inteiros(sys.stdin)
    else:
        # Abre o arquivo e lê os valores
        with open(caminho, 'r', encoding='utf-8') as f:
            valores = _ler_inteiros(f)

    if not valores:
        # Se não houver nenhum número no arquivo, é inválido
        raise ValueError("Arquivo de entrada vazio.")

    frames = valores[0]       # Primeiro valor = quantidade de quadros
    referencias = valores[1:] # Demais valores = sequência de referências

    return frames, referencias
