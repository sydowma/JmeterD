from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.conf import settings

CESHI = settings.CESHI_ENVIRONMENT
ONLINE = settings.ONLINE_ENVIRONMENT

ENVIRONMENT_OPTIONS = (CESHI, ONLINE,)


def validate_environment(value):
    if value not in ENVIRONMENT_OPTIONS:
        raise ValidationError(
            _('%(value)s 错误的环境id'),
            params={'value': value},
        )


UNIXTIME_LENGTH = 10


def validate_unixtime(value):
    """
    验证数字位数
    """
    f = len(str(value))
    if f != UNIXTIME_LENGTH:
        raise ValidationError(
            _('%(value)s 错误的时间'),
            params={'value': value}
        )
