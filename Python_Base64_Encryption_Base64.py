# Python Base64 Encryption
# base64 — Base16, Base32, Base64, Base85 Data Encodings
# This module provides functions for encoding binary data to printable ASCII characters and decoding such encodings back to binary data.
# It provides encoding and decoding functions for the encodings specified in RFC 3548, which defines the Base16, Base32, and Base64 algorithms, and for the
# de-facto standard Ascii85 and Base85 encodings.
# The RFC 3548 encodings are suitable for encoding binary data so that it can safely sent by email, used as parts of URLs, or included as part of an HTTP
# POST request.
# The encoding algorithm is not the same as the uuencode program.
#
# base64.encodebytes(s) 
# Encode the bytes-like object s, which can contain arbitrary binary data, and return bytes containing the base64-encoded data, with newlines (b'\n')
# inserted after every 76 bytes of output, and ensuring that there is a trailing newline, as per RFC 2045 (MIME).
# 

# 
# An example usage of the module:
# 

import base64

encoded = base64.b64encode(b'data to be encoded')
encoded

# OUTPUT: 'b'ZGF0YSB0byBiZSBlbmNvZGVk''

data = base64.b64decode(encoded)
data

# OUTPUT: 'b'data to be encoded''
