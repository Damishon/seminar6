try:
    fhand = open("mailbox.txt")
except:
    print('File cannot be opened')
    exit()



lines=fhand.readlines()
new_list=[]
file=open('output.txt', 'w')


for line in lines:
   if 'JAMES SMTP' in line:
      ind=line.find('SMTP ID ')
      en_ind=line.find(';')
      word=line[ind+8:en_ind]
      if word not in new_list:
         new_list.append(word)
      new_list.sort()
for word in new_list:
   print(word)
   file.write(word)
   file.write('\n')
fhand.close()
