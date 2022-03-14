data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1 #count = count + 1的快寫法
        if count % 1000 == 0: # %符號為餘數 
            print(len(data))

print(data[0])
print('-----------')
print(data[1])