# Question 3: Do Django signals run in the same database transaction as the caller?
# Answer: Yes, by default, Django signals run in the same transaction.

from django.db import transaction, models
from django.dispatch import Signal, receiver

my_signal = Signal()

class MyModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(my_signal)
def my_receiver(sender, **kwargs):
    print("Creating a MyModel instance within the receiver...")
    MyModel.objects.create(name="Test")

with transaction.atomic():
    print("Sending signal within a transaction...")
    my_signal.send(sender=None)
    print("Signal sent within the transaction.")