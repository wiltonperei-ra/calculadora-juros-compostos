python# Calculadora de Juros Compostos - Projeto 
# Autor: Wilton Pereira - Zona Sul SP

def calcular_juros_compostos(capital, taxa, tempo):
    """
    Calcula o montante final com base em juros compostos
    Fórmula: M = C * (1 + i)^t
    """
    montante = capital * (1 + taxa/100) ** tempo
    juros = montante - capital
    return montante, juros

print("--- Calculadora de Juros Compostos ---")
try:
    capital = float(input("Digite o capital inicial (R$): "))
    taxa = float(input("Digite a taxa de juros ao mês (%): "))
    tempo = int(input("Digite o tempo (em meses): "))

    montante_final, total_juros = calcular_juros_compostos(capital, taxa, tempo)

    print("\n--- Resultado ---")
    print(f"Capital Inicial: R$ {capital:.2f}")
    print(f"Montante Final: R$ {montante_final:.2f}")
    print(f"Total de Juros: R$ {total_juros:.2f}")

except ValueError:
    print("Erro: Por favor, digite apenas números válidos.")
