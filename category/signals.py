from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils.timezone import now
from utils.my_logger import get_logger
from .models import CategoryVO

logger = get_logger()


# Signal triggered after saving a category
@receiver(post_save, sender=CategoryVO)
def category_saved(sender, instance, created, **kwargs):
    if instance.is_deleted:
        return  # Avoid logging it as a save if it's a delete action

    log_data = {
        "signal": "post_save",
        "sender": sender.__name__,
        "category_id": instance.category_id,
        "category_name": instance.category_name,
        "category_description": instance.category_description,
        "is_deleted": instance.is_deleted,
        "timestamp": now().isoformat(),
        "action": "Created" if created else "Updated",
    }
    logger.info(f"Signal Triggered: {log_data}")


# Signal triggered after deleting a category
@receiver(pre_save, sender=CategoryVO)
def category_soft_deleted(sender, instance, **kwargs):
    if instance.is_deleted:
        log_data = {
            "signal": "soft_delete",
            "sender": sender.__name__,
            "category_id": instance.category_id,
            "category_name": instance.category_name,
            "category_description": instance.category_description,
            "is_deleted": instance.is_deleted,
            "timestamp": now().isoformat(),
            "action": "Soft Deleted",
        }
        logger.info(f"Signal Triggered: {log_data}")