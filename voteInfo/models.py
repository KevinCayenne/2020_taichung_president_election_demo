from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField

class Dept(models.Model):
    dept_code = models.IntegerField(verbose_name = _('行政區代碼'))
    dept_name = models.CharField(verbose_name = _('行政區名稱'), max_length = 200)

    def __str__(self):
        return self.dept_name

    class Meta:
        verbose_name = _('行政區')
        verbose_name_plural = _('行政區')
