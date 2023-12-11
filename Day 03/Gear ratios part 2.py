def calcola_valore_ingranaggio(riga, posizione_asterisco, riga_corrente, riga_precedente, riga_successiva):
    valore_ingranaggio = 0
    numeri_vicini = []
    
    numero_a_sinistra = ottieni_numero_a_sinistra(posizione_asterisco, riga_corrente)
    if numero_a_sinistra:
        numeri_vicini.append(numero_a_sinistra)
    numero_a_destra = ottieni_numero_a_destra(posizione_asterisco, riga_corrente)
    if numero_a_destra:
        numeri_vicini.append(numero_a_destra)
        
    if riga_precedente[posizione_asterisco].isdigit():
        numero_sopra = ottieni_numero_sopra(posizione_asterisco, riga_precedente)
        if numero_sopra:
            numeri_vicini.append(numero_sopra)
    else:
        numero_sopra_sinistra = ottieni_numero_a_sinistra(posizione_asterisco, riga_precedente)
        if numero_sopra_sinistra:
            numeri_vicini.append(numero_sopra_sinistra)
        numero_sopra_destra = ottieni_numero_a_destra(posizione_asterisco, riga_precedente)
        if numero_sopra_destra:
            numeri_vicini.append(numero_sopra_destra)
            
    if riga_successiva[posizione_asterisco].isdigit():
        numero_sotto = ottieni_numero_sotto(posizione_asterisco, riga_successiva)
        if numero_sotto:
            numeri_vicini.append(numero_sotto)
    else:
        numero_sotto_sinistra = ottieni_numero_a_sinistra(posizione_asterisco, riga_successiva)
        if numero_sotto_sinistra:
            numeri_vicini.append(numero_sotto_sinistra)
        numero_sotto_destra = ottieni_numero_a_destra(posizione_asterisco, riga_successiva)
        if numero_sotto_destra:
            numeri_vicini.append(numero_sotto_destra)

    if len(numeri_vicini) != 2:
        return 0
    else:
        print("Riga: " + str(riga + 1) + " - Numeri vicini: " + str(numeri_vicini))
        return numeri_vicini[0] * numeri_vicini[1]



def ottieni_numero_a_sinistra(posizione_asterisco, riga_corrente):
    numero = ''
    
    posizioneDiRicerca = posizione_asterisco - 1
    
    if is_posizione_valida(posizioneDiRicerca, riga_corrente) and riga_corrente[posizione_asterisco - 1].isdigit():
        pos = posizione_asterisco - 1
        while is_posizione_valida(pos, riga_corrente) and riga_corrente[pos].isdigit():
            numero += riga_corrente[pos]
            pos -= 1    
        return int(numero[::-1])

    return None

def ottieni_numero_a_destra(posizione_asterisco, riga_corrente):
    numero = ''

    posizioneDiRicerca = posizione_asterisco + 1

    if is_posizione_valida(posizioneDiRicerca, riga_corrente) and riga_corrente[posizione_asterisco + 1].isdigit():
        pos = posizione_asterisco + 1
        while is_posizione_valida(pos, riga_corrente) and riga_corrente[pos].isdigit():
            numero += riga_corrente[pos]
            pos += 1
        return int(numero)

    return None

def ottieni_numero_sopra(posizione_asterisco, riga_precedente):
    numero = ''

    posizioneDiRicerca = posizione_asterisco
    if is_posizione_valida(posizioneDiRicerca, riga_precedente):
        pos = posizione_asterisco
        while is_posizione_valida(pos, riga_precedente) and riga_precedente[pos].isdigit():
            numero += riga_precedente[pos]
            pos -= 1
        numero = numero[::-1]
        pos = posizione_asterisco + 1
        while(is_posizione_valida(pos, riga_precedente) and riga_precedente[pos].isdigit()):
            numero += riga_precedente[pos]
            pos += 1
        return int(numero)

    return None

def ottieni_numero_sotto(posizione_asterisco, riga_successiva):
    numero = ''

    posizioneDiRicerca = posizione_asterisco
    if is_posizione_valida(posizioneDiRicerca, riga_successiva):
        pos = posizione_asterisco
        while is_posizione_valida(pos, riga_successiva) and riga_successiva[pos].isdigit():
            numero += riga_successiva[pos]
            pos -= 1
        numero = numero[::-1]
        pos = posizione_asterisco + 1
        while (is_posizione_valida(pos, riga_successiva) and riga_successiva[pos].isdigit()):
            numero += riga_successiva[pos]
            pos += 1
        return int(numero)

    return None


def is_posizione_valida(posizione, riga_corrente):
    return posizione >= 0 and posizione < len(riga_corrente)


with open("input.txt", 'r') as file:
    riga_corrente = file.readline().rstrip()
    riga_precedente = ''
    riga_successiva = file.readline().rstrip()
    posizione_asterisco = None
    somma_ratio_ingranaggi = 0
    counter = 0
    
    while riga_corrente:
        for i in range(len(riga_corrente)):
            char = riga_corrente[i]
            if char == '*':
                posizione_asterisco = i
                valore_ingranaggio = calcola_valore_ingranaggio(counter, 
                    posizione_asterisco, riga_corrente, riga_precedente, riga_successiva)
                somma_ratio_ingranaggi += valore_ingranaggio
            
        riga_precedente = riga_corrente
        riga_corrente = riga_successiva
        riga_successiva = file.readline().rstrip()
        counter += 1

print(somma_ratio_ingranaggi)
