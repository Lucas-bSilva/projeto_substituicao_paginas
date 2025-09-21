"""
Algoritmos de substituição de páginas (FIFO, Ótimo/OTM, LRU).

Cada função recebe:
- references: lista de inteiros representando a sequência de referências a páginas;
- frames: inteiro com a quantidade de quadros disponíveis;

Retorna:
- int: número total de faltas de página.
"""

from collections import deque
from typing import List


# ==============================
# Algoritmo FIFO (First-In First-Out)
# ==============================
def fifo_faults(references: List[int], frames: int) -> int:
    """
    Implementa o algoritmo de substituição de páginas FIFO.
    A página mais antiga na memória (a que entrou primeiro) é a primeira a sair.
    """
    if frames <= 0:  # Caso não haja quadros disponíveis
        return 0

    faltas = 0                   # Contador de faltas de página
    memoria = set()              # Conjunto com as páginas atualmente na memória
    fila = deque()               # Fila que mantém a ordem de chegada das páginas

    for p in references:         # Percorre a sequência de referências
        if p in memoria:
            # HIT: página já está na memória, nada é feito
            continue

        # MISS: página não está na memória
        faltas += 1
        if len(memoria) < frames:
            # Ainda há espaço livre na memória, apenas adiciona
            memoria.add(p)
            fila.append(p)
        else:
            # Memória cheia: remove a mais antiga (primeiro da fila)
            sair = fila.popleft()
            memoria.remove(sair)

            # Adiciona a nova página
            memoria.add(p)
            fila.append(p)

    return faltas


# ==============================
# Algoritmo ÓTIMO (Optimal - OTM)
# ==============================
def otm_faults(references: List[int], frames: int) -> int:
    """
    Algoritmo Ótimo (Optimal / OTM).
    Remove a página cujo próximo uso está mais distante no futuro.
    Se uma página nunca mais for usada, ela é escolhida como vítima.
    """
    if frames <= 0:
        return 0

    faltas = 0
    memoria: List[int] = []      # Representa os quadros como lista de páginas
    n = len(references)          # Tamanho da sequência de referências

    for i, p in enumerate(references):
        if p in memoria:
            # HIT: página já está na memória
            continue

        # MISS: página não está na memória
        faltas += 1
        if len(memoria) < frames:
            # Se houver espaço, apenas adiciona a página
            memoria.append(p)
            continue

        # Escolher a página vítima
        # Critério: próxima utilização mais distante (ou nunca usada)
        idx_mais_distante = -1
        pagina_vitima = None

        for q in memoria:
            try:
                # Procura a próxima vez que q será usada
                proximo_uso = references.index(q, i + 1)
            except ValueError:
                # Página q nunca mais será usada → melhor escolha
                pagina_vitima = q
                break
            # Atualiza se esta página será usada mais distante que a atual candidata
            if proximo_uso > idx_mais_distante:
                idx_mais_distante = proximo_uso
                pagina_vitima = q

        # Substitui a vítima pela nova página
        pos = memoria.index(pagina_vitima)
        memoria[pos] = p

    return faltas


# ==============================
# Algoritmo LRU (Least Recently Used)
# ==============================
def lru_faults(references: List[int], frames: int) -> int:
    """
    Implementa o algoritmo LRU.
    Remove a página menos recentemente usada (a que ficou mais tempo sem ser acessada).
    """
    if frames <= 0:
        return 0

    faltas = 0
    memoria: List[int] = []        # Lista das páginas atualmente na memória
    ultimo_uso = {}                # Dicionário: página -> último índice de acesso

    for i, p in enumerate(references):
        if p in memoria:
            # HIT: atualiza o último acesso da página
            ultimo_uso[p] = i
            continue

        # MISS: página não está na memória
        faltas += 1
        if len(memoria) < frames:
            # Se ainda há espaço, insere diretamente
            memoria.append(p)
            ultimo_uso[p] = i
        else:
            # Memória cheia → escolher a vítima (página com menor índice de último uso)
            vitima = min(memoria, key=lambda x: ultimo_uso.get(x, -1))
            pos = memoria.index(vitima)

            # Substitui a vítima pela nova página
            memoria[pos] = p
            ultimo_uso[p] = i  # Atualiza o tempo de uso da nova página

            # Obs: não é obrigatório remover a vítima do dicionário,
            # pois ela não estará mais em 'memoria'.

    return faltas
