# counter=0
# word="molokooioiyhikgjhhikgjhvgcbxvfghujkuioiuytrewqyuiokjhgfdz,mnbv bgjutf"
# for i in range(len(word)):
#     if word[i]=='y':
#         counter+=1
# print(counter)        
with open('text.txt','r') as data:
    a=data.read()
print(a) 
f=0
for i in range(len(a)):
    if a[i]=='a':
        f+=1
print(f)