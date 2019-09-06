#Author : Sandeepkrishna S
#Env is Windows

import requests, json, sys, time, re

proxyDict = { 
              "http"  : "172.16.2.30:8080", 
              "https" : "172.16.2.30:8080", 
              "ftp"   : "172.16.2.30:8080"
            }
            
            
url = 'https://www.atg.party/ws-dashboard?user_id=455'


def scrape_emails_N_phones(u):
    Wpage = requests.get(u, proxies=proxyDict).text
    
    patter1 = re.compile('''[a-zA-Z0-9-()*_.]+@[a-zA-Z0-9-_]+.\b(in|com|word|us|party|world)\b''')
    
    patter2 = re.compile('''\+91\d\d\d\d\d\d\d\d\d\d''')
    
    e_match = re.findall(patter1,Wpage)
    ph_match = re.findall(patter2,Wpage)
    
    return (e_match,ph_match)

def posts(jdata):
    count = 0
    posturl= []
    for c in jdata['dashboard']:
        if 'post_url' in c:
            count+=1
            posturl.append(c['post_url'])
    return (count,posturl)

start = time.time()

r = requests.get(url, proxies=proxyDict) # Remove the proxies switch if not required....

RespTime = (time.time() - start)*1000 
data = r.json()

print("\n[*]Response Time : ",RespTime, " ms \n")

with open("response.json", "w") as write_file:
    json.dump(data, write_file)
    
if r.status_code == 200:
    print("[*]The Status code is indeed 200\n")
else:
    print("[*]The Status code is NOT 200\n")
    sys.exit(1) 
    
(post_count,post_url) = posts(data)

print("[*]The post count is ", post_count, "\n")
print("-->post_URL : [emails] : [phone]\n")

with open("post_URL.txt", "w") as pf:
    for u in post_url:
        pf.write(str(u)+'\n')
        (email,phone) = scrape_emails_N_phones(u)
        print(">>> {} : {} : {}".format(u,email,phone))
print("\n[*]All the post URLs have been saved in post_URL.txt \n")