# Atividade Prática02- questão03
distancia_percorrida = float(input("Digite a distância percorrida (km): "))
combustivel_gasto = float(input("Digite o combustível gasto (litros): "))

consumo_medio = distancia_percorrida / combustivel_gasto

print(f"Distância percorrida: {distancia_percorrida:.1f} km")
print(f"Combustível gasto: {combustivel_gasto:.1f} litros")
print(f"Consumo médio: {consumo_medio:.2f} km/l")