###
###  Disclaimer, there are more holes than in a block of cheese in the plot, I was too busy coding to write something decent.
###
import random #### Random module
from random import choice ### Choice Module
from os import system ### OS module, Used here for animation
import time ### Time module
import threading ### Multi Threading baby :D

clear = lambda: system('clear') ### Prepares Terminal for next frame

clear() ### Program Starts Here
affi = 0
charis = random.randint(1,10)
intelli = random.randint(1,10)

print ("""
           .d8888b.                          .d8888b.                       
          d88P  Y88b                        d88P  Y88b                      
          Y88b.                             888    888                      
           "Y888b.   888  888 88888b.d88b.  888         .d88b.  88888b.d88b.  
              "Y88b. 888  888 888 "888 "88b 888        d88""88b 888 "888 "88b 
                "888 888  888 888  888  888 888    888 888  888 888  888  888 
          Y88b  d88P Y88b 888 888  888  888 Y88b  d88P Y88..88P 888  888  888 
           "Y8888P"   "Y88888 888  888  888  "Y8888P"   "Y88P"  888  888  888 
                          888                                             
                     Y8b d88P                                             
                      "Y88P"                  



 """)
time.sleep(1)
clear()

# set global variable flag
### I found this set of functions to allow me to loop some code while also looking for an input, you can find it here https://stackoverflow.com/a/47540581
flag = True

def normal():
    flag
    while flag:
        print (u"""
           .d8888b.                          .d8888b.                       
        \u001b[36m.d\u001b[0md88P\u001b[36mb.\u001b[0mY88b                      \u001b[36m.d\u001b[0md88P\u001b[36m8b\u001b[0mY88b                      
        \u001b[36md8\u001b[0mY88b\u001b[36mY88b                        d8\u001b[0m888  \u001b[36mY8\u001b[0m888                      
        \u001b[36mY88\u001b[0m"Y888b.   888  888 88888b.d88b.\u001b[36m88\u001b[0m888  \u001b[36m888\u001b[0m     .d88b.  88888b.d88b.  
         \u001b[36m“Y888\u001b[0m"Y88b\u001b[36m88\u001b[0m888\u001b[36m88\u001b[0m888\u001b[36m8\u001b[0m888\u001b[36mb\u001b[0m"888\u001b[36mb\u001b[0m"88b\u001b[36m8\u001b[0m888        \u001b[36m.\u001b[0md88""88b\u001b[36m8\u001b[0m888\u001b[36mb\u001b[0m"888\u001b[36mb\u001b[0m"88b 
            \u001b[36m“Y88\u001b[0m"888\u001b[36m8\u001b[0m888\u001b[36m88\u001b[0m888\u001b[36m8\u001b[0m888\u001b[36m88\u001b[0m888\u001b[36m88\u001b[0m888\u001b[36m8\u001b[0m888    888\u001b[36md8\u001b[0m888\u001b[36m88\u001b[0m888\u001b[36m8\u001b[0m888\u001b[36m88\u001b[0m888\u001b[36m88\u001b[0m888 
          Y88b\u001b[36m”8\u001b[0md88P\u001b[36m8\u001b[0mY88b\u001b[36m8\u001b[0m888\u001b[36m8\u001b[0m888\u001b[36m88\u001b[0m888\u001b[36m88\u001b[0m888\u001b[36m8\u001b[0mY88b\u001b[36m 8\u001b[0md88P\u001b[36m88\u001b[0mY88..88P\u001b[36m8\u001b[0m888\u001b[36m88\u001b[0m888\u001b[36m88\u001b[0m888 
        \u001b[36mY88\u001b[0m"Y8888P"\u001b[36mY88\u001b[0m"Y88888\u001b[36m8\u001b[0m888\u001b[36m88\u001b[0m888\u001b[36m88\u001b[0m888\u001b[36m88\u001b[0m"Y8888P" \u001b[36mY88\u001b[0m"Y88P"\u001b[36m88\u001b[0m888\u001b[36m88\u001b[0m888\u001b[36m88\u001b[0m888 
        \u001b[36m“Y8888p”   “Y8888\u001b[0m888\u001b[36m88  888  888   “Y8888P”    “Y88P”  888  888  888                
                    \u001b[0mY8b d88P                                             
                  \u001b[36mY8b\u001b[0m"Y88P" 
                    \u001b[36m“Y88P’ \u001b[0m

        Press Enter to Start
        """)
        time.sleep(.25)
        print (u"""
           .d8888b.                          .d8888b.                       
        \u001b[36m.d\u001b[0md88P\u001b[36mb.\u001b[0mY88b                      \u001b[36m.d\u001b[0md88P\u001b[36m8b\u001b[0mY88b                      
        \u001b[36md8\u001b[0mY88b\u001b[36mY88b                        d8\u001b[0m888  \u001b[36mY8\u001b[0m888                      
        \u001b[36mY88\u001b[0m"Y888b.   888  888 88888b.d88b.\u001b[36m88\u001b[0m888  \u001b[36m888\u001b[0m     .d88b.  88888b.d88b.  
         \u001b[36m“Y888\u001b[0m"Y88b\u001b[36m88\u001b[0m888\u001b[36m88\u001b[0m888\u001b[36m8\u001b[0m888\u001b[36mb\u001b[0m"888\u001b[36mb\u001b[0m"88b\u001b[36m8\u001b[0m888        \u001b[36m.\u001b[0md88""88b\u001b[36m8\u001b[0m888\u001b[36mb\u001b[0m"888\u001b[36mb\u001b[0m"88b 
            \u001b[36m“Y88\u001b[0m"888\u001b[36m8\u001b[0m888\u001b[36m88\u001b[0m888\u001b[36m8\u001b[0m888\u001b[36m88\u001b[0m888\u001b[36m88\u001b[0m888\u001b[36m8\u001b[0m888    888\u001b[36md8\u001b[0m888\u001b[36m88\u001b[0m888\u001b[36m8\u001b[0m888\u001b[36m88\u001b[0m888\u001b[36m88\u001b[0m888 
          Y88b\u001b[36m”8\u001b[0md88P\u001b[36m8\u001b[0mY88b\u001b[36m8\u001b[0m888\u001b[36m8\u001b[0m888\u001b[36m88\u001b[0m888\u001b[36m88\u001b[0m888\u001b[36m8\u001b[0mY88b\u001b[36m 8\u001b[0md88P\u001b[36m88\u001b[0mY88..88P\u001b[36m8\u001b[0m888\u001b[36m88\u001b[0m888\u001b[36m88\u001b[0m888 
        \u001b[36mY88\u001b[0m"Y8888P"\u001b[36mY88\u001b[0m"Y88888\u001b[36m8\u001b[0m888\u001b[36m88\u001b[0m888\u001b[36m88\u001b[0m888\u001b[36m88\u001b[0m"Y8888P" \u001b[36mY88\u001b[0m"Y88P"\u001b[36m88\u001b[0m888\u001b[36m88\u001b[0m888\u001b[36m88\u001b[0m888 
        \u001b[36m“Y8888p”   “Y8888\u001b[0m888\u001b[36m88  888  888   “Y8888P”    “Y88P”  888  888  888                
                    \u001b[0mY8b d88P                                             
                  \u001b[36mY8b\u001b[0m"Y88P" 
                    \u001b[36m“Y88P’ \u001b[0m


        """)
        time.sleep(.25)
        clear()
        print (u"""
           .d8888b.                          .d8888b.                       
        \u001b[36m.d\u001b[0md88P\u001b[36mb.\u001b[0mY88b                      \u001b[36m.d\u001b[0md88P\u001b[36m8b\u001b[0mY88b                      
        \u001b[36md8\u001b[0mY88b\u001b[36mY88b                        d8\u001b[0m888  \u001b[36mY8\u001b[0m888                      
        \u001b[36mY88\u001b[0m"Y888b.   888  888 88888b.d88b.\u001b[36m88\u001b[0m888  \u001b[36m888\u001b[0m     .d88b.  88888b.d88b.  
         \u001b[36m“Y888\u001b[0m"Y88b\u001b[36m88\u001b[0m888\u001b[36m88\u001b[0m888\u001b[36m8\u001b[0m888\u001b[36mb\u001b[0m"888\u001b[36mb\u001b[0m"88b\u001b[36m8\u001b[0m888        \u001b[36m.\u001b[0md88""88b\u001b[36m8\u001b[0m888\u001b[36mb\u001b[0m"888\u001b[36mb\u001b[0m"88b 
            \u001b[36m“Y88\u001b[0m"888\u001b[36m8\u001b[0m888\u001b[36m88\u001b[0m888\u001b[36m8\u001b[0m888\u001b[36m88\u001b[0m888\u001b[36m88\u001b[0m888\u001b[36m8\u001b[0m888    888\u001b[36md8\u001b[0m888\u001b[36m88\u001b[0m888\u001b[36m8\u001b[0m888\u001b[36m88\u001b[0m888\u001b[36m88\u001b[0m888 
          Y88b\u001b[36m”8\u001b[0md88P\u001b[36m8\u001b[0mY88b\u001b[36m8\u001b[0m888\u001b[36m8\u001b[0m888\u001b[36m88\u001b[0m888\u001b[36m88\u001b[0m888\u001b[36m8\u001b[0mY88b\u001b[36m 8\u001b[0md88P\u001b[36m88\u001b[0mY88..88P\u001b[36m8\u001b[0m888\u001b[36m88\u001b[0m888\u001b[36m88\u001b[0m888 
        \u001b[36mY88\u001b[0m"Y8888P"\u001b[36mY88\u001b[0m"Y88888\u001b[36m8\u001b[0m888\u001b[36m88\u001b[0m888\u001b[36m88\u001b[0m888\u001b[36m88\u001b[0m"Y8888P" \u001b[36mY88\u001b[0m"Y88P"\u001b[36m88\u001b[0m888\u001b[36m88\u001b[0m888\u001b[36m88\u001b[0m888 
        \u001b[36m“Y8888p”   “Y8888\u001b[0m888\u001b[36m88  888  888   “Y8888P”    “Y88P”  888  888  888                
                    \u001b[0mY8b d88P                                             
                  \u001b[36mY8b\u001b[0m"Y88P" 
                    \u001b[36m“Y88P’ \u001b[0m

        Press Enter to Start
        """)
        time.sleep(.25)
        print (u"""
           .d8888b.                          .d8888b.                       
        \u001b[36m.d\u001b[0md88P\u001b[36mb.\u001b[0mY88b                      \u001b[36m.d\u001b[0md88P\u001b[36m8b\u001b[0mY88b                      
        \u001b[36md8\u001b[0mY88b\u001b[36mY88b                        d8\u001b[0m888  \u001b[36mY8\u001b[0m888                      
        \u001b[36mY88\u001b[0m"Y888b.   888  888 88888b.d88b.\u001b[36m88\u001b[0m888  \u001b[36m888\u001b[0m     .d88b.  88888b.d88b.  
         \u001b[36m“Y888\u001b[0m"Y88b\u001b[36m88\u001b[0m888\u001b[36m88\u001b[0m888\u001b[36m8\u001b[0m888\u001b[36mb\u001b[0m"888\u001b[36mb\u001b[0m"88b\u001b[36m8\u001b[0m888        \u001b[36m.\u001b[0md88""88b\u001b[36m8\u001b[0m888\u001b[36mb\u001b[0m"888\u001b[36mb\u001b[0m"88b 
            \u001b[36m“Y88\u001b[0m"888\u001b[36m8\u001b[0m888\u001b[36m88\u001b[0m888\u001b[36m8\u001b[0m888\u001b[36m88\u001b[0m888\u001b[36m88\u001b[0m888\u001b[36m8\u001b[0m888    888\u001b[36md8\u001b[0m888\u001b[36m88\u001b[0m888\u001b[36m8\u001b[0m888\u001b[36m88\u001b[0m888\u001b[36m88\u001b[0m888 
          Y88b\u001b[36m”8\u001b[0md88P\u001b[36m8\u001b[0mY88b\u001b[36m8\u001b[0m888\u001b[36m8\u001b[0m888\u001b[36m88\u001b[0m888\u001b[36m88\u001b[0m888\u001b[36m8\u001b[0mY88b\u001b[36m 8\u001b[0md88P\u001b[36m88\u001b[0mY88..88P\u001b[36m8\u001b[0m888\u001b[36m88\u001b[0m888\u001b[36m88\u001b[0m888 
        \u001b[36mY88\u001b[0m"Y8888P"\u001b[36mY88\u001b[0m"Y88888\u001b[36m8\u001b[0m888\u001b[36m88\u001b[0m888\u001b[36m88\u001b[0m888\u001b[36m88\u001b[0m"Y8888P" \u001b[36mY88\u001b[0m"Y88P"\u001b[36m88\u001b[0m888\u001b[36m88\u001b[0m888\u001b[36m88\u001b[0m888 
        \u001b[36m“Y8888p”   “Y8888\u001b[0m888\u001b[36m88  888  888   “Y8888P”    “Y88P”  888  888  888                
                    \u001b[0mY8b d88P                                             
                  \u001b[36mY8b\u001b[0m"Y88P" 
                    \u001b[36m“Y88P’ \u001b[0m


        """)
        time.sleep(.25)
        clear()
        print (u"""
           .d8888b.                          .d8888b.                       
        \u001b[35m.d\u001b[0md88P\u001b[35mb.\u001b[0mY88b                      \u001b[35m.d\u001b[0md88P\u001b[35m8b\u001b[0mY88b                      
        \u001b[35md8\u001b[0mY88b\u001b[35mY88b                        d8\u001b[0m888  \u001b[35mY8\u001b[0m888                      
        \u001b[35mY88\u001b[0m"Y888b.   888  888 88888b.d88b.\u001b[35m88\u001b[0m888  \u001b[35m888\u001b[0m     .d88b.  88888b.d88b.  
         \u001b[35m“Y888\u001b[0m"Y88b\u001b[35m88\u001b[0m888\u001b[35m88\u001b[0m888\u001b[35m8\u001b[0m888\u001b[35mb\u001b[0m"888\u001b[35mb\u001b[0m"88b\u001b[35m8\u001b[0m888        \u001b[35m.\u001b[0md88""88b\u001b[35m8\u001b[0m888\u001b[35mb\u001b[0m"888\u001b[35mb\u001b[0m"88b 
            \u001b[35m“Y88\u001b[0m"888\u001b[35m8\u001b[0m888\u001b[35m88\u001b[0m888\u001b[35m8\u001b[0m888\u001b[35m88\u001b[0m888\u001b[35m88\u001b[0m888\u001b[35m8\u001b[0m888    888\u001b[35md8\u001b[0m888\u001b[35m88\u001b[0m888\u001b[35m8\u001b[0m888\u001b[35m88\u001b[0m888\u001b[35m88\u001b[0m888 
          Y88b\u001b[35m”8\u001b[0md88P\u001b[35m8\u001b[0mY88b\u001b[35m8\u001b[0m888\u001b[35m8\u001b[0m888\u001b[35m88\u001b[0m888\u001b[35m88\u001b[0m888\u001b[35m8\u001b[0mY88b\u001b[35m 8\u001b[0md88P\u001b[35m88\u001b[0mY88..88P\u001b[35m8\u001b[0m888\u001b[35m88\u001b[0m888\u001b[35m88\u001b[0m888 
        \u001b[35mY88\u001b[0m"Y8888P"\u001b[35mY88\u001b[0m"Y88888\u001b[35m8\u001b[0m888\u001b[35m88\u001b[0m888\u001b[35m88\u001b[0m888\u001b[35m88\u001b[0m"Y8888P" \u001b[35mY88\u001b[0m"Y88P"\u001b[35m88\u001b[0m888\u001b[35m88\u001b[0m888\u001b[35m88\u001b[0m888 
        \u001b[35m“Y8888p”   “Y8888\u001b[0m888\u001b[35m88  888  888   “Y8888P”    “Y88P”  888  888  888                
                    \u001b[0mY8b d88P                                             
                  \u001b[35mY8b\u001b[0m"Y88P" 
                    \u001b[35m“Y88P’ \u001b[0m

        Press Enter to Start
        """)
        time.sleep(.25)
        clear()
        print (u"""
           .d8888b.                          .d8888b.                       
        \u001b[35m.d\u001b[0md88P\u001b[35mb.\u001b[0mY88b                      \u001b[35m.d\u001b[0md88P\u001b[35m8b\u001b[0mY88b                      
        \u001b[35md8\u001b[0mY88b\u001b[35mY88b                        d8\u001b[0m888  \u001b[35mY8\u001b[0m888                      
        \u001b[35mY88\u001b[0m"Y888b.   888  888 88888b.d88b.\u001b[35m88\u001b[0m888  \u001b[35m888\u001b[0m     .d88b.  88888b.d88b.  
         \u001b[35m“Y888\u001b[0m"Y88b\u001b[35m88\u001b[0m888\u001b[35m88\u001b[0m888\u001b[35m8\u001b[0m888\u001b[35mb\u001b[0m"888\u001b[35mb\u001b[0m"88b\u001b[35m8\u001b[0m888        \u001b[35m.\u001b[0md88""88b\u001b[35m8\u001b[0m888\u001b[35mb\u001b[0m"888\u001b[35mb\u001b[0m"88b 
            \u001b[35m“Y88\u001b[0m"888\u001b[35m8\u001b[0m888\u001b[35m88\u001b[0m888\u001b[35m8\u001b[0m888\u001b[35m88\u001b[0m888\u001b[35m88\u001b[0m888\u001b[35m8\u001b[0m888    888\u001b[35md8\u001b[0m888\u001b[35m88\u001b[0m888\u001b[35m8\u001b[0m888\u001b[35m88\u001b[0m888\u001b[35m88\u001b[0m888 
          Y88b\u001b[35m”8\u001b[0md88P\u001b[35m8\u001b[0mY88b\u001b[35m8\u001b[0m888\u001b[35m8\u001b[0m888\u001b[35m88\u001b[0m888\u001b[35m88\u001b[0m888\u001b[35m8\u001b[0mY88b\u001b[35m 8\u001b[0md88P\u001b[35m88\u001b[0mY88..88P\u001b[35m8\u001b[0m888\u001b[35m88\u001b[0m888\u001b[35m88\u001b[0m888 
        \u001b[35mY88\u001b[0m"Y8888P"\u001b[35mY88\u001b[0m"Y88888\u001b[35m8\u001b[0m888\u001b[35m88\u001b[0m888\u001b[35m88\u001b[0m888\u001b[35m88\u001b[0m"Y8888P" \u001b[35mY88\u001b[0m"Y88P"\u001b[35m88\u001b[0m888\u001b[35m88\u001b[0m888\u001b[35m88\u001b[0m888 
        \u001b[35m“Y8888p”   “Y8888\u001b[0m888\u001b[35m88  888  888   “Y8888P”    “Y88P”  888  888  888                
                    \u001b[0mY8b d88P                                             
                  \u001b[35mY8b\u001b[0m"Y88P" 
                    \u001b[35m“Y88P’ \u001b[0m


        """)
        time.sleep(.25)
        clear()
        print (u"""
           .d8888b.                          .d8888b.                       
        \u001b[35m.d\u001b[0md88P\u001b[35mb.\u001b[0mY88b                      \u001b[35m.d\u001b[0md88P\u001b[35m8b\u001b[0mY88b                      
        \u001b[35md8\u001b[0mY88b\u001b[35mY88b                        d8\u001b[0m888  \u001b[35mY8\u001b[0m888                      
        \u001b[35mY88\u001b[0m"Y888b.   888  888 88888b.d88b.\u001b[35m88\u001b[0m888  \u001b[35m888\u001b[0m     .d88b.  88888b.d88b.  
         \u001b[35m“Y888\u001b[0m"Y88b\u001b[35m88\u001b[0m888\u001b[35m88\u001b[0m888\u001b[35m8\u001b[0m888\u001b[35mb\u001b[0m"888\u001b[35mb\u001b[0m"88b\u001b[35m8\u001b[0m888        \u001b[35m.\u001b[0md88""88b\u001b[35m8\u001b[0m888\u001b[35mb\u001b[0m"888\u001b[35mb\u001b[0m"88b 
            \u001b[35m“Y88\u001b[0m"888\u001b[35m8\u001b[0m888\u001b[35m88\u001b[0m888\u001b[35m8\u001b[0m888\u001b[35m88\u001b[0m888\u001b[35m88\u001b[0m888\u001b[35m8\u001b[0m888    888\u001b[35md8\u001b[0m888\u001b[35m88\u001b[0m888\u001b[35m8\u001b[0m888\u001b[35m88\u001b[0m888\u001b[35m88\u001b[0m888 
          Y88b\u001b[35m”8\u001b[0md88P\u001b[35m8\u001b[0mY88b\u001b[35m8\u001b[0m888\u001b[35m8\u001b[0m888\u001b[35m88\u001b[0m888\u001b[35m88\u001b[0m888\u001b[35m8\u001b[0mY88b\u001b[35m 8\u001b[0md88P\u001b[35m88\u001b[0mY88..88P\u001b[35m8\u001b[0m888\u001b[35m88\u001b[0m888\u001b[35m88\u001b[0m888 
        \u001b[35mY88\u001b[0m"Y8888P"\u001b[35mY88\u001b[0m"Y88888\u001b[35m8\u001b[0m888\u001b[35m88\u001b[0m888\u001b[35m88\u001b[0m888\u001b[35m88\u001b[0m"Y8888P" \u001b[35mY88\u001b[0m"Y88P"\u001b[35m88\u001b[0m888\u001b[35m88\u001b[0m888\u001b[35m88\u001b[0m888 
        \u001b[35m“Y8888p”   “Y8888\u001b[0m888\u001b[35m88  888  888   “Y8888P”    “Y88P”  888  888  888                
                    \u001b[0mY8b d88P                                             
                  \u001b[35mY8b\u001b[0m"Y88P" 
                    \u001b[35m“Y88P’ \u001b[0m

        Press Enter to Start
        """)
        time.sleep(.25)
        clear()
        print (u"""
           .d8888b.                          .d8888b.                       
        \u001b[35m.d\u001b[0md88P\u001b[35mb.\u001b[0mY88b                      \u001b[35m.d\u001b[0md88P\u001b[35m8b\u001b[0mY88b                      
        \u001b[35md8\u001b[0mY88b\u001b[35mY88b                        d8\u001b[0m888  \u001b[35mY8\u001b[0m888                      
        \u001b[35mY88\u001b[0m"Y888b.   888  888 88888b.d88b.\u001b[35m88\u001b[0m888  \u001b[35m888\u001b[0m     .d88b.  88888b.d88b.  
         \u001b[35m“Y888\u001b[0m"Y88b\u001b[35m88\u001b[0m888\u001b[35m88\u001b[0m888\u001b[35m8\u001b[0m888\u001b[35mb\u001b[0m"888\u001b[35mb\u001b[0m"88b\u001b[35m8\u001b[0m888        \u001b[35m.\u001b[0md88""88b\u001b[35m8\u001b[0m888\u001b[35mb\u001b[0m"888\u001b[35mb\u001b[0m"88b 
            \u001b[35m“Y88\u001b[0m"888\u001b[35m8\u001b[0m888\u001b[35m88\u001b[0m888\u001b[35m8\u001b[0m888\u001b[35m88\u001b[0m888\u001b[35m88\u001b[0m888\u001b[35m8\u001b[0m888    888\u001b[35md8\u001b[0m888\u001b[35m88\u001b[0m888\u001b[35m8\u001b[0m888\u001b[35m88\u001b[0m888\u001b[35m88\u001b[0m888 
          Y88b\u001b[35m”8\u001b[0md88P\u001b[35m8\u001b[0mY88b\u001b[35m8\u001b[0m888\u001b[35m8\u001b[0m888\u001b[35m88\u001b[0m888\u001b[35m88\u001b[0m888\u001b[35m8\u001b[0mY88b\u001b[35m 8\u001b[0md88P\u001b[35m88\u001b[0mY88..88P\u001b[35m8\u001b[0m888\u001b[35m88\u001b[0m888\u001b[35m88\u001b[0m888 
        \u001b[35mY88\u001b[0m"Y8888P"\u001b[35mY88\u001b[0m"Y88888\u001b[35m8\u001b[0m888\u001b[35m88\u001b[0m888\u001b[35m88\u001b[0m888\u001b[35m88\u001b[0m"Y8888P" \u001b[35mY88\u001b[0m"Y88P"\u001b[35m88\u001b[0m888\u001b[35m88\u001b[0m888\u001b[35m88\u001b[0m888 
        \u001b[35m“Y8888p”   “Y8888\u001b[0m888\u001b[35m88  888  888   “Y8888P”    “Y88P”  888  888  888                
                    \u001b[0mY8b d88P                                             
                  \u001b[35mY8b\u001b[0m"Y88P" 
                    \u001b[35m“Y88P’ \u001b[0m


        """)
        clear()
        if not flag:### Inserting my code here
            ###  Difficulty Selector, the number you pick add to your stats, but if you add more than 10, it will remove 10 point from your stats as a punishment, there is 1 exception
            clear()
            print("Select Difficulty")
            while True:
                try:
                    difficulty = int(input('Easier 10-0 Harder: '))
                    break
                except ValueError:
                    print("Please input integer only...")  
                    continue
            if difficulty == 69: ### Difficulty Exception
               print('I like your style, have fun :D')
            elif difficulty > 10:
                difficulty = -10
                print("""
                You tried to cheat and make the game easier for yourself, 
                so now I will punish you by making it harder
                """)

            time.sleep(1)
                        ### Starting Stat Generator
                        ### Starting stats are pseudo-randomly generated plus the difficulty number
            random.seed()
            affinity = "Affinity: " + str(affi + difficulty)
            print(affinity +
"""

This is your affinity with SymCom
When this stat reaches 100 just type 'done' and you win, but if you have less than a 100 you lose
""")
            time.sleep(1)
            intelligence = "Intelligence: " + str(intelli + difficulty)
            print(intelligence + 
"""
The higher this stat, the easier it is to lie to SymCom
""")
            time.sleep(1)
            charisma = "Charisma: " + str(charis + difficulty)
            print(charisma
+ """
The higher this stat, the faster will you gain affinity with SymCom
""")
            input('press enter to continue\n')

            clear()

            ###  intro convo with the chatbot.

            print("This is your anti-virus")
            username = input(str("Anti-Virus: Your hard drive is corrupted, may I know your name? "))
            input('press enter to continue\n')
            print("Anti-Virus: muahahaha, " + username + " I've fooled you, im not your Anti-Virus, im actually...")
            time.sleep(1)
            print("Not-your-antivrus: SymCom!!!!")
            time.sleep(1)
            print("SymCom: I've infected your computer, all your base are belong to me!!! >:)c")
            time.sleep(.5)
            print("SymCom: Nothing can Stop me!!!!")
            time.sleep(.5)
            print("[Virus Quarantined]")
            input('press enter to continue\n')
            print("From what you can tell, that was an AI, pretending to be a virus, your current anti-virus can only hold it back for three days")
            time.sleep(.5)
            print("SymCom: I don't know what tricks you used " + username + "thaniel! but even though i've been incapacitated, I will infect this computer and you can't stop me!! ")
            input('press enter to continue\n')
            print("you have an Idea, if you keep speaking to SymCom you may be able to convince them to leave you alone or become friends with them")
            input('press enter to continue\n')

            clear()
            print("START")
            print('"lie" and "friend" are your two choices, if you add a 2 or a 3 at the end, you get more points, but if your stats' + " aren't high enough you will lose affinity with symcom")
            input('press enter to continue\n')
            clear()


            ### chatbot function
            intellis = int(intelli + difficulty)
            affis = int(affi + difficulty)
            chariss = int(charis + difficulty)
            def get_bot_response(user_response):
                nonlocal affis
                nonlocal chariss
                nonlocal intellis

                bot_response_trick = ["SymCom: Are you telling me you can charge your phone in the microwave? [DO NOT DO THIS]","SymCom: Silly Im in a computer I can't pull your finger.","SymCom: If I had a mask of my own face, Imagine all the things I could do.. WHY ARE YOU RIPPING YOUR FACE OFF?!?!?!?"]
                bot_response_trick2 = ["SymCom: You mean to tell me the earth is flat?[ITS NOT]","SymCom: Wait if the next statement is true, and the previous statement is false? [Rebooting]", "Wait so the sky, isn't really blue?, and the roses aren't red? What about the grass? Its not green?"]
                bot_response_trick3 = ["SymCom: Wait System 32 is a virus that slows down a computer, I should delete that, only I can infect this computer [Rebooting] [DO NOT DO THIS]","SymCom: If I click on https://www.youtube.com/watch?v=dQw4w9WgXcQ, I can watch free movies? [its a rickroll]","SymCom: Updog? What's UpDog?"]
                bot_response_friend = ["Oh you think im cool? Tell me more!!!","Wow thats a really cool wig you have, last night I had a dream that I had a really cool wig, if only I could remember what the [Redacted] it looked like","Woah this band 'Queen' seems really cool thanks for showing me their songs!"]
                bot_response_friend2 = ["SymCom: Oh you like to play [insert fave game here] too? Thats really cool!","What you had a psychic vision? you know my name? HOW DID YOU KNOW ITS SYMCOM!!! :o ",""]
                bot_response_friend3 = ["SymCom: Wow will you really read my 250 page fanfiction on [insert popular thing]","SymCom:  ;-; Some jerk on the internet said some mean things to me. What? Really? A drop of vanilla behind each ear and I'll smell like a cookie all day? Wow this is life changing, thank you","SymCom: You wrote a song about me? I wanna listen :D ... WOW, that part where it goes 'burger fries on a dashboard underneath the burning hot sun' , I- I felt that"]

                bot_response_tfailure = "Failed to trick SymBot, you feel five points less smart now"
                bot_response_tfailure2 = """
SymBot is so dumbfounded thinking you could trick him like that,
he has hacked into your school, and deleted all records of you attendance there, have fun at kindergarden tomorrow :D
you are now 20 points less smart now"""

                bot_response_ffailure = "SymBot is not impressed, you feel your charisma fade away by 5 points"
                bot_response_ffailure2 = """
SymBot didn't like that, he managed to secretly sent a message to all your loved ones,
they have disowned you, your last name is now Null, oh yeah you lost 20 charisma btw"""


                ### Here is where stats matter, you will either succeed if your stats are high enough you get a funny line and some points
                ### if you fail, you lose everything
                if user_response == "lie":
                    intellis += 2
                    affis += 2
                    return choice(bot_response_trick)
                elif user_response == "lie2":
                    if intellis > 20:
                        intellis += 5
                        affis += 5
                        return choice(bot_response_trick2)
                    else:
                        intellis -= 5
                        affis -= 5
                        return bot_response_tfailure
                elif user_response == "lie3":
                    if intellis > 50:
                        intellis += 20
                        affis += 20
                        return choice(bot_response_trick3)
                    else:
                        intellis -= 20
                        affis -= 20
                        return bot_response_tfailure2
                elif user_response == "friend":
                    chariss += 2
                    affis += 2
                    return choice(bot_response_friend)
                elif user_response == "friend2":
                    if chariss > 20:
                        chariss += 5
                        affis += 5
                        return choice(bot_response_friend2)
                    else:
                        chariss -= 5
                        affis -= 5
                        return bot_response_ffailure
                elif user_response == "friend3":
                    if chariss > 50:
                        chariss += 20
                        affis += 20
                        return choice(bot_response_friend3)
                    else:
                        chariss -= 20
                        affis -= 20
                        return bot_response_ffailure2
                elif user_response == "affinity":
                    return affis
                elif user_response == "charisma":
                    return chariss
                elif user_response == "intelligence":
                    return intellis
                else:
                    print("Really?")

                ### user chatbot interaction

                user_response = ""

            while True:
                user_response = input('''

Will you "lie" to SymCom? or become his "friend", 
you might also want to check the stats "affinity" "charisma" "intelligence",maybe affinity reach 100 and you are "done" :

''')


                if user_response == 'done':
                    break
                clear()
                bot_response = get_bot_response(user_response)
                print(

bot_response)
                


            if affis >= 100:
                if chariss > intellis:
                        print("You've become friends with SymCom, because of that he will continue living on your computer, but will use his AI powers to help you, this is the good ending champ!")
                else:
                        print("After finding out everything you told SymCom was a lie, SymCom doesn't know whats real anymore, he didn't do anything after that, and eventually he stopped thinking, this is the opposite of a good ending, you monster, lying hurts people you know?")
            else:
                print("You didn't reach 100 affinity with SymCom, he won't Sympathize with you, when he eats your ram, slows down your gaming computer, or send your 'homework' folder to your proffessor, you could have tried harder, just type 'friend' a few times, then 'friend2' once you had 21 charisma, and then 'friend3', when you had 51 charisma, its easy as that.")

                


def get_input():
    global flag
    input('\n')
    #thread doesn't continue until key is pressed
    flag=False

n=threading.Thread(target=normal)
i=threading.Thread(target=get_input)
n.start()
i.start()
### end of borrowed code



