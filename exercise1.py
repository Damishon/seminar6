fhand = open ("mailbox.txt")

lines=fhand.readlines()
Damishon=[]
file2=open('output.txt', 'w')
for line in lines:
   if 'SMTP ID' in line:
      print(line[68:-1])
      if line not in Damishon:
              Damishon.append(line)
Damishon.sort()
for line in Damishon:
       file2.write(line[68:-1])      
       file2.write('\n') 
file2.close()
fhand.close()

