from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import datetime

def validate_upload_date(value):
    value=value.replace(tzinfo=None)
    if value.date() < datetime.now().date():
        raise ValidationError(
            _('%(value)s should not be a past date'),
            params={'value': value},
        )


