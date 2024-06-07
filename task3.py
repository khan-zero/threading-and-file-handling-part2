import threading
import os

def ct_words(fn):
    with open(fn, "r") as file:
        count = len(file.read().split())

    print(f"count of words in {fn}: {count}")

def main():
    threads = []
    for i in os.listdir():
        t = threading.Thread(target=ct_words, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("Program was ended")

if __name__ == "__main__":
    main()

