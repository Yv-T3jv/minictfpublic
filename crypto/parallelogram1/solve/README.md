# Solve

This challenge serves as an introduction to AES.

AES is a block-cipher. In this challenge, we use ECB mode, where input is split into seperate blocks of 16 and encrypted seperately.

This is insecure: Consider a input of [block 1] [block 2] [block 3] that encrypts to become [enc 1] [enc 2] [enc 3].

If we "shuffle" the blocks, we can obtain the encrypted result of [block 2] [block 1] [block 3] as [enc 2] [enc 1] [enc 3].

We abuse this by sending AAAAparallelogra|AAAAAAAAAAAAAAA|mAAAAAAAAAAAAAAA or something similar, and shuffling the blocks (| denotes a seperation of blocks).