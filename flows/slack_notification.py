from prefect import Flow, task
from prefect.tasks.notifications.slack_task import SlackTask


@task
def foo():
    SlackTask(message={"foo": "bar"})


with Flow(name="slack_notification") as flow:
    foo_task = foo()
