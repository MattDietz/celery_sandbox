import sandbox


@sandbox.app.task
def add(x, y):
    return x + y
