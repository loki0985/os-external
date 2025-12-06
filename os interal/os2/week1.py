import os 
import time
import sys

#1.fork() to create a child process
print ("Before fork, PID:", os.getpid())
pid = os.fork()

if pid == 0:
    print("child process PID:", os.getpid(), " Parent PID:", os.getppid())
    os._exit(0)  # Exit child process
else:
    print("parent process PID:", os.getpid(), " Child PID:", pid)

    #2.wait()
    finished_pid, status = os.wait()
    print("parent waited.child ", finished_pid, " exited with status ", status)

    #3.execv() to replace the process image
    print("\n-- Using execv to replace process image --")
    if os.fork() == 0:
        os.execlp("ls", "ls", "-l")  # Replace child process with 'ls -l'
    else:
        os.wait()  # Wait for the 'ls' command to finish

    #4.exit()
 #os._exit(0)  # Exit parent process
    #5.getpid() and getppid()
    print("Final Parent PID:", os.getpid())

    #6.getuid() and getgid()
    print("current ID:", os.getuid())
    
    #7.setuid() and setgid()
    # Note: Changing UID/GID requires appropriate permissions and is system dependent.
    # Uncomment the following lines only if you have the necessary permissions.
    # new_uid = 1000  # Example UID

    # os.setuid(new_uid)
    # print("New UID:", os.getuid())

    #8.brkk() and sbrk()
    # Note: Python does not provide direct access to brk() and sbrk()
    mem = bytearray(1024 * 1024)  # Allocate 1MB
    print ("simulated brk by allocating memory of size:", len(mem))

    #9. nice()
    print("old nice value:", os.nice(0))
    os.nice(5)  # Increase nice value by 5
    print("new nice value:", os.nice(0))

    #10.sleep()
    print("Sleeping for 2 seconds...")
    time.sleep(2)
    print("Woke up!")