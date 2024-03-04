import re

p = "my-p@ssw0rd"
reg = r"^[a-zA-Z0-9-@_]{6,18}$"
print(re.findall(reg, p))

