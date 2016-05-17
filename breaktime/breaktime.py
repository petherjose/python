import webbrowser
import time

i = 0
while i < 6:
    time.sleep(10)
    webbrowser.open("http://www.terra.com.br")
    print "TESTE"
    i = i + 1
