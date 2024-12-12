from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Document

is_graph_built = False  # Global flag to track graph status

@receiver([post_save, post_delete], sender=Document)
def reset_graph_flag(sender, instance, **kwargs):
    global is_graph_built
    is_graph_built = False  # Reset the flag when documents change
