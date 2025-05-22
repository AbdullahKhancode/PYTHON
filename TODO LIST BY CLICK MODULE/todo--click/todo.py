# import click
# import os 
# import json

# TODO_FILE="todo.json"


# def load_tasks():
#     if not os.path.exists(TODO_FILE):
#         return[]
#     with open(TODO_FILE,'r')as file:
#             return json.load(file)

# def save_tasks(tasks):
#     with open(TODO_FILE,'w')as file:
#         json.dump(tasks,file,indent=4)

# @click.group()
# def cli():
#     """simple todo list manage"""
#     pass
# @click.argument("task")
# def add(task):
#     tasks=load_tasks()
#     tasks.append({"task":task,"done":False})
#     save_tasks(tasks)
#     click.echo(f"task added successfully:{task}")
    
# @click.command()
# def list():
#     """list all the task"""
#     tasks=load_tasks()
#     if not tasks:
#         click.echo("no task found")
#         return
#     for index, task in enumerate(tasks ,1):
#         click.echo(f"{index}. [{'✅' if task['done'] else '❌'}] {task['task']}")

# @click.command()
# @click.argument("task_number",type=int)
# def complete(task_number):
#     """mark the task as completed"""
#     tasks = load_tasks()
#     if 0< task_number <=len(tasks):
#         tasks[task_number-1]['done']=True
#         save_tasks(tasks)
#     else:
#         click.echo(f"Invalid task number:{task_number}")
# @click.command()
# @click.argument("task_number",type=int)
# def remove(task_number):
#     """Removea task from the list"""
#     tasks=load_tasks()
#     if 0< task_number<=len(tasks): 
#         removed_task =tasks.pop(task_number-1)
#         save_tasks(tasks)
#         click.echo(f"Remove task:{removed_task['task']}")

#     else:
#         click.echo(f"Invalid task number")


# cli.add_command(add)
# cli.add_command(list)
# cli.add_command(complete)
# cli.add_command(remove)
# if __name__=="__main__":
#      cli() 


import click
import os
import json

TODO_FILE = "todo.json"

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, 'r') as file:
        return json.load(file)

def save_tasks(tasks):
    with open(TODO_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

@click.group()
def cli():
    """Simple To-Do list manager."""
    pass

@click.command()
@click.argument("task")
def add(task):
    """Add a new task to the list."""
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    click.echo(f"Task added successfully: {task}")

@click.command(name="list")
def list_tasks():
    """List all tasks."""
    tasks = load_tasks()
    if not tasks:
        click.echo("No tasks found.")
        return
    for index, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "❌"
        click.echo(f"{index}. [{status}] {task['task']}")

@click.command()
@click.argument("task_number", type=int)
def complete(task_number):
    """Mark a task as completed."""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["done"] = True
        save_tasks(tasks)
        click.echo(f"Marked task #{task_number} as complete.")
    else:
        click.echo(f"Invalid task number: {task_number}")

@click.command()
@click.argument("task_number", type=int)
def remove(task_number):
    """Remove a task from the list."""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        click.echo(f"Removed task: {removed_task['task']}")
    else:
        click.echo("Invalid task number.")

# Register commands
cli.add_command(add)
cli.add_command(list_tasks)
cli.add_command(complete)
cli.add_command(remove)

if __name__ == "__main__":
    cli()
