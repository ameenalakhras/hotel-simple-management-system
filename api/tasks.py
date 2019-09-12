# import random
# from celery.decorators import task
#
# @task(name="sum_two_numbers")
# def add(x, y):
#     return x + y
#
# @task(name="multiply_two_numbers")
# def mul(x, y):
#     total = x * (y * random.randint(3, 100))
#     return total
#
# @task(name="sum_list_numbers")
# def xsum(numbers):
#     return sum(numbers)


from celery.decorators import task


@task(name="add_two_numbers")
def add(x, y):
    print(f'x: {x}, y: {y}')
    return x + y
