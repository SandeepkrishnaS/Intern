#Env is windows
#Author : Sandeepkrishna S

import requests, re, time, sys

url = "https://www.atg.world/view-article/A%20HIDDEN%20STORY-30953"

def extract_data(s):
    pattern1 = re.compile('''<script type="application\/ld\+json">\[{[@:.,\-"\/a-zA-Z0-9\s]+}]<\/script>''')
    
    pattern2 = re.compile('''"headline"\s*:\s*"[a-zA-z0-9\s]+"''')
    
    match = re.findall(pattern1,s)[0]
    match = re.findall(pattern2,match)[0].split(":")
    
    return match[1]

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

print("\n\nThe title of article at "+url+" is : ",extract_data(Wpage))
