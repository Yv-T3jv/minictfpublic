# Solve

There are 3 parts to this challenge.

We start with the zero knowledge proof segment. The goal is to get 2 values of rng that are the same, then we can easily determine the value of $c_2$.

Now we look at the LCG. It is taken mod $N = pq$. It turns out that most LCGs are periodic every $(p-1)(q-1)$ terms (depending on the values of $a$ and $c$).

That value is just phi. Lastly, we look at the RSA segment. We obtain a "leak", of $d_1$ for some value $e_1$. Notice that $(p-1)(q-1)|e_1 \times d_1 - 1$, so the LCG is periodic every $e_1 \times d_1 - 1$ terms.

Put $e_1 \times d_1 - 1$ as input to obtain $c_2$. Now there are two ways to finish the challenge.

1. Compute $d_2$ as $pow(e_2, -1, e_1 \times d_1 - 1)$, or

2. Run this twice to obtain two ciphertexts with different values of $e_2$, allowing you to finish with a euclidean algorithm-esque decryption.