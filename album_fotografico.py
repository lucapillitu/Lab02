
"""Carica le foto dal file, creando un nuovo anno ogni volta che compare per la prima volta"""
def carica_da_file(file_path):
    album = {}#dizionario di dati contenente le informazioni dell'album
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            f.readline()

            for line in f:
                line = line.strip()#rimumovo parti testuali vuote
                if not line:
                    continue

                campi = line.split(",")#divisione dei campi
                foto = {
                    "codice": campi[0].strip(),
                    "titolo": campi[1].strip(),
                    "autore": campi[2].strip(),
                    "mese": int(campi[3]),
                    "anno": int(campi[4]),
                }

                if int(campi[4]) not in album:
                    album[int(campi[4])] = []

                album[int(campi[4])].append(foto)
    except FileNotFoundError:
        return None

    return album


    """Aggiunge una foto all'album, creando l'anno al volo se non è ancora presente"""
def aggiungi_foto(album, codice, titolo, autore, mese, anno, file_path):
    foto = {}
    #controlli sulla singola foto
    if mese < 1 or mese > 12:
        return None

    for a in album:
        for c in album[a]:
            if c["codice"] == codice:
                return None

    #passati i controlli aggiungo la foto e relativi dati
    try:
        with open(file_path, "a", encoding="utf-8") as f:
            if anno not in album:
                album[anno] = []

            foto = {
                "codice": codice,
                "titolo": titolo,
                "autore": autore,
                "mese": mese,
                "anno": anno,
            }
            album[anno].append(foto)
            f.write(f"{codice},{titolo},{autore},{mese},{anno}\n")#aggiungo linea dati al file

    except FileNotFoundError:
        return None

    return foto


    """Cerca una foto nell'album dato il codice"""
def cerca_foto(album, codice):
    for anno in album:
        for c in album[anno]:
            if c["codice"] == codice:
                return f"{c["codice"]}, {c["titolo"]}, {c["autore"]}, {c["mese"]}, {c["anno"]}" #ritorno la stringa da stampare a video

    return None


    """Ordina i titoli delle foto di un dato anno in ordine alfabetico"""
def elenco_foto_anno_per_titolo(album, anno):
    titoli = []
    if anno not in album:
        return None
    for c in album[anno]: # titoli = [c["titolo" for c in album[anno]]
        titoli.append(c["titolo"])

    return sorted(titoli)


"""MAIN"""
def main():
    album = {}
    file_path = "album_fotografico.csv"

    while True:
        print("\n--- MENU ALBUM FOTOGRAFICO ---")
        print("1. Carica album da file")
        print("2. Aggiungi una nuova foto")
        print("3. Cerca una foto per codice")
        print("4. Elenco foto di un anno (ordinato per titolo)")
        print("5. Esci")

        scelta = input("Scegli un'opzione >> ").strip()
##
        if scelta == "1":
            while True:
                file_path = input("Inserisci il path del file da caricare: ").strip()
                album = carica_da_file(file_path)#1

                if album is not None:
                    #print(album)#prova
                    break
##
        elif scelta == "2":
            if not album:
                print("Prima carica l'album da file.")
                continue

            codice = input("Codice della foto: ").strip()
            titolo = input("Titolo: ").strip()
            autore = input("Autore: ").strip()

            try:
                mese = int(input("Mese (1-12): ").strip())
                anno = int(input("Anno: ").strip())
            except ValueError:
                print("Errore: inserire valori numerici validi per mese e anno.")
                continue
            foto = aggiungi_foto(album, codice, titolo, autore, mese, anno, file_path)#2

            if foto:
                print(f"Foto aggiunta con successo!")
            else:
                print("Non è stato possibile aggiungere la foto.")
##
        elif scelta == "3":
            if not album:
                print("L'album è vuoto.")
                continue

            codice = input("Inserisci il codice della foto da cercare: ").strip()
            risultato = cerca_foto(album, codice)#3 (risultato --> deve essere una stringa)

            if risultato:
                print(f"Foto trovata: {risultato}")
            else:
                print("Foto non trovata.")
##
        elif scelta == "4":
            if not album:
                print("L'album è vuoto.")
                continue

            try:
                anno = int(input("Inserisci l'anno da consultare: ").strip())
            except ValueError:
                print("Errore: inserire un valore numerico valido.")
                continue
            titoli = elenco_foto_anno_per_titolo(album, anno)#4

            if titoli is not None:
                print(f'\nFoto del {anno}:')
                print("\n".join([f"- {titolo}" for titolo in titoli]))
            else:
                print(f"Nessuna foto trovata per l'anno {anno}.")

##
        elif scelta == "5":
            print("Uscita dal programma.")
            break
        else:
            print("Opzione non valida. Riprova.")


if __name__ == "__main__":
    main()
