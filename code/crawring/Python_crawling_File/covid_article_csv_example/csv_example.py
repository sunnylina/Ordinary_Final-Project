import csv

f = open('./covid19_articles.csv', 'r', encoding="cp949")

rdr = csv.reader(f)

next(rdr)
count = 0 

for i in rdr:
    if'[속보]' in i[2]:
        print(i[2])
        count += 1

print("속보 기사 개수 : " + str(count))

f.close()