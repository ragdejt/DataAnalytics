import numpy

def generate_sku(nome, categoria):
    number = numpy.random.randint(low=1000, high=9999, size=1)
    sku = f'{nome[:3].upper()}{categoria[:3].upper()}{number[0]}'
    return sku
