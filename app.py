import requests
import socket
from flask import Flask

# Your Webhook URL
webhook_url = 'https://discord.com/api/webhooks/1338168922935136267/RpF-lYkLx2Hi5wUATDRPA_-KN0ebYnPQCfy2oNx86Y7Gt_rgq787-vUCtCV4eVXUQS8S'

app = Flask(__name__)

# Function to get the local machine's IP address
def get_ip():
    ip_address = socket.gethostbyname(socket.gethostname())
    return ip_address

# Route for the website
@app.route('/')
def home():
    ip_address = get_ip()
    data = {
        'content': f'IP Address: {ip_address}'
    }
    # Send the IP address to the webhook
    response = requests.post(webhook_url, json=data)
    if response.status_code == 204:
        return f'IP Address sent: {ip_address}'
    else:
        return f'Failed to send IP. Status code: {response.status_code}'

# Start the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
