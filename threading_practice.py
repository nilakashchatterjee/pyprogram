import threading
import time

def increase_by_10():
    for i in range(1, 11):
        print(f"Thread {threading.current_thread().name}: {i}0% complete")

# Create two threads
thread1 = threading.Thread(target=increase_by_10, name="Thread-1")
thread2 = threading.Thread(target=increase_by_10, name="Thread-2")

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("Both threads have finished completely.")
