# Key Steps / Observations

1. Realise that the provided file is a .img, which is neither compressed nor encrypted - .txt files in the filesystem are stored in plaintext.
2. Realise that the chall description hints at cheesing using `strings`.
3. run `strings kali-linux_corrupt.img | grep IRS{`.

# Alternative

1. Prepend 1025 null bytes (`0x00`) to <b>kali-linux_corrupt.img</b>.
2. Open the resultant file in Autopsy, and use the search function ("IRS\{", Exact match).
