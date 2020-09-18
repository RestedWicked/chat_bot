from random import choice #### Random module
from os import system ### OS module, Used here for animation
import time ### Time module
import threading ### Multi Threading baby :D

clear = lambda: system('clear') ### Prepares Terminal for next frame

clear() ### Program Starts Here

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
flag = 1

def normal():
    global flag
    while flag==1:
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
        if flag==False:
            clear()
            print('it works')

def get_input():
    global flag
    keystrk=input('\n')
    #thread doesn't continue until key is pressed
    print('You pressed: ', keystrk)
    flag=False
    print('flag is now:', flag)

n=threading.Thread(target=normal)
i=threading.Thread(target=get_input)
n.start()
i.start()
