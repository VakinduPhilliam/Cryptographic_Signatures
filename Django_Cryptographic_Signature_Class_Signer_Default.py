# Python/Django Cryptographic signing.
# Django provides both a low-level API for signing values and a high-level API for setting and reading signed cookies,
# one of the most common uses of signing in Web applications.
#
# Protecting the SECRET_KEY.
# When you create a new Django project using startproject, the settings.py file is generated automatically
# and gets a random SECRET_KEY value. This value is the key to securing signed data – it is vital you keep this secure,
# or attackers could use it to generate their own signed values.
#

#
# By default, the Signer class uses the SECRET_KEY setting to generate signatures. 
# You can use a different secret by passing it to the Signer constructor:

signer = Signer('my-other-secret')

value = signer.sign('My string')
value

# OUTPUT: 'My string:EkfQJafvGyiofrdGnuthdxImIJw'

#
# class Signer(key=None, sep=’:’, salt=None).
# Returns a signer which uses key to generate signatures and sep to separate values. 
# 'sep' cannot be in the URL safe base64 alphabet. 
# This alphabet contains alphanumeric characters, hyphens, and underscores.
#
