'''Implemente a função trocaPU(), que aceita uma lista como entrada e troca o primeiro e último elementos da lista.
Você pode considerar que a lista não estará vazia. A função não deverá retornar nada'''

def trocaPU(list):
    item1 = list[0]
    list[0] = list[3]
    list[3] = item1

ingredientes = ['farinha', 'açúcar', 'manteiga', 'maçãs']
trocaPU(ingredientes)
print(ingredientes)
