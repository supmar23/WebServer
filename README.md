# PROGETTO RETI DI CALCOLATORI 2019-2020
## Web Server HTTP Multithread — Traccia 2
Il web server scritto in python, realizzato sul localhost, visualizza un classica testata giornalistica di moda, in stile giornale cartaceo, in cui sono presenti più pagine html in grado di gestire più connessioni in contemporanea.

In particolare è composto da una pagina principale denominata *index.html* e da altre sotto pagine, una per ogni articolo.

Le pagine html sono personalizzate con due fogli di stile css, uno per la pagina principale (index.html) e un secondo comune per le altre pagine riguardanti i vari articoli.

La struttura del server multithread è basata sulla classe SimpleHTTPServer.**SimpleHTTPRequestHandler** aggiornata con un metodo il quale scrive su file tutte le connessioni in entrata da parte dei client che si connettono al server (metodo **handle_one_request**) creando una sorta di log file.

Nella pagina iniziale, in alto a destra, è presente un piccolo menù che permette di tornare alla pagina iniziale, di visualizzare una pagina con alcune informazioni e un download link in grado di scaricare la pagina in formato pdf.

## Utilizzo
* Lanciare il server da terminale: `python http_multithread.py [numero di porta]` se si omette il numero di porta il server utilizzerà la porta numero 8080
* Connettersi tramite browser tramite indirizzo: `http://127.0.0.1:8080/index.html`

## Informazioni aggiuntive
* **NB:** L’attributo *download* non è supportato da Edge (versione 12), Safari 10 (e precedenti) o Opera versione 12 (e precedenti)
* Il web server è stato testato su: Chrome, Brave e Safari.

## Autori
* Interfaccia Sito Web e ampliamento della struttura del web server creata da: Mario Ciccioni, mario.ciccioni@studio.unibo.it
* Struttura del Web Server creata da: A. Piroddi - G. Pau, Programmazione di Reti, Università di Bologna
