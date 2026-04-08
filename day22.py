import json



from urllib.request import urlopen

try:
    with urlopen("https://open.er-api.com/v6/latest/USD") as response:
        source = response.read()
    data = json.loads(source)
    print(json.dumps(data, indent=2))

except Exception as e:
    print(f"Error: {e}")

#new lines added

print("hello world")