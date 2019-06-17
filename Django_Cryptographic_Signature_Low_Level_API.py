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
# Using the low-level API.
# Django’s signing methods live in the django.core.signing module.
# To sign a value, first instantiate a Signer instance:
#

from django.core.signing import Signer

signer = Signer()

value = signer.sign('My string')
value

# OUTPUT: 'My string:GdMGD6HNQ_qdgxYP8yBZAdAIV1w'


#
# The signature is appended to the end of the string, following the colon. You can retrieve the original value using the
# unsign method:
#

original = signer.unsign(value)
original

# OUTPUT: 'My string'