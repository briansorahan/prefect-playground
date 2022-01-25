import os

from prefect import Flow

with Flow("envvar") as flow:
    foo = os.getenv("FOO", "MISSING")
    print(f"FOO env var = {foo}")
