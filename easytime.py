"""easytime - The simplest python time library ever written."""


from datetime import datetime
from dateutil import tz


def now(timezone='UTC'):
    """Return the current datetime, in the specified timezone.

    Usage::

        >>> from easytime import now
        >>> time_utc = now()
        2012-11-17 23:16:16.252081+00:00
        >>> time_la = now('America/Los_Angeles')
        2012-11-17 15:16:16.252357-08:00
        >>> time_chicago = now('America/Chicago')
        2012-11-17 17:16:16.252664-06:00
        >>> time_berlin = now('Europe/Berlin')
        2012-11-18 00:16:16.253005+01:00

    :param str timezone: The timezone to output the current time in. Defaults to
        'UTC'. You can find a full list of available timezones at:
        http://en.wikipedia.org/wiki/List_of_tz_database_time_zones
    :rtype: datetime
    :returns: A python datetime object, with the correct current local time of
        the given timezone.
    """
    return datetime.utcnow().replace(tzinfo=tz.gettz('UTC')).astimezone(tz.gettz(timezone))
