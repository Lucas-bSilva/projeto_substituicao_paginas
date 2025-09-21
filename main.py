"""
Responsável por:
- Validar argumentos da linha de comando;
- Ler o arquivo de entrada no formato esperado;
- Executar os três algoritmos de substituição de páginas (FIFO, OTM, LRU);
- Exibir os resultados na saída padrão.
"""

import sys
from algorithms import fifo_faults, otm_faults, lru_faults   # Importa os algoritmos implementados
from io_utils import carregar_entrada                       # Função para carregar e validar a entrada


def main(argv):
    """
    Função principal do programa.

    Parâmetros:
    - argv (list): lista de argumentos passados pela linha de comando (sys.argv).

    Retorna:
    - int: código de saída do programa.
        * 0 → execução bem-sucedida
        * 1 → erro ao ler/validar arquivo de entrada
        * 2 → erro de uso (argumentos inválidos)
    """
    # Verifica se a quantidade de argumentos está correta
    if len(argv) != 2:
        sys.stderr.write("Uso: python main.py <arquivo_de_entrada>\n")
        return 2  # Erro de uso (parâmetros incorretos)

    caminho = argv[1]  # Caminho do arquivo de entrada fornecido pelo usuário

    try:
        # Lê os dados do arquivo de entrada
        # Retorna:
        # - frames: número de quadros disponíveis
        # - referencias: sequência de referências a páginas
        frames, referencias = carregar_entrada(caminho)
    except Exception as e:
        # Caso ocorra erro na leitura ou formatação do arquivo,
        # imprime mensagem no stderr (não interfere na saída padrão)
        sys.stderr.write(str(e) + "\n")
        return 1  # Erro na leitura da entrada

    # =============================
    # Execução dos algoritmos
    # =============================
    fifo = fifo_faults(referencias, frames)   # Algoritmo FIFO (First-In, First-Out)
    otm  = otm_faults(referencias, frames)    # Algoritmo Ótimo (Optimal Page Replacement)
    lru  = lru_faults(referencias, frames)    # Algoritmo LRU (Least Recently Used)

    # =============================
    # Impressão dos resultados
    # =============================
    # O formato de saída é estritamente definido:
    # <NOME_ALGORITMO> <NÚMERO_DE_FALTAS>
    print(f"FIFO {fifo}")
    print(f"OTM {otm}")
    print(f"LRU {lru}")

    return 0  # Execução concluída com sucesso


# =============================
# Ponto de entrada do programa
# =============================
if __name__ == "__main__":
    # O raise SystemExit garante que o código de saída retornado por main()
    # seja repassado ao sistema operacional.
    raise SystemExit(main(sys.argv))
