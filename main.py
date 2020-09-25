import names
import namegenerator as namegen
import secrets
import string

user = names.get_full_name()
prof = namegen.gen()
alphabet = string.ascii_letters + string.digits
password = ''.join(secrets.choice(alphabet) for i in range(16))

print('Nombres: ', user, '\nUsername: ', prof, '\nPassword: ', password)
