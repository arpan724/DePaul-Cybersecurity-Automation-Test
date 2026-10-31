##### Week 7- Rsyslog/Log Parsing- Homework #####
##### CSEC-380/480 - Arpan Panchal ####

'''
Part 1: Write a Python function that sends syslog messages (1.5 Points)
'''
import socket
import time 

def send_syslog(filename, host, protocol):

    port = 514

    # 
    if protocol =="UDP":
        so= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    elif protocol =="TCP":
        so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        so.connect((host,port))    
    
    else:
        print("Protocol is not valid")
        return
    
    # File Open: 
    with open(filename, "r") as file:  
        # read File:
        for line in file: 
            Message = line.strip() 

            if protocol == "UDP":
                so.sendto(Message.encode(),(host,port))

            elif protocol == "TCP":
                so.sendall((Message + "\n").encode())

            print ("Sent :", Message)

            # sleep time
            time.sleep(1)        
    so.close()

send_syslog('system2.log','192.168.1.101','UDP')

