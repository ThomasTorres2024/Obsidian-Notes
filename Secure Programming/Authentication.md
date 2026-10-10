---
title: Authentication
tags:
  - Secure_Programming
draft: "False"
---
# Types:

- Something you know
- Something you are
- Something you have
- Something you are 

---
# Password Security 

- "Something you know" form of authentication
- De-facto standard, many pitfalls
	- People can make super simple passwords, too easy to remember and easier to attack
	- Hard to remember lots of different passwords, especially long and complicated ones 
	- Password reuse is an issue as well 
- Susceptible to many forms of attacks


# Online Attacks

Someone tries to login to system as a user. Can be done manually or with some automated script as well.
### Attack
* Manual or automated login attempts against the system
* Note: Lists of previously breached passwords are collected and tried on other systems
* Social engineering 

### Defense 

* Limited number of attempts 
* Rate-limiting new login attempts
* Disable account
* Honeypot passwords
	* Passwords that exist that allow us to determine if certain passwords etc were breached 
* Display last login
* 2 factor
* Password alternatives

# Good Passwords:

* Don't allow users to choose bad paswords
* We are interested in high [[Entropy]] passwords
* Character type requirements
* Length requirements (nowadays 8 characters is trivially breakable)
* Don't allow the user to choose "known passwords"
	* History of passwords, user cannot reuse a password
* Encourage the use of password managers

---
# Online Attacks

### Attack -

* Attacker captures password database 
* If encrypted/hashed, there are many brute-force attacks, especially if the algorithm underlying is known 
* Known algorithms without salts allow pre-computation

### Defense -

* One way hash, based on cryptography, we cannot reverse a hash done to our password
* MFA - even if a password is broken, a second factor has to be compromised


---
# Examples of Security Breaches

### Yahoo Data Breach (2013-2014)
* Breach compromised over $3$ billion accounts
* Attackers used access to user data, including hashed passwords
* Weak [[MD5]] [[Hashing]] algorithm, very susceptible to brute force attacks 

---
# Hashing

* Passwords should be hashed
* Same idea as cryptography 
	* We want to mangle text and reverse text that's mangled
	* In hashing we do not want to unmangle the text. 
* Hashing algorithms produce fixed length value.
* Hashes are __not__ meant to be [[injective]], they may have many values that all map to some hash 
* Output of a hash is a string of bytes, to store them in a portable way, they typically are encoded in [[base64]]. 

Various hashing Algorithms:


* DE5 (1976-1997)
* MD5 (1992-2009)
* SHA1 (1995-2010)
* SHA2 (2001-) 
* SHA3 (2015-)

All of the above algorithms are very well known and can be embedded into chips. 

* bcrypt - Designed for passwords; slow
* scrypt - Time memory trade off
* Argon2 - Needs 1+ second to be stronger than bcrypt, also resistant to GPU

---
# What makes a Hashing Algorithm good?

### Collision
Find any two different messages that hash to the same value. We want this to be fairly low.

### Preimage
Find a message that hashes to a particular hash

### Second Preimage
Find a message that hashes has the same hash as a given message 

We can do timing attacks on the implementations of these things. If we can determine how long the CPU takes, we can determine the algorithm used, potentially. 

---
# Salting

* Hash functions need to be predictable (Deterministic, same output for some input)
* Without extra work, two users with the same password, share the same hash. From the POV of an attacker, this makes it a lot easier for them, since they don't need to crack each individual user's password when they can break multiple user's in one. 
* We can add"salt to the password before calling the hash function by randomly changes [[Byte]]s, this will completely change the resulting hash.
* When we do comparison we need to actually know what the hash gets mapped to. When a user comes back, we need to perform the same hash and do the same verification. But, when they come back we need to know the same hash again to verify them. 
* How many hashes need to be computed for a $k$-bit salt?
	* If we add $k$ bits of salt to a password, how much additional work do we need to add our computation so we need $2^k$ many bits in total here, making this $O(2^k)$ and thus __very__ expensive. 

---
# Efficency

* Hash functions should be efficiency for their primary purpose of integrity
* This is at odds with the requirements for brute force attacks
* Key-Stretching uses many iterations, we rehash values:
	* $h(p)=c_{1},c_{2}=h(c_{1})\dots,c_{n}=h(c_{n-1})$
* Password Based Key Derivation Function
	* Use key stretching and 128 bit salt to produce key material that can be used in symmetric ciphers
* __scrypt__ designed to require more memory to compute, to make specialized hardware more expensive 
* Argon2 - designed to be efficient as well to control time, memory, and parallelism

---
# A Password API

In PHP, Password introduced a password API consisting of $4$ functions:

* password_hash - Hashes a given password
* password_verify - Hashes a password compared to stored hash 
* password_needs_rehash Tests if stored hash matches current hash type.parameters
* password_get_info Returns type/parameter of stored hash 

__Large issue using password_hash__ versus a normal hash for comparison if we want to validate a user. We can time the amount of time the algorithm takes if we compare element wise, we make the operation in total some constant amount of time so no more info could be gained if we were to do some bruteforce attack and gradually gain insight into the password. 

---
# Bio-metrics

### Types:

* Fingerprints
* Retinas
* Facial Recognition
* Voice Print (generally depreciated)
### Pro/Cons
* Pro Ease of use
* Pro Impossible to forget
* Con Hard to revoke/replace
* Con Deployment (Generally easy nowadays for facial recognition and fingerprints). Deployment is __generally__ a lot easier with modern devices. 

---
# Tokens/Devices

### TOTP Time based One-Time Password
* Used by MFA. Every $60$ seconds maybe we regenerate a pin and it continually rotates. Idea is there's a very short limited window in which it can actually be attacked. It becomes hard to find password 
### Phone Push notification to phone
* Relies on out of band communication
* SMS messages __very__ insecure 

---
# Location

Location information may be used as part of making an authentication decision. 

* Which network or segment is the device connected to
* What is the physical location of the device? 
	* Has the user connection from here before?
	* If authentication is session based, how to determine if the device has left the original location? 

---
# WebAuthN 

### Registration

* User registers for site 
* Site sends challenge with user info and site 
* Local authenticator generates Key for site, stores, and sends public key to server with challenge response
### Login:

1. Server generates and sends cryptographic challenge
2. Client uses key for this site (stored in hardware if supported, to respond to challenge)