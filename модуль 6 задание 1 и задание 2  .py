import time
from threading import Thread
from datetime import datetime
def start_gamefootbal(number):
    time.sleep(1)
    print(f'Gamefootbal № {number} started!')
for i in range(5):
  start_gamefootbal( i + 1 )

threads = [Thread(target=start_gamefootbal(1),args = (i +  1 )) for i in range(5)]
time1 = time.time()
for t in threads:
	t.start()
	t.join()
print(f'Время последовательного выполнения: {time.time()-time1}')

threads = [Thread(target = start_gamefootbal(2),args = (i +  1  )) for i in range(5)]
time1 = time.time()
for t in threads:
	t.start()
for t in threads:
	t.join()
print(f'Время параллельного выполнения: {time.time()-time1}')





