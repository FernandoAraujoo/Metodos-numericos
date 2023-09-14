def newtonRaphson(x0, epsilon, maxIteracoes):
    iteracao = 0

    while iteracao < maxIteracoes:
        derivada_x0 = derivada(x0)
        if derivada_x0 == 0:
            raise ValueError("Derivada se tornou zero durante a iteração.")
        x1 = x0 - funcao(x0) / derivada_x0
        if abs(x1 - x0) < epsilon:
            return x1
        x0 = x1
        iteracao += 1

    raise ValueError(f"O método de Newton-Raphson não convergiu após {maxIteracoes} iterações.")

def funcao(x):
    # função
    return x * x - 4 

def derivada(x):
    # Derivada da função 
    return 2 * x 

x0 = 1.0
epsilon = 0.0001
maxIteracoes = 100
raiz = newtonRaphson(x0, epsilon, maxIteracoes)
print(f"Raiz encontrada: {raiz}")