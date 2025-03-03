# Solve

This chall requires a decent understanding of how mod works.

So the first thing that should be suspicious is: Why are we generating $d$ **before** we generate $e$? In a secure implementation of RSA, the value of $e$ should be something like 65537, a fixed value.

We can see that the values of $d$ should be from $0$ to $N$, which has size around $2^{4000}$. Interestingly, $d$ can only have size $2^{2000}$. Hence we observe that $d$ is **small**.

In fact, $d<pq$. The second thing to observe is that phi of $N$, $(p-1)(q-1)pq$ is a multiple of $pq$, **which can be computed easily** (by taking the square root of $N$).

Now we know $ed \equiv 1$ mod $(p-1)(q-1)pq$. Indeed this means that $ed \equiv 1$ mod $pq$. Since $d<pq$, this is sufficient to determine $d$. 