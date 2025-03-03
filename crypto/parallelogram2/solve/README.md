# Solve
https://eprint.iacr.org/2020/1506.pdf

Page 28.

# Explanation and Motivation

Basically, we have the equations 

$s_1 k_1 \equiv (h_1 + d \times r_1)$ mod $n$

and 

$s_2 k_2 \equiv (h_2 + d \times r_2)$ mod $n$

The main vulnerability in the code lies in the fact that $k_1, k_2$ are *small*. They should be around the same size as $n$, but are only 100 bits each. 

To exploit this, we try to use LLL. However we encounter an issue: $d$ is not known to us, so we cannot solve for $k_1, k_2$ so easily.

This is not a big problem. We can simply do algebra to make the $d$s cancel out. For example,

$s_1 k_1 r_2 \equiv h_1 r_2 + d r_1 r_2$ mod $n$

and

$s_2 k_2 r_1 \equiv h_2 r_1 + d r_1  r_2$ mod $n$.

Subtracting,

$s_1 k_1 r_2 + h_2 r_1 - s_2 k_2 r_1 - h_1 r_2 \equiv 0$ mod $n$

This gives us

$k_1 (s_1 r_2) + k_2 (-s_2 r_1) + (h_2 r_1 - h_1 r_2) \equiv 0$ mod $n$.

Let $K$ be a large number. This is now solvable with LLL, for instance with the matrix 

$$
\begin{bmatrix}
n & 0 & 0 & 0 \\
s_1r_2 & 1 & 0 & 0 \\
-s_2r_1 & 0 & 1 & 0 \\
h_2r_1 - h_1r_2 & 0 & 0 & K
\end{bmatrix}
$$

However if you just directly run LLL on said matrix, the result you get will not be correct. Why? In this case, the value in the first column needs to be $0$ for our solution to be valid. LLL only finds a *short* vector. 

If the value in the first column is not $0$, there is not much "punishment" as the length of the vector will not increase by much. 

Instead, we may run LLL on the following matrix

$$
\begin{bmatrix}
Kn & 0 & 0 & 0 \\
Ks_1r_2 & 1 & 0 & 0 \\
-Ks_2r_1 & 0 & 1 & 0 \\
Kh_2r_1 - h_1r_2 & 0 & 0 & K
\end{bmatrix}
$$

(In fact, this is the same reason why the last row last column should have value $K$ instead of say, value $1$)

Running LLL on this matrix will produce the vector $(0, k_1, k_2, K)$. From which we can easily calculate the value of $d$. The value of $K$ I used is $2^{100}$.

# Note
This is the solution I came up with, the one in the paper is much less "gimmicky", and simply works if you run LLL on the following matrix:

$$
\begin{bmatrix}
n & 0 & 0 \\
-s_1^{-1}s_2r_1r_2^{-1} & 1 & 0 \\
s_1^{-1}r_1h_2r_2^{-1}-s_1^{-1}h_1 & 0 & K \\
\end{bmatrix}
$$

(with the same value of $K$, namely $2^{100}$)