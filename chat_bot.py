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
The higher this stat, the easier it is to trick SymCom
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
            print('"trick" and "friend" are your two choices, if you add a 2 or a 3 at the end, you get more points, but if your stats' + " aren't high enough you will lose affinity with symcom")
            time.sleep(1)
            clear()


            ### chatbot function
            intellis = int(intelli + difficulty)
            affis = int(affi + difficulty)
            chariss = int(charis + difficulty)
            def get_bot_response(user_response):
                nonlocal affis
                nonlocal chariss
                nonlocal intellis

                bot_response_trick = ["Hello"]
                bot_response_trick2 = ["You"]
                bot_response_trick3 = ["Are"]
                bot_response_friend = ["Really"]
                bot_response_friend2 = ["Mega"]
                bot_response_friend3 = ["Cool"]

                bot_response_tfailure = "Failed to trick SymBot, you feel five points less smart now"
                bot_response_tfailure2 = """
SymBot is so dumbfounded thinking you could trick him like that,
he has hacked into your school, and deleted all records of you attendance there, have fun at kindergarden tomorrow :D
you are now 20 points less smart now"""

                bot_response_ffailure = "SymBot is not impressed, you feel your charisma fade away by 5 points"
                bot_response_ffailure2 = """
SymBot didn't like that, he managed to secretly send a message to all your loved ones,
they have disowned you, your last name is now Null, oh yeah you lost 20 charisma btw"""


                ### Here is where stats matter, you will either succeed if your stats are high enough you get a funny line and some points
                ### if you fail, you lose everything
                if user_response == "trick":
                    intellis += 2
                    affis += 2
                    return choice(bot_response_trick)
                elif user_response == "trick2":
                    if intellis > 20:
                        intellis += 5
                        affis += 5
                        return choice(bot_response_trick2)
                    else:
                        intellis -= 5
                        affis -= 5
                        return bot_response_tfailure
                elif user_response == "trick3":
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
                user_response = input('''Will you "trick" SymCom? or become his "friend", 
you might also want to check the stats "affinity" "charisma" "intelligence",maybe affinity reach 100 and you are "done" : ''')


                if user_response == 'done':
                    break

                
                bot_response = get_bot_response(user_response)
                print(bot_response)


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



