# the list with classes; please, do not modify it
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']

# your code here

groups_count = int(input())
user_input = [input() for _ in range(groups_count)]

answer = {}
for group in groups:
    answer[group] = None

x = 0
while x < groups_count:
    answer[groups[x]] = int(user_input[x])
    x += 1

print(answer)
