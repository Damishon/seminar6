fhand = open ("mailbox.txt")

lines=fhand.readlines()
Damishon=[]
file2=open('output.txt', 'w')
for line in lines:
   if 'SMTP ID' in line:
      if line not in Damishon:
         Damishon.append(line[68:-1])
Damishon.sort()

print(Damishon)

file2.write(str(Damishon)) 
file2.close()
fhand.close()


