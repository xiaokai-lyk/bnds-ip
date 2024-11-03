import json
FILE_NAME="./KUAKE-QQR_train"
f=open(FILE_NAME+".json",'r',encoding="utf-8")
text=json.load(f)
of=open(FILE_NAME+".csv",'w',encoding="utf-8")
of.write("query1,query2,label\n")
for item in text:
    of.write("{},{},{}\n".format(item['query1'],item['query2'],item['label']))