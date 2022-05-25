import requests

word = input("word: ").strip().lower()
url = r"https://dictionary.cambridge.org/us/dictionary/english-russian/" + word
headers = requests.utils.default_headers()
headers.update(
    {
        'User-Agent': 'My User Agent 1.0',
    }
)
response = requests.get(url, headers=headers)
with open(r"data\cambridge_get.html", 'w', encoding="utf-8") as f:
    f.write(response.text)
