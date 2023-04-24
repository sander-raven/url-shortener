from django.conf import settings
from django.db import models

from shortener.utils import create_random_string, FORBIDDEN_SHORT_CODES


class ShortURL(models.Model):
    original_url = models.URLField("original url")
    short_code = models.CharField("short code", max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="short_urls",
        null=True,
        verbose_name="owner",
    )
    number_of_transitions = models.PositiveIntegerField(
        "number of transitions",
        default=0,
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.short_code} for {self.original_url}'

    def save(self, *args, **kwargs):
        if not self.short_code:
            new_short_code = ''
            short_codes = [''] + FORBIDDEN_SHORT_CODES
            while new_short_code in short_codes:
                new_short_code = create_random_string()
                short_codes = self.__class__.objects.values_list(
                    'short_code', flat=True
                )
            self.short_code = new_short_code
        super().save(*args, **kwargs)

    def increase_number_of_transitions(self):
        self.number_of_transitions = models.F('number_of_transitions') + 1
        self.save()
