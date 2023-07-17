import time

def stopwatch():
    start_time = time.time()
    print("Stopwatch started. Press ENTER to stop.")
    input()
    elapsed_time = time.time() - start_time
    print("Elapsed time: {:.2f} seconds".format(elapsed_time))

stopwatch()