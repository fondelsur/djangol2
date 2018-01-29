# -*- coding: utf-8 -*-

from management.models import Characters
import base64
import hashlib


# We use the clause .using of the DJango ORM to select a database amongst
# the existent ones.

def encrypt_l2_password(password):
    """Encrypt a password using the L2 internal password."""
    first_threshold = hashlib.sha1(password).digest()
    encrypted_pass = base64.b64encode(first_threshold)
    return encrypted_pass


def get_top_level_players():
    """Return the highest level players."""
    # Returning only the first 5 occurences.
    return Characters.objects.using(
        'l2server'
    ).filter(accesslevel=0).order_by('-level').values('char_name', 'level')[:5]


def get_top_pk_players():
    """Return the highest level pk players."""
    # We return only the first 5 occurences.
    return Characters.objects.using(
        'l2server'
    ).filter(
        accesslevel=0
    ).order_by('-pkkills').values('char_name', 'pkkills')[:5]
    
