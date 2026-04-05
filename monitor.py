import requests

URL = "https://share.weverseshop.io/static/shares/sale/43782"
WEBHOOK = "https://discord.com/api/webhooks/1490372167983173885/hKmgaGr1Xeuh268ncP7FEyX5c91y6eMOzv5H7FiXa9TyffYSvOnnFE8Gu49BgMb35Jyx"

r = requests.get(URL, allow_redirects=True)
html = r.text.lower()

if "sold out" not in html and "품절" not in html:
    requests.post(WEBHOOK, json={
        "content": f"🚨 Weverse可能補貨！\n{URL}"
    })
