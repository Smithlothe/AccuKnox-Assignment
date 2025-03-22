# Question 2: Do Django signals run in the same thread as the caller?
# Answer: Yes, Django signals run in the same thread by default.

import threading
from django.dispatch import Signal, receiver

my_signal = Signal()

@receiver(my_signal)
def my_receiver(sender, **kwargs):
    print(f"Receiver running in thread: {threading.current_thread().name}")

print(f"Caller running in thread: {threading.current_thread().name}")
my_signal.send(sender=None)