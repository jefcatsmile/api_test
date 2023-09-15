import requests
import json

def main():
    url = 'https://api-test-omms.onrender.com'
    data = {
        'x': 6,
        'y': 4
    }
    res = requests.post(url, json.dumps(data))
    print(res)
    print(res.json())

if __name__ == '__main__':
    main()
