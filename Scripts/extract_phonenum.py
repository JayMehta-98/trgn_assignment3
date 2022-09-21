import re 
with open('mytextfile.txt') as f:
    contents = f.read()
print (contents)

match = re.findall(r'[\+\]?[0-9][0-9 .\-\(\)]{8,}[0-9]', contents)
if match:
    print ('phone number :', match)

else:
    print ('No match')

for s in match:
    if s.split("-")[0]=="+1":
    # print("Domestic")
        l = s.split("-")
        res =[]
        for i in range(len(l)):
            if i==1:
                res.append("(")
                res.append(l[i])
            elif i==2:
                res.append(")")
                res.append(l[i])
            else:
                res.append(l[i])
        final_format = "".join(map(str, res))
    else:
        # print("International")
        l = s.split("-")
        res =[]
        for i in range(len(l)):
            if i==1:
                res.append("(")
                res.append(l[i])
            elif i==2:
                res.append(")")
                res.append(l[i])
            else:
                res.append(l[i])
        final_format = "".join(map(str, res))
    print(final_format)
