#!/bin/env python
import sys, signal
import http.server
import socketserver
import time

# Legge il numero della porta dalla riga di comando
if sys.argv[1:]:
  port = int(sys.argv[1])
else:
  port = 8080

# estensione della classe SimpleHTTPRequestHandler
class MyRequestHandler(http.server.SimpleHTTPRequestHandler):

    # Override del metodo do_GET()
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

    # Metodo che crea una sorta di log file
    def handle_one_request(self):
        with open("logfile.txt", "a") as f:
            print("ip: " + self.client_address[0], "port: " + str(port),
                "[" + time.strftime("%d/%m/%Y") + " " + time.strftime("%H:%M:%S") + "]", file=f)
        return http.server.SimpleHTTPRequestHandler.handle_one_request(self)


# Funzione per permetterci di uscire dal processo tramite Ctrl-C
def signal_handler(signal, frame):
    print("\nCtrl+C received, shutting down server")
    try:
      if(server):
        server.server_close()
    finally:
      sys.exit(0)

# Creo l'Handler
Handler = MyRequestHandler

# Nota ForkingTCPServer non funziona su Windows come os.fork ()
# la funzione non è disponibile su quel sistema operativo. Invece dobbiamo usare il
# ThreadingTCPServer per gestire più richieste
server = socketserver.ThreadingTCPServer(('',port), Handler)

# Assicura che da tastiera usando la combinazione
# di tasti Ctrl-C termini in modo pulito tutti i thread generati
# In generale, per qualsiasi ragione in cui un flusso si interrompa, il threading si chiuderà correttamente
server.daemon_threads = True

# Il Server acconsente al riutilizzo del socket anche se ancora non è stato
# rilasciato quello precedente, andandolo a sovrascrivere
# Evitando situazioni di rifiuto richieste
server.allow_reuse_address = True

# Interrompe l’esecuzione se da tastiera arriva la sequenza (CTRL + C)
signal.signal(signal.SIGINT, signal_handler)

# Versione del server http
version = Handler.server_version

print("\n---Server started---")
print("Version: " + version)
print("Waiting for clients request on port: " + str(port))
print("Press Ctrl+C to close the server")

# Entra nel loop infinito
try:
  while True:
    server.serve_forever()
except KeyboardInterrupt:
  pass

server.server_close()
