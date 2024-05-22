from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem

@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """ 
    Update otder total on lineitem update/create
    """

    instance.order.update.total()

@receiver(post_delete, sender=OrderLineItem)
def update_on_save(sender, instance, **kwargs):
    """ 
    Update otder total on lineitem delete
    """

    instance.order.update.total()