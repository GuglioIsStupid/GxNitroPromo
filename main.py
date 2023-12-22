import requests
import json
import random

# Opera GX Nitro Promo

amount = int(input("How many codes do you want to generate? "))
print("Generating codes...")

giftStartURL = "https://discord.com/billing/partner-promotions/1180231712274387115/"

"""
curl 'https://api.discord.gx.games/v1/direct-fulfillment' \
  -H 'authority: api.discord.gx.games' \
  -H 'accept: */*' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'content-type: application/json' \
  -H 'origin: https://www.opera.com' \
  -H 'referer: https://www.opera.com/' \
  -H 'sec-ch-ua: "Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: cross-site' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0' \
  --data-raw '{"partnerUserId":"2bcedc970962a86fdb92c60ce684ee625c1fe9e97f36b5e0d0983f80d57a1fb6"}' \
  --compressed
"""

codes = []
for i in range(amount):
    try:
        r = requests.post("https://api.discord.gx.games/v1/direct-fulfillment", 
                        headers={
                            "authority": "api.discord.gx.games",
                            "accept": "*/*",
                            "accept-language": "en-US,en;q=0.9",
                            "content-type": "application/json",
                            "origin": "https://www.opera.com",
                            "referer": "https://www.opera.com/",
                            "sec-ch-ua": '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
                            "sec-ch-ua-mobile": "?0",
                            "sec-ch-ua-platform": '"Windows"',
                            "sec-fetch-dest": "empty",
                            "sec-fetch-mode": "cors",
                            "sec-fetch-site": "cross-site",
                            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0",
                        },
                        data=json.dumps({"partnerUserId": "2bcedc970962a86fdb92c60ce684ee625c1fe9e97f36b5e0d0983f80d57a1fb6"})
                    ).json()
        
        code = giftStartURL + r["token"]
        codes.append(code)
    except:
        print("Error. Possibly ratelimited. Saving codes to file...")
        break

# save codes to file
with open("codes.txt", "w") as f:
    for code in codes:
        f.write(code + "\n")