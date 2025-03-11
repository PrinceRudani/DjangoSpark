from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from django.utils.timezone import now
from product.models import ProductVO
from utils.my_logger import get_logger

logger = get_logger()


@receiver(post_save, sender=ProductVO)
def product_saved(sender, instance, created, **kwargs):

    if instance.is_deleted:
        return  # Avoid logging it as a save if it's a delete action

    log_data = {
        "signal": "post_save",
        "sender": sender.__name__,
        "product_id": instance.product_id,
        "product_name": instance.product_name,
        "action": "Created" if created else "Updated",
    }
    print(log_data)
    logger.info(f"Signal Triggered: {log_data}")


@receiver(pre_save, sender=ProductVO)
def product_deleted(sender, instance, **kwargs):
    """Only trigger when the product is physically deleted"""
    if instance.is_deleted:  # Ignore if it was just a soft delete
        log_data = {
            "signal": "soft_delete",
            "sender": sender.__name__,
            "product_id": instance.product_id,
            "product_name": instance.product_name,
            "action": "Soft Deleted",
        }
        print(log_data)
        logger.info(f"Signal Triggered: {log_data}")
