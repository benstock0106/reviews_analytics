data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1 #count = count + 1的快寫法
        if count % 1000 == 0: # %符號為餘數 
            print(len(data))
print('檔案讀取完了,總共有', len(data), '筆資料')

sum_len = 0
for d in data:
    sum_len += len(d) #算出100萬筆留言的總長度
print('平均是' ,sum_len/len(data)) #總長度 除 100萬筆留言 求得留言平均長度