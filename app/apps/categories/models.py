from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=125)
    slug = models.SlugField(max_length=125, unique=True)
    is_active = models.BooleanField(default=False)
    parent = TreeForeignKey(
        "self", on_delete=models.PROTECT, related_name="children", null=True, blank=True
    )

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        ordering = ["name"]
        verbose_name_plural = _("categories")

