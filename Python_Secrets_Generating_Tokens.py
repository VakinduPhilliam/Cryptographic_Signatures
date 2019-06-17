# Python Secrets Generating Tokens
# secrets — Generate secure random numbers for managing secrets.
# The secrets module is used for generating cryptographically strong random numbers suitable for managing data such as passwords, account authentication,
# security tokens, and related secrets.
#

# 
# In particularly, secrets should be used in preference to the default pseudo-random number generator in the random module, which is designed for modelling
# and simulation, not security or cryptography.
#

#
# Generating tokens.
# The secrets module provides functions for generating secure tokens, suitable for applications such as password resets, hard-to-guess URLs, and similar.
#

#
# secrets.token_bytes([nbytes=None]). 
# Return a random byte string containing nbytes number of bytes. If nbytes is None or not supplied, a reasonable default is used.
# 

token_bytes(16)  

# OUTPUT: 'b'\xebr\x17D*t\xae\xd4\xe3S\xb6\xe2\xebP1\x8b''

#
# secrets.token_hex([nbytes=None]). 
# Return a random text string, in hexadecimal.
# The string has nbytes random bytes, each byte converted to two hex digits.
# If nbytes is None or not supplied, a reasonable default is used.
# 

token_hex(16)  

# OUTPUT: ''f9bf78b9a18ce6d46a0cd2b0b86df9da''

#
# secrets.token_urlsafe([nbytes=None]). 
# Return a random URL-safe text string, containing nbytes random bytes.
# The text is Base64 encoded, so on average each byte results in approximately 1.3 characters.
# If nbytes is None or not supplied, a reasonable default is used.
# 

token_urlsafe(16)  

# OUTPUT: 'Drmhze6EPcv0fN_81Bj-nA'
