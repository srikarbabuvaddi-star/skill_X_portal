import urllib.request as u
try:
    r=u.urlopen('http://127.0.0.1:8000/')
    print('STATUS', r.status)
    print(r.read(2000).decode('utf-8','ignore'))
except Exception as e:
    import traceback
    traceback.print_exc()
