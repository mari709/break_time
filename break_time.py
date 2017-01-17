import time
import webbrowser

total_breaks = 2
break_count = 0
seconds = 2*60*60 #2 hours

print ("Comenzado: "+ time.ctime())
while (break_count < total_breaks):
    time.sleep(seconds)
    webbrowser.open("https://www.youtube.com")
    break_count += 1
    print  ("abierto " + str(break_count) + " veces")
