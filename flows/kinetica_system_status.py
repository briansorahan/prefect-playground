import gpudb

from prefect import Flow, Parameter, task
from prefect.run_configs.kubernetes import KubernetesRun
from prefect.storage import Git


@task
def show_system_status(host, username, password):
    conn = gpudb.GPUdb(
        host=host,
        username=username,
        password=password,
    )
    system_status = conn.show_system_status()
    print(f"system_status: {system_status}")
    for item in system_status.items():
        print(item)


with Flow(name="kinetica_system_status") as flow:
    flow.storage = Git(
        repo_host="github.com",
        repo="briansorahan/prefect-playground",
        flow_path="flows/kinetica_system_status.py",
        branch_name="master",
    )
    flow.run_config = KubernetesRun(
        image="devprismcr.azurecr.io/acuity/prefect/flows:0.0.70",
    )
    username = Parameter("username")
    password = Parameter("password")
    host = Parameter("host")
    show_system_status(host, username, password)
