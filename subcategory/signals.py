from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from django.utils.timezone import now
from subcategory.models import SubCategoryVO
from utils.my_logger import get_logger

logger = get_logger()

@receiver(post_save, sender=SubCategoryVO)
def post_save_subcategory(sender, instance, created, **kwargs):
    if instance.is_deleted:
        return
    log_data = {
        "signal": "post_save",
        "sender": instance.__class__.__name__,
        "instance": instance,
        "subcategory_id": instance.subcategory_id,
        "subcategory_name": instance.subcategory_name,
        "action": "Created" if created else "Updated",
    }
    logger.info(f"Signal Triggered: {log_data}")

@receiver(pre_save, sender=SubCategoryVO)
def subcategory_deleted(sender, instance, **kwargs):
    if instance.is_deleted:
        log_data = {
            "signal": "soft_delete",
            "sender": sender.__name__,
            "product_id": instance.subcategory_id,
            "product_name": instance.subcategory_name,
            "action": "Soft Deleted",
        }
        logger.info(f"Signal Triggered: {log_data}")