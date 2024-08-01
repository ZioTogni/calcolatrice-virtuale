#VARIABILI
nome_calcolatrice="La Tua Calcolatrice Virtuale"
operazione_1="addizione"
operazione_2="sottrazione"
operazione_3="moltiplicazione"
operazione_4="divisione"
#PROGRAMMA
print("Salve, io sono "+nome_calcolatrice+ " e sono qui per fare dei calcoli di livello base!")
print("\nCome prima cosa dimmi l'operazione che ti serve! (ATTENZIONE, non puoi usare operazioni miste, se scegli per esempio l'addizione non potrai usare insieme anche la sottrazione!)")
operazione_richiesta=input()
if operazione_richiesta==operazione_1:
    print("Bene, hai scelto l'addizione!")
    a=input("Inserisci il primo numero:")
    b=input("Inserisci il secondo numero:")
    x=float(a)+float(b)
    print("La somma dei 2 numeri inseriti è:",x)
elif operazione_richiesta==operazione_2:
    print("Bene, hai scelto la sottrazione!")
    a=input("Inserisci il primo numero:")
    b=input("Inserisci il secondo numero:")
    x=float(a)-float(b)
    print("La sottrazione dei 2 numeri inseriti è:",x)
elif operazione_richiesta==operazione_3:
    print("Bene, hai scelto la moltiplicazione!")
    a=input("Inserisci il primo numero:")
    b=input("Inserisci il secondo numero:")
    x=float(a)*float(b)
    print("La moltiplicazione dei 2 numeri inseriti è:",x)
elif operazione_richiesta==operazione_4:
    print("Bene, hai scelto la divisione!")
    a=input("Inserisci il primo numero:")
    b=input("Inserisci il secondo numero:")
    x=float(a)/float(b)
    print("La divisione dei 2 numeri inseriti è:",x)
else:
    print("Questa non è un'operazione,riavvia il programma perfavore!")