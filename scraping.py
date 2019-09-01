#Env is windows
#Sandeepkrishna S

import requests, re, time, sys

url = "https://www.atg.world/user-profile/Mjc5OTM="

def extract_data(s):
    lst=[]
    pattern1 = re.compile('''<a\s+class="actlink"\s+href="https:\/\/www\.atg\.world\/view-article\/[a-zA-Z0-9\s]+-\d+">\s+"[a-zA-Z0-9\s]+"<\/a>''')
    
    pattern2 = re.compile('''"[a-zA-Z0-9\s]+"\s*<''')
    
    matches = re.findall(pattern1,s)
    
    for match in matches:
        lst.append(re.search(pattern2,match).group()[:-1])
    lst = set(lst)
    return lst

start = time.time()
resp = requests.get(url)
ResTime = (time.time() - start)*1000
status = resp.status_code
if status != 200:
    print("Website not responding")
    sys.exit(1)
Wpage = str(resp.text)

print("\nResponse Time : ",ResTime,"ms")
print("Status Code : ", status)

print("\n\nThe titles of articles in "+url+" is :\n")
for i in extract_data(Wpage):
    print(i)
