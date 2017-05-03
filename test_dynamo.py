from taskpop import dynamo
from datetime import datetime

username = 'lauritzen@gmail.com'

dynamo.tasks_create(username, 'Keir', 'Lauritzen')
print(dynamo.tasks_get(username))
#print(dynamo._tasks_get_next_task_num('ishaan@gmail.com'))
#dynamo._tasks_delete('ishaan@gmail.com')

dynamo._tasks_update_new_task(username)
print(dynamo.tasks_get(username))
print()
dynamo._tasks_update_remove_task(username,1)
print(dynamo.tasks_get(username))

task = {
    'ud_priority': 3,
    'ud_time': 2,
    'deadline': datetime.utcnow().isoformat(),
    'item': 'Dummy test',
    'description': 'Dummy test description'
}

dynamo.task_new(username, task)
print(dynamo.tasks_get(username))
print(dynamo.task_get(username,2))

task = {
    'ud_priority': 3,
    'ud_time': 3,
    'deadline': datetime.utcnow().isoformat(),
    'item': 'Dummy test',
    'description': 'Dummy test description'
}

dynamo.task_update(username,2,task)
print(dynamo.task_get(username,2))

task = {
    'ud_priority': 4,
    'ud_time': 3,
    'deadline': datetime.utcnow().isoformat(),
    'item': 'Dummy test',
    'description': 'Dummy test description'
}

dynamo.task_update(username,2,task)
print(dynamo.task_get(username,2))

dynamo.task_remove(username,2)
print(dynamo.tasks_get(username))

task_higher = {
    'ud_priority': 3,
    'ud_time': 3,
    'deadline': datetime.utcnow().isoformat(),
    'item': 'Dummy test',
    'description': 'Dummy test description'
}

higher_task_id = dynamo.task_new(username, task_higher)

task_lower = {
    'ud_priority': 2,
    'ud_time': 3,
    'deadline': datetime.utcnow().isoformat(),
    'item': 'Dummy test',
    'description': 'Dummy test description'
}

lower_task_id = dynamo.task_new(username, task_lower)

task_middle = {
    'ud_priority': 2,
    'ud_time': 3,
    'deadline': datetime.utcnow().isoformat(),
    'item': 'Dummy test',
    'description': 'Dummy test description'
}

task_id = dynamo.task_new(username, task_middle)

dynamo.task_update_priority(username, task_id, higher_task_id, lower_task_id)
print()
print(dynamo.task_get(username,task_id))

dynamo.task_archive(username, task_id, 3)
print(dynamo.tasks_get(username))
print(dynamo.taskarchive_get(username))


