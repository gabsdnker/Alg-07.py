#BUSCA REVERSA

# Escreva uma função chamada buscaReversa, que encontra todas as chaves de um dicionário que estão mapeadas para um determinado valor.
def buscaReversa (dicionário, valor):
# A função deve receber como parâmetros um dicionário e um valor para ser buscado no dicionário.
    for chave in dicionário:
        lista= []
        if dicionário[chave] == valor:
            return lista.append(chave)
        elif chave == '':
            return lista

# Escreva uma função main para demonstrar sua função.
def main():
# Note que a função deve funcionar independentemente de ela retornar múltiplas chaves, uma única chave, ou nenhuma chave.
    d= {"G":1, "A":2, "B":3, "R":4, "I":5, "E":6, "L":7, "L":8, "I":9}
    v= input("Digite um valor: ")
    print(buscaReversa(d,v))

if __name__=='__main__':
    main()