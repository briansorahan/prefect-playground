from prefect import Flow, Parameter, Task


class Parameterized(Task):
    def __init__(self, s=None):
        self._s = s

    def run(self):
        self.logger.info(f"self._s = {self._s}")


with Flow(name="parameterized") as flow:
    s = Parameter("s", default="foo")
    p = Parameterized(s=s)
