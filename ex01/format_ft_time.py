#Write a script that formats the dates this way, of course your date will not be mine
#as in the example but it must be formatted the same.
#Expected output:
#$>python format_ft_time.py | cat -e
#Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$

import time
seconds = time.time()
print("Seconds since January 1, 1970:", seconds, "or","{:.2e}".format(seconds), "in scientific notation", sep=' ')
