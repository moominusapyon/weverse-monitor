import requests

URL = "https://share.weverseshop.io/static/shares/sale/43782"
WEBHOOK = "你的discord webhook"

r = requests.get(URL, allow_redirects=True)
html = r.text.lower()

if "sold out" not in html and "품절" not in html:
    requests.post(WEBHOOK, json={
        "content": f"🚨 Weverse可能補貨！\n{URL}"
    })
