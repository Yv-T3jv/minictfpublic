# Solve

In this challenge, the main observation is that some of the primes are shared across different public keys.

Taking gcd of different Ns, we can obtain some values of p and hence factor those numbers.

This is why you cannot reuse primes from RSA and why primes need to be **randomly generated**.