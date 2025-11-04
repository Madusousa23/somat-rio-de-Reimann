#somatório de Reimann
#criar graficos para os 3 (inf,cent,sup)
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

a = 0
b= 5
n = 5
xi = 0
f=0
soma=0
delta = (b - a)/n

#inferior
def inferior(xi,a,delta,f,):
  soma =0
  for i in range(n):
    xi = a + i * delta
    #print("Pontos: ",ponto_medio)
    f = 2*i+1
    #print("")
    #print("Pontos xi",xi)
    #print("")
    #print("\n fórmula",f)
    soma = soma+f
  print("-------------Inferior----------------")
  print("\nSomatório Inferior: ",soma)


#superior
def superior (a,delta,xi,f):
  soma=0
  print("\n--------Superior-------")
  for i in range(1,6):
    xi = a + i * delta
    f = 2* xi + 1
    soma = soma + f
  print("\nSomatório Superior: ",soma)

#central
def central (xi,a,delta,n,f):
  soma =0
  for i in range(n):
    xi= a + (i + 0.5)*delta
    f = 2 * xi + 1
    soma = soma + f
  print("\n-----------Central------------")
  print("\nSomatório Central: ",soma)


inferior(xi,a,delta,f)
superior (a,delta,xi,f)
central (xi,a,delta,n,f)

# -------------------- GRÁFICOS --------------------

def f_func(x):
    return 2 * x + 1

# Função para plotar os gráficos de Riemann
def plot_riemann(f, a, b, n, tipo):
    dx = (b - a) / n
    x = np.linspace(a, b, 1000)
    y = f(x)

    plt.plot(x, y, 'b-', linewidth=2, label='f(x) = 2x + 1')

    # Escolher tipo de ponto
    if tipo == 'inferior':
        x_i = np.array([a + i * dx for i in range(n)])
    elif tipo == 'superior':
        x_i = np.array([a + (i + 1) * dx for i in range(n)])
    else:
        x_i = np.array([a + (i + 0.5) * dx for i in range(n)])

    y_i = f(x_i)

    for i in range(n):
        plt.bar(x_i[i], y_i[i], width=dx, align='edge', alpha=0.3, edgecolor='black', label='Retângulos' if i==0 else "")

    plt.title(f"Soma de Riemann - {tipo.capitalize()}")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.show()


# Plota os três tipos de soma
plot_riemann(f_func, a, b, n, 'inferior')
plot_riemann(f_func, a, b, n, 'central')
plot_riemann(f_func, a, b, n, 'superior')
