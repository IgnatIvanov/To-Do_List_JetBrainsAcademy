# put your python code here

words = input().lower().split()
freq_dict = {}

for word in words:
    freq_dict[word] = freq_dict.get(word, 0) + 1


for pare in freq_dict.items():
    print(pare[0] + " " + str(pare[1]))
