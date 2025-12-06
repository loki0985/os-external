import os 

def child(pipeout):
    os.write(pipeout, b"Hello from child process!\n")
    os.close(pipeout)

def parent():
    pipein, pipeout = os.pipe()
    pid = os.fork()

    if pid == 0:
        os.close(pipein)
        child(pipeout)

    else:
        os.close(pipeout)
        msg = os.read(pipein, 1024)
        print ("Parent received:", msg.decode())
        os.close(pipein)

if __name__== "__main__":
    parent()    