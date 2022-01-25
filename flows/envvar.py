import os

from prefect import Flow
from prefect.run_config.kubernetes import KubernetesRun
from prefect.storage import Git

with Flow("envvar") as flow:
    flow.storage = Git(
        repo_host="github.com",
        repo="briansorahan/prefect-playground",
        flow_path="flows/envvar.py",
    )
    foo = os.getenv("FOO", "MISSING")
    print(f"FOO env var = {foo}")
