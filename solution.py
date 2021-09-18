# ! /usr/bin/env python3

from nacl.secret import SecretBox
from nacl.exceptions import CryptoError
import sys
import json

inputs = json.load(sys.stdin)
outputs = {}

# Problem 1
ints_sum = 0
ints_product = 1
for x in inputs["problem1"]:
    ints_sum += x
    ints_product *= x
outputs["problem1"] = {
    "sum": ints_sum,
    "product": ints_product,
}

# Output
#
# In the video I wrote something more like `json.dump(outputs, sys.stdout)`.
# Either way works. This way adds some indentation and a trailing newline,
# which makes things look nicer in the terminal.
print(json.dumps(outputs, indent="  "))