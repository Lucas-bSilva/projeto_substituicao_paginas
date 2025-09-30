"""
Algoritmos de substituição de páginas: FIFO, ÓTIMO (OTM) e LRU.

Cada função recebe:
- referencias (List[int]): sequência de referências a páginas.
- quadros (int): quantidade de quadros (espaços de memória disponíveis).

Retorna:
- int: número total de faltas de página (page faults).
"""

from collections import deque   # Importa deque (fila dupla) para gerenciar ordem de chegada no FIFO
from typing import List         # Importa List para anotações de tipo


# ============================================================
# Algoritmo FIFO (First-In First-Out)
# ============================================================
def fifo_faltas(referencias: List[int], quadros: int) -> int:
    if quadros <= 0:                     # Se o número de quadros for zero ou negativo
        return 0                         # Não há como armazenar páginas → retorna 0

    faltas = 0                           # Contador de faltas de página começa em 0
    memoria = set()                      # Conjunto que guarda as páginas atualmente carregadas
    fila = deque()                       # Fila para controlar a ordem em que as páginas entraram

    for pagina in referencias:           # Percorre cada referência de página na sequência
        if pagina in memoria:            # Verifica se a página já está na memória
            continue                     # Se já estiver, segue sem registrar falta

        faltas += 1                      # Caso contrário, conta uma falta de página
        if len(memoria) < quadros:       # Se ainda houver espaço disponível nos quadros
            memoria.add(pagina)          # Adiciona a nova página ao conjunto
            fila.append(pagina)          # Coloca a página na fila de chegada
        else:                            # Se a memória já estiver cheia
            sair = fila.popleft()        # Remove a página mais antiga (primeira da fila)
            memoria.remove(sair)         # Remove essa página também do conjunto
            memoria.add(pagina)          # Adiciona a nova página
            fila.append(pagina)          # E coloca a nova página no final da fila

    return faltas                        # Retorna o total de faltas encontradas


# ============================================================
# Algoritmo ÓTIMO (Optimal / OTM)
# ============================================================
def otm_faltas(referencias: List[int], quadros: int) -> int:
    if quadros <= 0:                     # Se não há quadros disponíveis
        return 0                         # Não há como armazenar páginas → retorna 0

    faltas = 0                           # Contador de faltas de página
    memoria: List[int] = []              # Lista que representa as páginas atualmente na memória

    for i, pagina in enumerate(referencias):   # Percorre cada referência com índice i
        if pagina in memoria:                  # Se a página já estiver na memória
            continue                           # Nada é feito (não ocorre falta)

        faltas += 1                            # Página não encontrada → conta uma falta
        if len(memoria) < quadros:             # Se ainda houver espaço disponível
            memoria.append(pagina)             # Adiciona a página diretamente à memória
            continue                           # Vai para a próxima referência

        indice_mais_distante = -1              # Guarda o índice do uso mais distante encontrado
        pagina_vitima = None                   # Página candidata à remoção começa vazia

        for atual in memoria:                  # Percorre cada página atualmente na memória
            try:
                proximo_uso = referencias.index(atual, i + 1)  # Procura quando será usada de novo
            except ValueError:                 # Se a página não aparecer mais
                pagina_vitima = atual          # Ela será a escolhida para remoção
                break                          # Encerra o laço, pois já achou a vítima ideal

            if proximo_uso > indice_mais_distante:   # Se o uso dessa página está mais distante
                indice_mais_distante = proximo_uso   # Atualiza o índice mais distante
                pagina_vitima = atual                # Define essa página como candidata

        pos = memoria.index(pagina_vitima)    # Descobre a posição da página vítima na memória
        memoria[pos] = pagina                 # Substitui pela nova página

    return faltas                             # Retorna o total de faltas encontradas


# ============================================================
# Algoritmo LRU (Least Recently Used)
# ============================================================
def lru_faltas(referencias: List[int], quadros: int) -> int:
    if quadros <= 0:                          # Se não há quadros disponíveis
        return 0                              # Não há como armazenar páginas → retorna 0

    faltas = 0                                # Contador de faltas
    memoria: List[int] = []                   # Lista de páginas carregadas
    ultimo_uso = {}                           # Dicionário que registra o último índice de uso de cada página

    for i, pagina in enumerate(referencias):  # Percorre cada referência com índice i
        if pagina in memoria:                 # Se a página já está na memória
            ultimo_uso[pagina] = i            # Atualiza o índice de último uso
            continue                          # Segue para a próxima referência

        faltas += 1                           # Página não encontrada → conta uma falta
        if len(memoria) < quadros:            # Se ainda houver espaço disponível
            memoria.append(pagina)            # Adiciona a página à memória
            ultimo_uso[pagina] = i            # Registra o índice de uso dessa página
        else:                                 # Se a memória já estiver cheia
            vitima = min(memoria, key=lambda x: ultimo_uso.get(x, -1))  # Acha a menos recentemente usada
            pos = memoria.index(vitima)       # Descobre a posição da vítima na lista
            memoria[pos] = pagina             # Substitui a vítima pela nova página
            ultimo_uso[pagina] = i            # Atualiza o último uso da nova página

    return faltas                             # Retorna o total de faltas encontradas
