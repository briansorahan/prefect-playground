import os

from prefect import Flow, Task
from prefect.run_configs.kubernetes import KubernetesRun
from prefect.storage import Git


class EnvVarTask(Task):
    def __init__(self, msg, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._msg = msg

    def run(self):
        self.logger.info(self._msg)


with Flow("envvar") as flow:
    branch_name = os.getenv("GITHUB_BRANCH_NAME", "master")

    flow.storage = Git(
        repo_host="github.com",
        repo="briansorahan/prefect-playground",
        flow_path="flows/envvar.py",
        branch_name=branch_name,
    )
    flow.run_config = KubernetesRun(
        image="devprismcr.azurecr.io/acuity/prefect/flows:0.0.47",
    )
    evt = EnvVarTask("hello from a branch")
    flow.add_task(evt)
