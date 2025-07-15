import sympy as sp
import random

def finite_diffs_sympy(xs, ordem=1, x0=1):
    n = len(xs)
    x = sp.Symbol('x')

    # Construir a matriz A simbolicamente
    A = sp.Matrix([
        [(xi - x0)**i / sp.factorial(i) for xi in xs]
        for i in range(n)
    ])

    # Vetor b: 1 na posição "ordem", 0 nos outros
    b = sp.Matrix([1 if i == ordem else 0 for i in range(n)])

    # Resolver o sistema linear A * c = b
    coef = A.LUsolve(b)
    
    return coef

def f(x):
    return x**x

# Definir ponto de derivação e ordem
x0 = 2
ordem = 1
pontos = 50

# Gerar pontos arbitrários em torno de x0
xs_vals = sorted([x0 - 0.25 + 0.5 * random.random() for _ in range(pontos)])

# Obter coeficientes simbólicos
coef = finite_diffs_sympy(xs_vals, ordem, x0)

# Calcular a aproximação da derivada
aprox = sum(coef[i] * f(xs_vals[i]) for i in range(pontos))

# Imprimir resultados
print("Pontos usados (xs):", xs_vals)
print("Coeficientes simbólicos:")
for i, c in enumerate(coef):
    print(f"c{i} = {sp.simplify(c)}")

print(f"\nAproximação da derivada de ordem {ordem} de f(x) = x^x em x = {x0}: {aprox.evalf()}")