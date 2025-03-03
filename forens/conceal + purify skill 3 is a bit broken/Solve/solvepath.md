# Key Steps / Observations

1. Open the file in a hex editor.
2. Realise that many of the same characters are appearing. Maybe some form of binary data can be extracted?
3. With reference to the Wikipedia article (and article section: "ELF header") linked in the challenge description, realise that the first 4 bytes are untouched.
4. With reference to the same section, realise that bytes at (0-indexed, hexadecimal) offsets 0x05, 0x08, 0x0B, 0x0D, etc. are all far larger than expected. Furthermore, they all have their most-significant bits set to 1 (or "True")...
5. Guess that this is an MSB chall and attempt it as such.

# Sample .py solve: notes

- `>>` represents a bitshift operation. If we let `x` be `0b10000000` (decimal 128 in base-2), `x >> 7` would equal `0b1` (decimal 1 in base-2). Essentially, the last 7 bits are discarded. You are left with the bit representing 2<sup>8</sup>, that is, the most-significant bit in a byte.
- The byte is not printed if it is equal to `0x08`. This is because printing `chr(0x08)` would result in a backspace, and would erase most of your flag. Alternatively, you could check if the current byte is the `'}'` (ASCII `0x7D`) character, and stop printing if so.

# Sample CyberChef solve: notes

- The first step is to remove the magic bytes (or magic number).
- In the next step of the recipe, essentially, the last 7 bits in each byte are discarded. You are left with the bit representing 2<sup>8</sup>, that is, the most-significant bit in a byte.
- In the 3rd step, `\x00` bytes are replaced with `'0'` and `\x01` with `'1'`.
- In the last step, the binary string is converted into the flag, and a bunch of other characters. You don't need to care about backspaces here (as opposed to in the Python solution) as they are represented as the `0x08` bytes are displayed as control characters rather than "executed" as backspaces.