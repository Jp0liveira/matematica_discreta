
"""
Atividade de Recorrência - Torres de Hanói
Aluno: João Paulo Oliveira
UFPA - Prof. Dr. Renato Hidaka

COMO EXECUTAR:
1. Instale o Python 3 (https://python.org)
2. No terminal, instale o matplotlib:
       pip install matplotlib
3. Execute:
       python torres_hanoi.py

Os gráficos serão salvos como imagens PNG na mesma pasta.
"""

import matplotlib.pyplot as plt

# =============================================================================
# VARIÁVEL GLOBAL - Contador de linhas executadas
# =============================================================================
line_counter = 0


# =============================================================================
# FUNÇÃO RECURSIVA - Torres de Hanói
# =============================================================================
def torres_de_hanoi(n, origem, destino, auxiliar, movimentos=None):
    """
    Resolve o problema das Torres de Hanói recursivamente.

    Parâmetros:
        n (int): Número de discos a serem movidos.
        origem (str): Pino de origem.
        destino (str): Pino de destino.
        auxiliar (str): Pino auxiliar.
        movimentos (list): Lista opcional para registrar os movimentos.
    """
    global line_counter

    line_counter += 1  # Linha 1: verificação do caso base

    # Caso base: apenas 1 disco
    if n == 1:
        line_counter += 1  # Linha 2: movimento direto
        if movimentos is not None:
            movimentos.append(f"Mover disco 1 de {origem} para {destino}")
        return

    # Passo 1: mover n-1 discos da origem para o auxiliar
    line_counter += 1  # Linha 3: chamada recursiva 1
    torres_de_hanoi(n - 1, origem, auxiliar, destino, movimentos)

    # Passo 2: mover o disco n da origem para o destino
    line_counter += 1  # Linha 4: movimento do disco maior
    if movimentos is not None:
        movimentos.append(f"Mover disco {n} de {origem} para {destino}")

    # Passo 3: mover n-1 discos do auxiliar para o destino
    line_counter += 1  # Linha 5: chamada recursiva 2
    torres_de_hanoi(n - 1, auxiliar, destino, origem, movimentos)


# =============================================================================
# FUNÇÃO DE MEDIÇÃO
# =============================================================================
def medir_desempenho(n):
    """
    Mede quantas linhas são executadas para n discos.

    Parâmetros:
        n (int): Número de discos.

    Retorna:
        int: Total de linhas executadas.
    """
    global line_counter
    line_counter = 0
    torres_de_hanoi(n, 'A', 'C', 'B')
    return line_counter


# =============================================================================
# DEMONSTRAÇÃO COM POUCOS DISCOS
# =============================================================================
def demonstracao():
    """Mostra os movimentos para 3 discos como exemplo."""
    print("=" * 50)
    print("DEMONSTRAÇÃO: Torres de Hanói com 3 discos")
    print("=" * 50)
    movimentos = []
    global line_counter
    line_counter = 0
    torres_de_hanoi(3, 'A', 'C', 'B', movimentos)
    for i, mov in enumerate(movimentos, 1):
        print(f"  Passo {i}: {mov}")
    print(f"\nTotal de movimentos: {len(movimentos)}")
    print(f"Total de linhas executadas: {line_counter}")
    print()


# =============================================================================
# BATERIA DE TESTES
# =============================================================================
def executar_testes():
    """Executa testes de n=1 até n=20 e retorna os resultados."""
    valores_n = list(range(1, 21))
    linhas_executadas = []
    movimentos = []

    print("=" * 60)
    print(f"{'n':>4} | {'Linhas Executadas':>20} | {'Movimentos (2^n - 1)':>20}")
    print("-" * 60)

    for n in valores_n:
        linhas = medir_desempenho(n)
        mov = 2**n - 1
        linhas_executadas.append(linhas)
        movimentos.append(mov)
        print(f"{n:>4} | {linhas:>20,} | {mov:>20,}")

    print("=" * 60)
    return valores_n, linhas_executadas, movimentos


# =============================================================================
# GERAÇÃO DOS GRÁFICOS
# =============================================================================
def gerar_graficos(valores_n, linhas_executadas, movimentos):
    """Gera e salva os gráficos de desempenho."""

    teorico = [5 * (2**n - 1) for n in valores_n]

    # ----- GRÁFICO 1: Escala Linear + Logarítmica lado a lado -----
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Escala linear
    ax1.plot(valores_n, linhas_executadas, 'o-', color='#2563EB',
             linewidth=2, markersize=6, label='Linhas executadas (medido)')
    ax1.plot(valores_n, teorico, 's--', color='#DC2626',
             linewidth=1.5, markersize=4, alpha=0.7, label='5 × (2ⁿ − 1) teórico')
    ax1.set_xlabel('Número de discos (n)', fontsize=12)
    ax1.set_ylabel('Linhas executadas', fontsize=12)
    ax1.set_title('Desempenho - Escala Linear', fontsize=14, fontweight='bold')
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3)

    # Escala logarítmica
    ax2.plot(valores_n, linhas_executadas, 'o-', color='#2563EB',
             linewidth=2, markersize=6, label='Linhas executadas (medido)')
    ax2.plot(valores_n, teorico, 's--', color='#DC2626',
             linewidth=1.5, markersize=4, alpha=0.7, label='5 × (2ⁿ − 1) teórico')
    ax2.set_xlabel('Número de discos (n)', fontsize=12)
    ax2.set_ylabel('Linhas executadas (escala log)', fontsize=12)
    ax2.set_title('Desempenho - Escala Logarítmica', fontsize=14, fontweight='bold')
    ax2.set_yscale('log')
    ax2.legend(fontsize=10)
    ax2.grid(True, alpha=0.3, which='both')

    plt.tight_layout()
    plt.savefig('grafico_desempenho.png', dpi=200, bbox_inches='tight')
    print("\n✅ Gráfico salvo: grafico_desempenho.png")
    plt.show()

    # ----- GRÁFICO 2: Barras de movimentos -----
    fig2, ax3 = plt.subplots(figsize=(10, 6))
    ax3.bar(valores_n, movimentos, color='#7C3AED', alpha=0.85, edgecolor='#5B21B6')
    ax3.set_xlabel('Número de discos (n)', fontsize=12)
    ax3.set_ylabel('Número de movimentos', fontsize=12)
    ax3.set_title('Movimentos Necessários por Número de Discos', fontsize=14, fontweight='bold')
    ax3.set_yscale('log')
    ax3.grid(True, alpha=0.3, axis='y')

    plt.tight_layout()
    plt.savefig('grafico_movimentos.png', dpi=200, bbox_inches='tight')
    print("✅ Gráfico salvo: grafico_movimentos.png")
    plt.show()


# =============================================================================
# EXECUÇÃO PRINCIPAL
# =============================================================================
if __name__ == "__main__":
    # 1. Demonstração visual com 3 discos
    demonstracao()

    # 2. Bateria de testes completa
    valores_n, linhas_executadas, movimentos = executar_testes()

    # 3. Gerar e exibir gráficos
    gerar_graficos(valores_n, linhas_executadas, movimentos)

    print("\n🎯 Concluído! Os gráficos foram salvos na pasta atual.")
