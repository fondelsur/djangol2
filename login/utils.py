from management.models import Characters


def get_top_level_players():
    """Return the highest level players."""
    return Characters.objects.using('l2server').filter(accesslevel=0).order_by('-level').values('char_name', 'level')[:5]


def get_top_pk_players():
    """Return the highest level pk players."""
    return Characters.objects.using('l2server').filter(accesslevel=0).order_by('-pkkills').values('char_name', 'pkkills')[:5]
