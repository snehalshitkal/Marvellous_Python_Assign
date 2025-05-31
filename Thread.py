'''
    program starts 3 thread.
    Each printing number from 1 to 5 with delay of 1 sec
    use Threading.thread.
'''
import threading
import time


def Display():
    print("Inside thread")
    for i in range(1,6):
        print(threading.current_thread().name,i)
        time.sleep(1)

def main():
    print("Inside Main:")
    threades = []
    for i in range(3):
        thread = threading.Thread(target = Display)
        thread.start()

    for thread in threades:
        thread.join()
    print("All Thread Finish:")

if __name__ == "__main__":
    main()