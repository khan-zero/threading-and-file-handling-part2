import threading
import os

def ct_numbers(fn):
    count = 0
    with open(fn, "r") as file:
        for i in file.read():
            if i.isnumeric():
                count += 1
    print(f"count of numbers in {fn}: {count}")

def main():
    threads = []
    for i in os.listdir():
        t = threading.Thread(target=ct_numbers, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("Program was ended")

if __name__ == "__main__":
    main()

