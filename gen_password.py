from string import ascii_letters, ascii_lowercase, ascii_uppercase, digits
from random import choice
chars = ascii_letters + digits

def pd(n):
	return ''.join(choice(chars) for _ in range(n))

print(pd(14))
