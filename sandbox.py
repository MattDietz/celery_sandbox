from __future__ import absolute_import

import celery

# broker is for sending
# backend is for receiving.
app = celery.Celery("sandbox", broker="amqp://", backend="amqp://",
                    include=["tasks"])

app.conf.update(CELERY_TASK_RESULT_EXPIRES=3600,
                CELERY_TASK_SERIALIZER="json",
                CELERY_ACCEPT_CONTENT=["json"])

if __name__ == "__main__":
    # This makes a worker process.
    # If you open a python interpreter and import "tasks"
    # you get an interface to the worker.
    #
    # Calling the task:
    # tasks.add(3, 4) -> calls the function as normal, returning a value
    #
    # Sending the request to the worker:
    # >>> tasks.add.delay(3, 4) # sends a message over AMQP to the worker
    #                           # and returns an AsyncResult
    # <AsyncResult: 3c978565-acae-4af9-9d99-4edc571dd5dd>
    # >>> r = tasks.add.delay(3, 4)
    # >>> r.ready()
    # True
    # >>> r.get()  # Accepts numerous values including a timeout to handle
    #              # waiting for you
    #
    # Awesome!
    app.start()
