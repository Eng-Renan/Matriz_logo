import RPi.GPIO as gpio
import time
import datetime
import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup
import datetime
gpio.setmode(gpio.BCM)  #define o Raspberry para trabalhar com numero GPIO e não pinout da placa
gpio.setwarnings(False) #não mostra alarm de portas


######## Config pin outputs ##########
gpio.setup(4, gpio.OUT)
gpio.setup(17, gpio.OUT)
gpio.setup(27, gpio.OUT)
gpio.setup(22, gpio.OUT)
gpio.setup(5, gpio.OUT)
gpio.setup(6, gpio.OUT)
gpio.setup(13, gpio.OUT)
gpio.setup(19, gpio.OUT)
gpio.setup(20, gpio.OUT)  # Led Azul (Connecting)
gpio.setup(21, gpio.OUT)  # Led Verde (Connected)



######## Reset das portas GPIO ########
def reset():
        gpio.output(4, gpio.HIGH)
        gpio.output(17, gpio.HIGH)
        gpio.output(27, gpio.HIGH)
        gpio.output(22, gpio.HIGH)
        gpio.output(5, gpio.HIGH)
        gpio.output(6, gpio.HIGH)
        gpio.output(13, gpio.HIGH)
        gpio.output(19, gpio.HIGH)
        print ("Reset GPIO")

###### Reset de incilização #######

reset()

###### URL da API #######

#url = 'http://172.22.131.177/'
url = 'https://tvcultura.com.br/temperatura'


####### Consulta API ########        
def check_connection():
        
    
    try:
        request = requests.get(url)
        print("Connected to the API")
        gpio.output(20, gpio.LOW)
        gpio.output(21, gpio.HIGH)
        connection = 1
           
    except (requests.ConnectionError) as exception:
        print("No API connection.")
        gpio.output(20, gpio.HIGH)
        gpio.output(21, gpio.LOW)
        reset()
        connection = 2
        

        if connection == 2:
                check_connection()
                reset()
                
                
    
############# Lista de Icones ##############
                
i1   = "1"
i1n  = "1n"
i2   = "2"
i2n  = "2n"
i2r  = "2r"
i2rn = "2rn"
i3   = "3"
i3n  = "3n"
i3tm = "3tm"
i3tmn = "3tmn"
i4   = "4"
i4n  = "4n"
i4r  = "4r"
i4rn = "4rn"
i4t  = "4t"
i4tn = "4tn"
i5   = "5"
i5n  = "5n"
i6   = "6"
i6n  = "6n"
i7   = "7"
i7n  = "7n"
i8   = "8"
i8n  = "8n"
i9   = "9"
i9n  = "9n"


# Identificação dos Icons e Comutação dos Relays 


def aciona():

##########################     Rele - A     ################################
     if icon1 == (i1):
        gpio.output(4, gpio.LOW)  #Raspberry Pin-4 // Evertz Pin-8 (gpi-A)
        print ("GPI-A ON")
        
     if icon1 == (i2):
        gpio.output(4, gpio.LOW)  #Raspberry Pin-4 // Evertz Pin-8 (gpi-A)
        print ("GPI-A ON")
        
     if icon1 == (i9):
        gpio.output(4, gpio.LOW)  #Raspberry Pin-4 // Evertz Pin-8 (gpi-A)
        print ("GPI-A ON")
    
 
    
##########################     Rele - B     ################################        

     if icon1 == (i2r):
        gpio.output(17, gpio.LOW)  #Raspberry Pin-17 // Evertz Pin-14 (gpi-B)
        print ("GPI-B ON")
        


##########################     Rele - C     ################################        

     if icon1 == (i1n):
        gpio.output(27, gpio.LOW)  #Raspberry Pin-27 // Evertz Pin-5 (gpi-C)
        print ("GPI-C ON")
        
     if icon1 == (i2n):
        gpio.output(27, gpio.LOW)  #Raspberry Pin-27 // Evertz Pin-5 (gpi-C)
        print ("GPI-C ON")
        
     if icon1 == (i2rn):
        gpio.output(27, gpio.LOW)  #Raspberry Pin-27 // Evertz Pin-5 (gpi-C)
        print ("GPI-C ON")

     if icon1 == (i9n):
        gpio.output(27, gpio.LOW)  #Raspberry Pin-27 // Evertz Pin-5 (gpi-C)
        print ("GPI-C ON") 
   
   

##########################     Rele - D     ################################

    
     if icon1 == (i3tm):
        gpio.output(22, gpio.LOW)  #Raspberry Pin-22 // Evertz Pin-9 (gpi-D)
        print ("GPI-D ON")

     if icon1 == (i3tmn):
        gpio.output(22, gpio.LOW)  #Raspberry Pin-22 // Evertz Pin-9 (gpi-D)
        print ("GPI-D ON")
        
     if icon1 == (i7):
        gpio.output(22, gpio.LOW)  #Raspberry Pin-22 // Evertz Pin-9 (gpi-D)
        print ("GPI-D ON")    

     if icon1 == (i7n):
        gpio.output(22, gpio.LOW)  #Raspberry Pin-22 // Evertz Pin-9 (gpi-D)
        print ("GPI-D ON")

     if icon1 == (i8):
        gpio.output(22, gpio.LOW)  #Raspberry Pin-22 // Evertz Pin-9 (gpi-D)
        print ("GPI-D ON")

     if icon1 == (i8n):
        gpio.output(22, gpio.LOW)  #Raspberry Pin-22 // Evertz Pin-9 (gpi-D)
        print ("GPI-D ON")    


##########################     Rele - E    ################################


     if icon1 == (i3):
        gpio.output(5, gpio.LOW)  #Raspberry Pin-5 // Evertz Pin-12 (gpi-E)
        print ("GPI-E ON")

        
     if icon1 == (i3n):
        gpio.output(5, gpio.LOW)  #Raspberry Pin-5 // Evertz Pin-12 (gpi-E)
        print ("GPI-E ON")

     if icon1 == (i4):
        gpio.output(5, gpio.LOW)  #Raspberry Pin-5 // Evertz Pin-12 (gpi-E)
        print ("GPI-E ON")   


##########################     Rele - F     ################################


     if icon1 == (i4n):
        gpio.output(6, gpio.LOW)  #Raspberry Pin-6 // Evertz Pin-7 (gpi-F)
        print ("GPI-F ON")
   


##########################     Rele - G     ################################

        
     if icon1 == (i4r):
        gpio.output(13, gpio.LOW)  #Raspberry Pin-13 // Evertz Pin-13 (gpi-G)
        print ("GPI-G ON")   
        
     if icon1 == (i4n):
        gpio.output(13, gpio.LOW)  #Raspberry Pin-13 // Evertz Pin-13 (gpi-G)
        print ("GPI-G ON")
        
     if icon1 == (i5):
        gpio.output(13, gpio.LOW)  #Raspberry Pin-13 // Evertz Pin-13 (gpi-G)
        print ("GPI-G ON")
        
     if icon1 == (i5n):
        gpio.output(13, gpio.LOW)  #Raspberry Pin-13 // Evertz Pin-13 (gpi-G)
        print ("GPI-G ON")   
     


##########################     Rele - H     ################################


     if icon1 == (i6):
        gpio.output(19, gpio.LOW)  #Raspberry Pin-19 // Evertz Pin-11 (gpi-H)
        print ("GPI-H ON")
        
     if icon1 == (i4t):
        gpio.output(19, gpio.LOW)  #Raspberry Pin-19 // Evertz Pin-11 (gpi-H)
        print ("GPI-H ON")
        
     if icon1 == (i4tn):
        gpio.output(19, gpio.LOW)  #Raspberry Pin-19 // Evertz Pin-11 (gpi-H)
        print ("GPI-H ON")
        
     if icon1 == (i6n):
        gpio.output(19, gpio.LOW)  #Raspberry Pin-19 // Evertz Pin-11 (gpi-H)
        print ("GPI-H ON")    



##### Loop #####


while True:
     
     check_connection()
     response = requests.get(url)
     html = requests.get(url, verify=False)
     bs = BeautifulSoup(html.text)
     icon1 = bs.icon.string
     print("icone-1")
     print(icon1)
     aciona()
     time.sleep(10)
     check_connection()    
     response = requests.get(url)
     html = requests.get(url, verify=False)
     bs = BeautifulSoup(html.text)
     icon2 = bs.icon.string
     print("icone-2")
     print(icon2)
     if icon1 != icon2:
             reset()
             print("Reset para mudança de icone")
             
     
        
     
     
   
    
              
           
           
    

    
   
    
        
    







































