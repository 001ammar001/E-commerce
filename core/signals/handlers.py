from django.dispatch import receiver
from store.signals import order_created,proudcts_sold

@receiver(order_created)
def on_order_created(sender, **kwargs):
  print(kwargs['order'])

@receiver(proudcts_sold)
def on_proudcts_sold(sender,**kwargs):
  items = kwargs['proudcts'] 
  for item in items:
    if item.inventory < 25:
      print('less than')