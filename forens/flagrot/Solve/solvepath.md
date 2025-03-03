# Key Steps / Observations

1. Translate the non-ASCII text in the challenge description: "How do you know what language the .png is written in?? Wait, what?"
2. Open the file in a hex editor and realise that it is a PDF.
3. Upon realising the PDF is blank, Google "how to find language of a PDF". Deduce that it is indicated in metadata.
4. run `exiftool flag_empty_no_thoughts.png` (or `exiftool flag_empty_no_thoughts.pdf`).

# Alternative

1. "omigor PNG" \*uploads to Aperi'Solve\*
2. Find the flag in the "Exiftool" section.