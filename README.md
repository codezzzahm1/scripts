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

https://github.com/codezzzahm1/telescraper/blob/main/main.py#L6-L8

### Step 3

Now that we created our client to interact with telegram server. 

Get the Username or ID of the group to extract the data. 



Now that's all the basic stuff we need. 

I will shortly brief, since I didn't comment my code.

#### Analyze number of messages group receive over the days.

By finding daily chat count and comparing it with previous days, we can answer lot about the group. 

Like, 

- Is this community growing ?
- Is this community becoming useful ? 
- What is the average activeness of the group? 

We can also apply techniques like **Regression** to predict the growth.

To get that, we iterate the messages between our desired dates. 

https://github.com/codezzzahm1/telescraper/blob/main/main.py#L10-L20

#### Get all the messages from group 

This is the tremendous and very use full data we are going to get.

The process might take longer, if your group is very active, since there will be lot of chats.

The cleaning process will be tedious, but after completion you may get good dataset on the particular topic of the group. 

This is very use full in ML.

Like, 

- Chatbot 
- Sentiment Analysis
- Text Summarization 

To do this, we iterate all the messages until certain limit reached. 

https://github.com/codezzzahm1/telescraper/blob/main/main.py#L22-L24

###### Tip : Use pandas to export it as CSV or EXCEL.

#### Get the members with their chat count 

Getting amount of messages user sent in group is interesting one.

By this, we will to know who is the most active/inactive and how much they contributed for the community or how much of troller they are.



