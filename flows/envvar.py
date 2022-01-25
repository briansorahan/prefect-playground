import os

from prefect import Flow
from prefect.run_configs.kubernetes import KubernetesRun
from prefect.storage import Git

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
    foo = os.getenv("FOO with new feature", "MISSING")
    print(f"FOO env var = {foo}")
