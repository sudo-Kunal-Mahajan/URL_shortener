import random
import string

def generate_new_shortened_url():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k = 10))    