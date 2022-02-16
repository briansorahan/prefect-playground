from prefect import Flow, Task


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
    a = A()
    b = B()
    a_result = a()
    b_result = b(a_result)
