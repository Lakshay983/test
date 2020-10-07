# Regular expression library

import re
class TestRegEx
# Add or remove the words in this list to vary the results
wordlist = ["color", "colour", "work", "working",
            "fox", "worker"]

for word in wordlist:
        # The .+ symbol is used in place of * symbol
        if re.search('work.+', word) : 
                print (word)
