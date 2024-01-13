import socket, time, re
import schedule
from pypresence import Presence

BOT_USERNAME = "YOUR_TWITCH_USERNAME"
CHANNEL_NAME = "CHANNEL_NAME"
BOT_OAUTH_TOKEN = "OAUTH_TOKEN" 

def receive_irc_messages(sock, stop_string):
    while True:
        for i in range(30): 
            # Receive data from the socket up to 4096 bytes at a time
            data = sock.recv(4096).decode('utf-8', 'ignore')

            # If the stop string is found in the data, print the whole message and return
            if stop_string in data:
                for line in data.split("\n"):
                    if "YOUR_TWITCH_USERNAME " in line:
                        return data
        sock.send(f"PRIVMSG #{CHANNEL_NAME} :!watchtime\r\n".encode("utf-8"))

client_id = 'YOUR_DISCORD_CLIENT_ID'  # Put your Client ID here
RPC = Presence(client_id)  
RPC.connect()  
buttons = [{"label": "Come join me 😄", "url": "https://www.twitch.tv/CHANNEL_NAME"}, {"label": "❗❗Read before adding❗❗", "url": "https://nohello.net/"}]

def execute_function():
    # Create a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to an IRC server
    sock.connect(("irc.chat.twitch.tv", 6667))

    # Send login credentials to the server
    sock.send(f"PASS {BOT_OAUTH_TOKEN}\r\n".encode("utf-8"))
    sock.send(f"NICK {BOT_USERNAME}\r\n".encode("utf-8"))

    # Join the channel
    sock.send(f"JOIN #{CHANNEL_NAME}\r\n".encode("utf-8"))

    # code to execute goes here
    # Receive IRC messages 
    sock.send(f"PRIVMSG #{CHANNEL_NAME} :!watchtime\r\n".encode("utf-8"))
    string = receive_irc_messages(sock, "YOUR_TWITCH_USERNAME has spent ")
    
    match = re.search(r'(\d+) months and (\d+) (days|hours)', string)

    if match:
        # Extract the months and days from the match object
        months = int(match.group(1))
        time_amount = int(match.group(2))
        time_unit = match.group(3)

        # Convert the months and days to hours
        hours = months * 30 * 24 
        if time_unit == "days":
            hours += time_amount * 24
        elif time_unit == "hours":
            hours += time_amount
    else:
        print("No match found. Cannot update presence.")
        return

    current_time = time.time()
    RPC.update(
        details=f"Time watched in total: {hours} hours",
        state=str("Last updated:"),
        # large_image="CUSTOM_IMAGE",       This can be changed to a custom image you set in the Discord application.
        # small_image="CUSTOM_IMAGE",       This can be changed to a custom image you set in the Discord application.
        buttons=buttons,
        start=current_time)
execute_function()
schedule.every(4).hours.do(execute_function) 

while True:
    schedule.run_pending()
    time.sleep(1)