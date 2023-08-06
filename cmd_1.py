import os
import subprocess

def start_command_os(command):

    stream = os.popen(command)
    return stream.read()


def start_command_sub(command):
    process = subprocess.Popen(command.split(" "),
                        stdout=subprocess.PIPE, 
                        stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    # return process.communicate()
    
    return(stdout.decode() + stderr.decode())
    

def read_signature():
    process = subprocess.Popen(["avrdude","-c", "usbasp", "-p", "m32"],stderr=subprocess.PIPE, stdout=subprocess.PIPE)

    stdout, stderr = process.communicate()
    # return process.communicate()
    
    return(stdout.decode() + stderr.decode())