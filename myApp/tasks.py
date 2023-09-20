import random
from celery import shared_task
import time

@shared_task(bind=True)
def test_func(self):
    for i in range(10):
        print(i)
        time.sleep(2)
        self.update_state(state='PROGRESS',
                          meta={'current': i, 'total': 10})
    print('Task completed')
    return {'current': 100, 'total': 100, }

@shared_task
def add(x, y):
    # Celery recognizes this as the `myApp.tasks.add` task
    # the name is purposefully omitted here.
    return x + y

@shared_task(name="multiply_two_numbers")
def mul(x, y):
    # Celery recognizes this as the `multiple_two_numbers` task
    total = x * (y * random.randint(3, 100))
    return total

@shared_task(name="sum_list_numbers")
def xsum(numbers):
    # Celery recognizes this as the `sum_list_numbers` task
    return sum(numbers)
