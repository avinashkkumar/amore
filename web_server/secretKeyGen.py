# Use this file to generate secret key and replace the secret key in the .env if needed to do so 
from django.core.management.utils import get_random_secret_key
x = get_random_secret_key()
print(x)