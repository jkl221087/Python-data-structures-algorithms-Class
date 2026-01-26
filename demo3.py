string_list = ['apple', 'banana', 'kiwi', 'pear']

count = []

for i in string_list:
    count.append(len(i))

ans = max(count)

for i in range(0, len(count)):
    if count[i] == ans:
        print(string_list[i])