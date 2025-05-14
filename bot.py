import time

# Configuration
BOT_TOKEN = "7854503845:AAF95TKIFUMjNmuTYqCddwh2oeIYflU5vho"
USER_ID = "7033502056"
START_INDEX = 400
CHECK_INTERVAL = 5  # in seconds

# Function to send Telegram messages
def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": USER_ID,
        "text": text
    }
    response = requests.post(url, data=data)
    print("Telegram response:", response.status_code, response.text)

# Function to check Bonded Ring links
def check_new_bondedring(start_index):
    # Send a test message
    print("Sending test message...")
    send_telegram_message("Test message from your Bonded Ring bot!")

    current = start_index
    while True:
        url = f"https://t.me/nft/bondedring-{current}"
        print(f"Checking: {url}")
        try:
            response = requests.get(url)
            if response.status_code == 200 and "tgme_page_404" not in response.text:
                send_telegram_message(f"New Bonded Ring NFT detected: {url}")
                current += 1
            else:
                print(f"Checked {url} - not available yet.")
        except Exception as e:
            print("Error during request:", str(e))
        time.sleep(CHECK_INTERVAL)

# Start the bot
check_new_bondedring(START_INDEX)
