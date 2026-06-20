NOMES = ['Brasil', 'Alemanha', 'Itália', 'Argentina']

def penta():
    return [NOMES[0]]

def tetra():
    return [NOMES[0], NOMES[1] + " e " + NOMES[2]]

def tri():
    return [NOMES[0], NOMES[1], NOMES[2], NOMES[3]]

print(penta())
print(tetra())
print(tri())

print(penta()[0])
print(tetra()[0])
print(tri()[0])