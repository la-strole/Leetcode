
# 1112233344 -> [[3,1],[2,2],[3,3],[2,4]]
value = "1"
alphabet = ""
unique = value[0]
count = 0
for i in range(len(value)):
    if value[i] == unique:
        count += 1
    else:
        alphabet = alphabet + str(count) + unique
        unique = value[i]
        count = 1
alphabet = alphabet + str(count) + unique


print(alphabet)