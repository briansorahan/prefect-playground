from prefect import Flow, task
from prefect.run_configs.kubernetes import KubernetesRun
from prefect.storage import Git
from prefect.tasks.notifications.slack_task import SlackTask


@task
def foo():
    SlackTask(message={"foo": "bar"})


with Flow(name="slack_notification") as flow:
    flow.storage = Git(
        repo_host="github.com",
        repo="briansorahan/prefect-playground",
        flow_path="flows/slack_notification.py",
        branch_name="master",
    )
    flow.run_config = KubernetesRun(
        image="devprismcr.azurecr.io/acuity/prefect/flows:0.0.69",
    )
    foo_task = foo()
