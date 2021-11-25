fhand = open ("mailbox.txt")

lines=fhand.readlines()
Damishon=[]
file2=open('output.txt', 'w')

for line in lines:
   if 'SMTP ID' in line:
     print(line[68:-1])
     if line not in Damishon:

           Damishon.append(line[68:-1])
   Damishon.sort()

if line in Damishon:
     file2.write(line[68:-1])
     file2.write('\n')

file2.write(str(Damishon)) 
file2.close()
fhand.close()



