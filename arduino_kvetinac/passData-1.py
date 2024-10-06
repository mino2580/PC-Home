import serial                       #instalovana knizinica pre seriovu komunikaciu
import time                         #kniznica pre pracu s casom
import datetime

arduinoData=serial.Serial('com3',115200)  #vytvorenie objektu Serial,otvorenie serioveho portu,nastavenie Bd
time.sleep(1)                        #pockaj 1s

    

while True:                             #nekonecna smzcka
    while(arduinoData.inWaiting()==0):  #ak nie su data v buferi spzsti sa nekone4na smycka
         pass                           #nevikona nic
    dataPacket=arduinoData.readline()   #Return the number of bytes in the receive buffer.
    dataPacket=str(dataPacket,'utf-8')  #Funkcia Python str() vráti reťazcovú verziu objektu.Po seriali prijimam int asci kod
    dataPacket=dataPacket.strip('\r\n') #Metóda strip() zabudovaná funkcia jazyka Python sa používa na odstránenie všetkých úvodných a koncových medzier z reťazca.
    splitPacket=dataPacket.split(",")   #Metóda Python String split() v Pythone rozdelila reťazec do zoznamu reťazcov po prerušení daného reťazca zadaným oddeľovačom.
    #petrzlen=int(splitPacket[0])        #skopirovanie a pretzpovanie casti retayca,rodeleneho na pole retaycov
    petrzlen=(splitPacket[0]) 
    pazitka=(splitPacket[1])
    tymian=(splitPacket[2])
    rozmarin=(splitPacket[3])
    with open("mojeData.csv", "a", encoding="utf-8") as f:
          f.write(petrzlen)
          f.write(";")
          f.write(pazitka)
          f.write(";")
          f.write(tymian)
          f.write(";")
          f.write(rozmarin)
          f.write(";\n")
    print("Petrzlen= ",petrzlen," Pazitka= ",pazitka," Tymian= ",tymian," Rozmarin= ",rozmarin)
   