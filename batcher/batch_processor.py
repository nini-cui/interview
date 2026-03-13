import threading, time
import concurrent.futures
from typing import List, Any, Callable

class BatcherProcessor:
    """
    Triggers:
        1. batch size
        2. batch interval

    Considerations:
        1. multithreading
            1.1 lock
        2. tests: different test cases

    Best Practices:
    1. docstring - what does this function do, list all the inputs and outpts variables
    2. backoff retry
    3. validate the data, raise erroer if needed

    Functions:
        1. class: BatcherProcessor
        2. add_items()
        3. trigger on batch size
        4. trigger on timeout - start up a different thread
        3. pass batch_processor() to this class
        4. stop() - threading event
    """
    def __init__(
            self,
            batch_size: int=3,
            batch_interval: float=3.0,
            batch_processor: Callable[[List[Any]], None]=None,
            max_worker: int=4
        ):

        self.batch_size = batch_size
        self.batch_interval = batch_interval
        self.batch_processor = batch_processor
        self.max_worker = max_worker

        self._executor = concurrent.futures.ThreadPoolExecutor(max_workers=self.max_worker)
        self._current_batch = []
        self._last_process_time = time.time()
        self._lock = threading.Lock()
        self._event = threading.Event()

        # flusher thread
                              

        # value validation
        if self.batch_size <= 0:
            raise ValueError("batch size cannot be less than 0")
        if self.batch_interval <= 0:
            raise ValueError("batch interval cannot be less than 0")
        # more checking goes here

    def add_items(self, item):
        with self._lock:
            self._current_batch.append(item)

            if len(self._current_batch) >= self.batch_size:
                self._process_batch()
                
    def _process_batch(self):
        batch = self._current_batch
        self._current_batch = []
        self._last_process_time = time.time()
        self._executor.submit(self.batch_processor, batch)

    def _process_on_timeout(self):
        while not self._event.is_set():
            with self._lock:
                if self._current_batch and (time.time() - self._last_process_time >= self.batch_interval):
                    self._process_batch()

    def stop(self):
        self._event.set()
        self._fluser_thread.join()
        with self._lock:
            if self._current_batch:
                self._process_batch()

if __name__ == "__main__":
    def batch_processor(items):
        print("processing task {} on thread {}".format(items, threading.current_thread().name))
        time.sleep(2)

    batcher = BatcherProcessor(
        batch_processor=batch_processor
    )

    batcher.add_items(1)
    batcher.add_items(2)
    batcher.add_items(3)
    # time.sleep(2)
    # batcher.add_items(4)
    # time.sleep(1.5)

