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
# Signature Altering.
# If the signature or value have been altered in any way, a django.core.signing.BadSignature exception will be raised:
#

from django.core import signing

value += 'm'

try:
    original = signer.unsign(value)

    except signing.BadSignature:

    print("Tampering detected!")
