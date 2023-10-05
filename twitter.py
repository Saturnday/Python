"""
import re
url = input('link? ')
name=url.replace("Https://twitter.com/", "")
print(name)
"""
import re
url = input('link? ').strip()
i=re.search(r"^(?:https?//www\.)?twitter\.com/([a-z0-9]+)$", url, re.I)
if i:
# Walrus operator usage:
#if i := e.search(r"^(?:https?//www\.)?twitter\.com/([a-z0-9]+)$", url, re.I)
    name = i.group(1)
    print(f"The user name is {name}")
"""

"""