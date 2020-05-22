'''
23May - @ilanchezhian
'''
#celery -A task worker --pool=solo --loglevel=info
import time
from celery import Celery

app = Celery('task',
             backend='redis://0.0.0.0',
             broker= "redis://0.0.0.0")

@app.task()
def task():
    '''
    this is Asyncio task
    :return None:
    '''
    print("started task and sleep for 4 secs")
    time.sleep(4)
    print("completed")

