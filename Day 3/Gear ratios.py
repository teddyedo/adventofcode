def is_numero_vicino_a_simboli(posizioni_cifre, riga_corrente, riga_precedente, riga_successiva):
    is_presente_simbolo = False
    
    #controlla riga corrente
    if is_simbolo(posizioni_cifre[0]-1, riga_corrente) or is_simbolo(posizioni_cifre[len(posizioni_cifre) - 1] + 1, riga_corrente):
        return True
        
    #controlla riga precedente
    if is_simbolo(posizioni_cifre[0]-1, riga_precedente) or is_simbolo(posizioni_cifre[len(posizioni_cifre) - 1] + 1, riga_precedente):
        return True
    for posizione in posizioni_cifre:
        if is_simbolo(posizione, riga_precedente):
            return True
        
    #controlla riga successiva
    if is_simbolo(posizioni_cifre[0]-1, riga_successiva) or is_simbolo(posizioni_cifre[len(posizioni_cifre) - 1] + 1, riga_successiva):
        return True
    for posizione in posizioni_cifre:
        if is_simbolo(posizione, riga_successiva):
            return True
    
    return False

def is_simbolo(posizione, riga):
    if posizione < 0 or posizione >= len(riga):
        return False
    char = riga[posizione]
    
    return char != '.' and not char.isdigit()

with open("input.txt", 'r') as file:
    riga_corrente = file.readline().rstrip()
    riga_precedente = ''
    riga_successiva = file.readline().rstrip()
    numero_che_sto_leggendo = []
    posizioni_cifre = []
    somma_ingranaggi = 0
    counter = 0
    numeri_riga = []
    
    while riga_corrente:
        for i in range(len(riga_corrente)):
            char = riga_corrente[i]
            if char.isdigit():
                numero_che_sto_leggendo.append(char)
                posizioni_cifre.append(i)
            if (not char.isdigit() or i == len(riga_corrente) - 1) and len(numero_che_sto_leggendo) > 0:
                if is_numero_vicino_a_simboli(posizioni_cifre, riga_corrente, riga_precedente, riga_successiva):
                    numero = int(''.join(numero_che_sto_leggendo))
                    somma_ingranaggi += numero
                    numeri_riga.append(numero)
                    # print(numero_che_sto_leggendo)
                numero_che_sto_leggendo = []
                posizioni_cifre = []

        # Aggiorna le righe
        riga_precedente = riga_corrente
        riga_corrente = riga_successiva
        riga_successiva = file.readline().rstrip()
        counter += 1

        print("Riga " + str(counter) + ": " + ''.join(str(numero) + ", " for numero in numeri_riga))
        numeri_riga = []

print(somma_ingranaggi)