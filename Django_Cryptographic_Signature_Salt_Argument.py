# Python/Django Cryptographic signing
# Django provides both a low-level API for signing values and a high-level API for setting and reading signed cookies,
# one of the most common uses of signing in Web applications.
#
# Protecting the SECRET_KEY
# When you create a new Django project using startproject, the settings.py file is generated automatically
# and gets a random SECRET_KEY value. This value is the key to securing signed data – it is vital you keep this secure,
# or attackers could use it to generate their own signed values.
#

#
# Using the salt argument
# If you do not wish for every occurrence of a particular string to have the same signature hash, you can use the optional
# salt argument to the Signer class. 
# Using a salt will seed the signing hash function with both the salt and your SECRET_KEY:
#

signer = Signer()

signer.sign('My string')

# OUTPUT: 'My string:GdMGD6HNQ_qdgxYP8yBZAdAIV1w'

signer = Signer(salt='extra')
signer.sign('My string')

# OUTPUT: 'My string:Ee7vGi-ING6n02gkcJ-QLHg6vFw'

signer.unsign('My string:Ee7vGi-ING6n02gkcJ-QLHg6vFw')

# OUTPUT: 'My string'

#
# Using salt in this way puts the different signatures into different namespaces. 
# A signature that comes from one namespace (a particular salt value) cannot be used to validate the same plaintext string in a different namespace that
# is using a different salt setting.
# The result is to prevent an attacker from using a signed string generated in one place in the code as input to another piece of code that is generating
# (and verifying) signatures using a different salt.
# Unlike your SECRET_KEY, your salt argument does not need to stay secret.
#
