entradas = [1, 7, 5]

pesos = [0.8, 0.1, 0.0]

def soma(e,p):
	s = 0

	for x in range(len(e)):
		s += e[x]*p[x]

	return s


def step_function(soma):
	if soma >= 1:
		return 1
	else:
		return 0


s = soma(entradas,pesos)
r = step_function(s)


print(r)