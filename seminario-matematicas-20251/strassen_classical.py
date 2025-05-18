import numpy as np
import matplotlib.pyplot as plt

n = np.arange(1, 300, 1)

# 1. Método clásico: O(n³)
classic = n ** 3

# 2. Strassen: Antes de n=128, añadimos un overhead constante; después, solo n^2.81
overhead_before_128 = 50000  # Ajusta este valor para controlar el punto de cruce
strassen = np.where(
    n <= 128,
    overhead_before_128 + n ** 2.81,  # Overhead + término dominante
    n ** 2.81                         # Solo término dominante
)

# Normalización para mejor visualización
classic_normalized = classic / 1e6
strassen_normalized = strassen / 1e6

plt.figure(figsize=(12, 6))
plt.plot(n, classic_normalized, 'r-', linewidth=2, label='Clásico (O(n³))')
plt.plot(n, strassen_normalized, 'b-', linewidth=2, label='Strassen (O(n²·⁸¹))')

# Marcar el punto de cruce (n=128)
crossover_n = 128
crossover_index = np.where(n >= crossover_n)[0][0]
plt.scatter(crossover_n, strassen_normalized[crossover_index], color='black', zorder=5, s=100)
plt.annotate(f'n = {crossover_n}', (crossover_n + 10, strassen_normalized[crossover_index] + 5), fontsize=12, weight='bold')

plt.xlabel('Tamaño de la matriz (n)', fontsize=12)
plt.ylabel('Operaciones (millones)', fontsize=12)
plt.title('Strassen vs. Clásico', fontsize=14)
plt.legend(fontsize=10)
plt.grid(True, linestyle='--', alpha=0.6)

# Línea vertical en n=128
plt.axvline(x=crossover_n, color='gray', linestyle=':', linewidth=1.5)

plt.show()