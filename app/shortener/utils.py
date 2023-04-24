import os
from random import choice
from string import ascii_lowercase, digits


# Available chars (total 36): [a-z0-9]
AVAILABLE_CHARS = ascii_lowercase + digits

# Default short code size
SHORT_CODE_SIZE = int(os.environ.get('SHORT_CODE_SIZE', default=7))

# List of forbidden words for short codes
FORBIDDEN_SHORT_CODES = os.environ.get('FORBIDDEN_SHORT_CODES', default='').split(' ')


def create_random_string(chars=AVAILABLE_CHARS, size=SHORT_CODE_SIZE):
    """
    Creates a random string with the predetermined size.
    :param chars: a string of available characters.
    :param size: length of generated string.
    :return: a random string with the predetermined size.
    """
    return ''.join([choice(chars) for _ in range(size)])
