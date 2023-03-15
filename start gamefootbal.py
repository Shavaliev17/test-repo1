import time
from threading import Thread

def start_gamefootbal(number):
    time.sleep(1)
    print(f'Gamefootbal № {number} started!')

threads = [Thread(target = start_gamefootbal, args = (i + 1, )) for i in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()

    



