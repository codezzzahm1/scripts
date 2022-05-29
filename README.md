# Telegram scraper 

I made a simple script that extract data from telegram group using telethon library. 

### Why ? 

Because the data we can get from telegram chats is tremendous. We can even use them as a dataset for ML. 
By deeply analysing we get many features like sentiment anlysis etc.

### Requirements 

#### Telethon 

Telethon is a MTProto library used to interact with telegram server as a user/bot. 

> pip install telethon 

### Step 1

To create a client in telethon, api id and api hash is mandatory. 

Visit https://my.telegram.org

### Step 2

Create client 

> from telethon import TelegramClient, sync 
> api_id = #your api id
> api_hash = '#your api hash'
> client = TelegramClient('session_name', api_id, api_hash).start() 

### Step 3

Now that we created our client to interact with telegram server. 

Get the Username or ID of the group to extract the data. 



Now that's all the basic stuff we need. 

I will shortly brief about the functions since I didn't comment my code.

#### Analyze number of messages group receive over the days.

By analysing the chat count we can tell a lot about the group. 
