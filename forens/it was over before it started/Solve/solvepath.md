# Key Steps / Observations

1. Find that the file won't open in an image viewer.
2. Open it in a hex editor.
3. Realise that there is `IEND` in place of `IHDR`.
4. Realise that the challenge title hints that `IEND` comes before `IHDR`.
5. Find `IHDR` at the end of the file, in place of `IEND`.
6. Swap `IHDR` and `IEND` and open the resultant file in an image viewer.
