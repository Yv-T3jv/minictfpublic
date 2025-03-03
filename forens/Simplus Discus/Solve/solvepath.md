# Key Steps / Observations

1. The disk image is in .E01 format. `strings` won't work this time.
2. Open it in Autopsy.
3. Look at /home/hyacinthus/.bash_history to find that /usr/lib/urandom has been modified.

# Alternative

1. Open the disk image in Autopsy.
2. Use the Keyword Search function to search for `IRS{` (Exact Match).
