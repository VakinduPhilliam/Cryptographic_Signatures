# Python_Crytographic_Signatures
Python/Django Cryptographic Signature Signing. 

The golden rule of Web application security is to never trust data from untrusted sources.  

Sometimes it can be useful to pass data through an untrusted medium. 

Cryptographically signed values can be passed through an untrusted channel safe in the knowledge that any tampering will be detected. 

Django provides both a low-level API for signing values and a high-level API for setting and reading signed cookies, one of the most common uses of signing in Web applications. 

You may also find signing useful for the following: 

>    Generating “recover my account” URLs for sending to users who have lost their password. 

>     Ensuring data stored in hidden form fields has not been tampered with. 

>     Generating one-time secret URLs for allowing temporary access to a protected resource, for example a downloadable file that a user has paid for. Compiled and presented by Vakindu Philliam.
