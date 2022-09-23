import re 
with open('mytextfile.txt') as f:
    contents = f.read()

match = re.findall(r'[\+\]?[0-9][0-9 .\-\(\)]{8,}[0-9]', contents)
#print(match)

for s in match:
    
    #print('P',s.split("-")[0])
    if "+" in s.split("-")[0]:
    # print("Domestic")
        l = s.split("-")
        # print('l',l)
        res =[]
        for i in range(len(l)):
            if i==1:
                res.append(" (")
                res.append(l[i])
            elif i==2:
                res.append(") ")
                res.append(l[i])
            else:
                res.append(l[i])
        #print('res if',res)
        final_format = "".join(map(str, res))
    else:
         #print("International")
        #print('else')
        l = s.split("-")
        #print('l',l)
        res =[]
        for i in range(len(l)):
            if i==0:
                res.append("(")
                res.append(l[i])
            elif i==1:
                res.append(")")
                res.append(l[i])
            else:
                res.append(l[i])
        #print('res',res)
        final_format = "".join(map(str, res))
    print(final_format)
