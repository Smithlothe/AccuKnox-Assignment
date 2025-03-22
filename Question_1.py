# Question 1: Are Django signals executed synchronously or asynchronously?
# Answer: By default, Django signals are executed synchronously.

from django.dispatch import Signal, receiver

my_signal = Signal()

@receiver(my_signal)
def my_receiver(sender, **kwargs):
    print("Signal received!")

print("Sending signal...")
my_signal.send(sender=None)
print("Signal sent.")