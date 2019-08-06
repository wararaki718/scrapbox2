## ref: http://ja.pymotw.com/2/multiprocessing/communication.html
import logging
import multiprocessing
import time
import sys


# logger settings
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s : %(levelname)s : %(message)s'
)
logger = logging.getLogger(__name__)


class Consumer(multiprocessing.Process):
    def __init__(self, task_queue, result_queue):
        multiprocessing.Process.__init__(self)
        self.task_queue = task_queue
        self.result_queue = result_queue

    def run(self):
        proc_name = self.name
        logger.info(f'start : run method.({proc_name})')

        while True:
            next_task = self.task_queue.get()
            if not next_task:
                logger.info(f'{proc_name} is end.')
                self.task_queue.task_done()
                break
            
            logger.info(f'{proc_name}: {next_task}')
            answer = next_task()
            self.task_queue.task_done()
            self.result_queue.put(answer)

        logger.info(f'finish: run method.({proc_name})')
        return


class Task:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        time.sleep(0.1)
        return f'{self.a} * {self.b} = {self.a * self.b}'

    def __str__(self):
        return f'{self.a} * {self.b}'


def main():
    tasks = multiprocessing.JoinableQueue()
    results = multiprocessing.Queue()

    # create worker instances
    num_consumers = multiprocessing.cpu_count() * 2
    logger.info(f'creating {num_consumers} consumers')
    consumers = [
        Consumer(tasks, results)
        for i in range(num_consumers)
    ]

    # start workers.
    for consumer in consumers: # consumer: worker
        consumer.start()
    logger.info('all consumer are ready.')

    # add jobs in queues.
    num_jobs = 10
    for i in range(num_jobs):
        tasks.put(Task(i, i))
    logger.info(f'created {num_jobs} jobs.')

    # add poison pill for each consumer
    # "poison pill" is used to stop the workers
    for i in range(num_jobs):
        tasks.put(None)
    logger.info('stoped workers.')
    
    # show all results
    for i in range(num_jobs):
        result = results.get()
        logger.info(f'result: {result}')

    for consumer in consumers:
        consumer.join()
    logger.info('finish all tasks.')
    logger.info('done.')

    return 0


if __name__ == '__main__':
    sys.exit(main())
