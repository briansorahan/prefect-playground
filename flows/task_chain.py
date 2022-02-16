from prefect import Flow, Task
from prefect.run_configs.kubernetes import KubernetesRun
from prefect.storage import Git


class A(Task):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self):
        print("run task A")
        return "foo"


class B(Task):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self, s):
        print(f"run task B with s={s}")


with Flow(name="task_chain") as flow:
    flow.storage = Git(
        repo_host="github.com",
        repo="briansorahan/prefect-playground",
        flow_path="flows/task_chain.py",
        branch_name="master",
    )
    flow.run_config = KubernetesRun(
        image="devprismcr.azurecr.io/acuity/prefect/flows:0.0.70",
    )
    a = A()
    b = B()
    a_result = a()
    b_result = b(a_result)
