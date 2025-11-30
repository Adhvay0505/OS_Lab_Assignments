# task3_ipc_fork_pipe.py
# Demonstrates fork(), pipe(), IPC in Python (Linux only)

import os
import sys

def main():
    # Create pipe: returns (read_end, write_end)
    read_fd, write_fd = os.pipe()
    
    pid = os.fork()

    if pid < 0:
        print("Fork failed!")
        sys.exit(1)

    elif pid > 0:  # Parent process
        print(f"Parent Process (PID: {os.getpid()})")
        os.close(read_fd)  # Close unused read end
        
        message = "Greetings from Parent Process!"
        os.write(write_fd, message.encode())
        print(f"Parent sent: {message}")
        
        os.close(write_fd)
        os.wait()  # Wait for child to finish
        print("Parent: Child has terminated.")

    else:  # Child process
        print(f"Child Process (PID: {os.getpid()})")
        os.close(write_fd)  # Close unused write end
        
        received = os.read(read_fd, 1024)
        decoded_msg = received.decode()
        print(f"Child received: {decoded_msg}")
        
        os.close(read_fd)
        print("Child process exiting.")
        sys.exit(0)

if __name__ == "__main__":
    print("=== Fork + Pipe IPC Demo ===\n")
    main()
