def bisseccao(a, b, epsilon, maxIteracoes):
    if funcao(a) * funcao(b) >= 0:
        raise ValueError("A função não atende aos requisitos do método da bissecção.")

    iteracao = 0

    while iteracao < maxIteracoes:
        x0 = (a + b) / 2
        if funcao(x0) == 0 or abs(b - a) < epsilon:
            return x0
        elif funcao(x0) * funcao(a) < 0:
            b = x0
        else:
            a = x0
        iteracao += 1

    raise ValueError(f"O método da bissecção não convergiu após {maxIteracoes} iterações.")

def funcao(x):
    # função
    return x * x - 4 

a = 0
b = 5
epsilon = 0.0001
maxIteracoes = 100
raiz = bisseccao(a, b, epsilon, maxIteracoes)
print(f"Raiz encontrada: {raiz}")
