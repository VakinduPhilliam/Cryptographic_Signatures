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
# Verifying timestamped values
# TimestampSigner is a subclass of Signer that appends a signed timestamp to the value.
# This allows you to confirm that a signed value was created within a specified period of time:
#
#
# class TimestampSigner(key=None, sep=’:’, salt=None):
# sign(value);
# Sign value and append current timestamp to it.
# unsign(value, max_age=None);
# Checks if value was signed less than max_age seconds ago, otherwise raises SignatureExpired.
# The max_age parameter can accept an integer or a datetime.timedelta object.
#


from datetime import timedelta
from django.core.signing import TimestampSigner

signer = TimestampSigner()
value = signer.sign('hello')
value

# OUTPUT: 'hello:1NMg5H:oPVuCqlJWmChm1rA2lyTUtelC-c'

signer.unsign(value)

# OUTPUT: 'hello'

signer.unsign(value, max_age=10)

# OUTPUT: 'SignatureExpired: Signature age 15.5289158821 > 10 seconds'

signer.unsign(value, max_age=20)

# OUTPUT: 'hello'

signer.unsign(value, max_age=timedelta(seconds=20))

# OUTPUT: 'hello'


