# Projeto - Simulação de Algoritmos de Substituição de Páginas

##  Descrição
Este projeto foi desenvolvido para a disciplina **Sistemas Operacionais I (UFPB)** e implementa uma simulação dos **principais algoritmos de substituição de páginas** estudados em sala:

- **FIFO** (First-In, First-Out)  
- **OTM** (Ótimo / Optimal)  
- **LRU** (Least Recently Used ou Menos Recentemente Utilizado)  

O objetivo é calcular o número de **faltas de página** para cada algoritmo, dado um arquivo de entrada contendo:  
1. A quantidade de **quadros de memória disponíveis**.  
2. A **sequência de referências às páginas** (um inteiro por linha).  

A saída deve respeitar exatamente o formato definido no enunciado do projeto.

---

##  Estrutura do Projeto

```
.
├── algorithms.py   # Implementações dos algoritmos FIFO, OTM e LRU
├── io_utils.py     # Funções utilitárias para leitura e validação da entrada
├── main.py         # Arquivo principal que integra e executa os algoritmos
├── caso_teste_1.txt
├── caso_teste_2.txt
├── caso_teste_3.txt
└── README.md       # Documentação do projeto
```

---

##  Execução

O programa deve ser executado via **linha de comando**.  
Uso geral:

```bash
python main.py <arquivo_de_entrada>
```

- `<arquivo_de_entrada>` deve conter os dados no formato especificado:  
  - Primeira linha: número de quadros (frames).  
  - Linhas seguintes: sequência de referências às páginas.  

 ## Comandos prontos para execução

Para rodar os casos de teste fornecidos no projeto, utilize os seguintes comandos:

python main.py caso_teste_1.txt
python main.py caso_teste_2.txt
python main.py caso_teste_3.txt  

###  Exemplos

#### Exemplo 1 — caso_teste_1.txt
```bash
python main.py caso_teste_1.txt
```

Saída esperada:
```
FIFO 8
OTM 6
LRU 7
```

#### Exemplo 2 — caso_teste_2.txt
```bash
python main.py caso_teste_2.txt
```

Saída esperada:
```
FIFO 9
OTM 8
LRU 10
```

#### Exemplo 3 — caso_teste_3.txt
```bash
python main.py caso_teste_3.txt
```

Saída esperada:
```
FIFO 6
OTM 6
LRU 6
```

---

##  Especificação da Entrada e Saída

- **Entrada**:  
  Arquivo texto (`.txt`) contendo números inteiros, um por linha.  
  - O **primeiro número** representa a quantidade de quadros de memória disponíveis.  
  - Os **demais números** representam a sequência de referências às páginas.  

- **Saída**:  
  Linhas no formato estritamente definido:  

  ```
  FIFO X
  OTM Y
  LRU Z
  ```

  Onde `X`, `Y` e `Z` são os números de faltas de página para cada algoritmo.  

⚠️ **Atenção**: Qualquer caractere extra ou saída fora desse formato será considerado **incorreto**.

---

##  Tecnologias
- **Linguagem**: Python 3  
- **Bibliotecas utilizadas**:  
  - `collections.deque` (suporte à fila do FIFO)  
  - `typing` (anotações de tipo)  
  - `sys` (entrada e argumentos de linha de comando)  
  
