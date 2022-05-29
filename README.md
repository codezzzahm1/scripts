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

>api_id = #your api id 

> api_hash = '#your api hash' 

> client = TelegramClient('session_name', api_id, api_hash).start() 

### Step 3

Now that we created our client to interact with telegram server. 

Get the Username or ID of the group to extract the data. 



Now that's all the basic stuff we need. 

I will shortly brief about the functions since I didn't comment my code.

#### Analyze number of messages group receive over the days.

By finding daily chat count and comparing it with previous days, we can answer lot about the group. 

Like, 

- Is this community growing ?
- Is this community becoming useful ? 
- What is the average activeness of the group? 

We can also apply techniques like **Regression** to predict the growth.

To get that, we iterate the messages between our desired dates. 

> def get_total_chat_count_for_n_days(group_chat_username, date_range): 


>    date_with_chat_count_dict = {} 
    start_date = datetime.date.today() + datetime.timedelta(-abs(date_range))
    end_date = datetime.date.today() + datetime.timedelta(-1)
    while start_date <= end_date: 
        for chat in client.iter_messages(group_chat_username, offset_date=start_date): 
            if start_date in date_with_chat_count_dict:
                date_with_chat_count_dict[start_date] += 1 
            else:
                date_with_chat_count_dict[start_date] = 1 
    return date_with_chat_count_dict

