from prefect import Flow, Parameter, Task, task


@task
def list_task(l):
    return l


class MyTask(Task):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self, databricks_host, jar_params=None):
        self.logger.info(f"databricks_host = {databricks_host}")
        self.logger.info(f"jar_params      = {jar_params}")


with Flow(name="trigger_failed") as flow:
    databricks_host = Parameter("databricks_host", default="foo")
    data_root = Parameter("data_root", default="bar")
    my_task = MyTask()
    my_task(databricks_host, jar_params=list_task(["--dataRoot", data_root]))
