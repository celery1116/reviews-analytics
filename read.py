data = []
file = 'reviews.txt'
with open(file,'r') as f:
	for line in f:
		data.append(line)
print('檔案'+ file +'留言資料數量為',len(data),'筆')

sum_len = 0
for d in data:
	sum_len += len(d)
print('留言平均長度為', sum_len/len(data))