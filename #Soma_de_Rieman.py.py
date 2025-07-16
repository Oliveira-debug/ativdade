# Soma de Reiman
# Bibliotecas importadas para o código
from sympy import integrate, symbols
from sympy import cos, sin, tan, cot, sec, csc

#F(x)
x = symbols('x')
função = (x**2)+(3*x)+10 
#intervalo
xinicial = 1
xfinal = 50
Soma_de_Reiman = integrate(função, (x, xinicial, xfinal))
# Integração simbólica exata
integral_definida = integrate(função, (x, xinicial, xfinal))
print("Integral definida (valor exato):", integral_definida)
# Número de subintervalos
n = 100
dx = (xfinal - xinicial) / n
# Pontos à esquerda dos subintervalos
def f(x):
    return x**2 + 3*x + 10
soma_riemann = 0
for i in range(n):
    xi = xinicial + i * dx  # ponto à esquerda de cada subintervalo
    soma_riemann += f(xi) * dx
print("Aproximação por Soma de Riemann (esquerda):", soma_riemann)
