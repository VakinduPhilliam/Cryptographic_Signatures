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
# Protecting complex data structures.
# If you wish to protect a list, tuple or dictionary you can do so using the signing module’s dumps and loads functions.
# These imitate Python’s pickle module, but use JSON serialization under the hood.
# JSON ensures that even if your SECRET_KEY is stolen an attacker will not be able to execute arbitrary commands by exploiting the pickle format:
#

from django.core import signing

value = signing.dumps({"foo": "bar"})
value

# OUTPUT: 'eyJmb28iOiJiYXIifQ:1NMg1b:zGcDE4-TCkaeGzLeW9UQwZesciI'

signing.loads(value)

# OUTPUT: '{'foo': 'bar'}'

#
# Because of the nature of JSON (there is no native distinction between lists and tuples) if you pass in a tuple, you will get a list 
# from 'signing.loads(object)':

from django.core import signing

value = signing.dumps(('a','b','c'))
signing.loads(value)

# OUTPUT: '['a', 'b', 'c']'

#
# dumps(obj, key=None, salt=’django.core.signing’, compress=False):
# Returns URL-safe, sha1 signed base64 compressed JSON string. Serialized object is signed using TimestampSigner.
#
# loads(string, key=None, salt=’django.core.signing’, max_age=None):
# Reverse of dumps(), raises BadSignature if signature fails. Checks max_age (in seconds) if given.
#
