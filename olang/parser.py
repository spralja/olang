

def parse(l):
    l = l.replace('!', '(__base__):')
    l = l.replace('``', '.__copy__(2)')
    l = l.replace('`', '.__copy__(1)')
    return l