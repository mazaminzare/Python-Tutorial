import re

# Named groups
pattern = re.compile(r"(?P<first>\w+) (?P<last>\w+)")
match = pattern.match("Amin Zare")
print(match.group('first'))  # Output: John
print(match.group('last'))  # Output: Doe

# Lookahead and Lookbehind
pattern = re.compile(r"(?<=\$)\d+")
match = pattern.findall("The price is $100 and $200")
print(match)  # Output: ['100', '200']
