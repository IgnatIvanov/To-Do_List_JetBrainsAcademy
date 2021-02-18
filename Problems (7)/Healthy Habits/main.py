# the list "walks" is already defined
# your code here

summary = 0

for dist in walks:
    summary += dist.get("distance")

print(int(summary / len(walks)))