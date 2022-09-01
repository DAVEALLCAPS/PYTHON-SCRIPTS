import string
import secrets
import pyperclip

my_symbols = '!@#$%^&'

characters_allowed = string.ascii_letters + string.digits + my_symbols

my_password = ''.join(secrets.choice(characters_allowed) for i in range(50))

pyperclip.copy(my_password)
