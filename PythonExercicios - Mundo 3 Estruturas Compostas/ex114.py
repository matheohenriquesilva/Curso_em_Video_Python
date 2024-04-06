# Site está acessível?
import urllib
import urllib.request


try:
    site = urllib.request.urlopen("http://www.pudin.com.br")
except urllib.error.URLError:
    print("O site Pudin não está acessível no momento.")
else:
    print("Consegui acessar o site Pudin com sucesso!")
