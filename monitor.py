import requests
import os

URL = "https://shop.weverse.io/en/shop/KRW/artists/2/sales/56488"
WEBHOOK = "https://discord.com/api/webhooks/1490372167983173885/hKmgaGr1Xeuh268ncP7FEyX5c91y6eMOzv5H7FiXa9TyffYSvOnnFE8Gu49BgMb35Jyx"

STATE_FILE = "status.txt"


def get_status():
    r = requests.get(URL, allow_redirects=True)
    html = r.text.lower()

    if "sold out" in html or "품절" in html:
        return "soldout"
    else:
        return "instock"


def read_last_status():
    if not os.path.exists(STATE_FILE):
        return None
    with open(STATE_FILE, "r") as f:
        return f.read().strip()


def save_status(status):
    with open(STATE_FILE, "w") as f:
        f.write(status)


def send_discord():
    requests.post(WEBHOOK, json={
        "content": f"🚨 Weverse補貨！\n{URL}"
    })


current = get_status()
last = read_last_status()

print("last:", last, "| current:", current)

if last == "soldout" and current == "instock":
    send_discord()

save_status(current)
