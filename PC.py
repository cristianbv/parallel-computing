from multiprocessing import Pool
from pi import pi
import time

data = range(1000, 3000)

for i in range(1, 5):
    start_time = time.time()
    pool = Pool(processes=i)  # quantity of workers
    results = pool.map(pi, data)
    print '{} seconds with {} pools'.format(round((time.time() - start_time), 3), i)
