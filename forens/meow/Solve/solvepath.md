# Key Steps / Observations

1. Upload the file to Aperi'Solve.
2. Find that the "Binwalk" section shows that there are 2 JFIFs.
3. Download the Binwalk'd files, unzip the `.7z`, append `.jfif` to the resultant files, and open them in an image viewer.

# Note

If you are running binwalk on your own machine, you might have to use `binwalk --dd=".*" <path_to_file>`.<br>
Did you know that the `cat` command stands for "con<b>cat</b>enate file to terminal"?
