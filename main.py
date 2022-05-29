
from telethon import TelegramClient, sync 
from telethon import functions, types 
import datetime

api_id = 
api_hash =
client = TelegramClient('session_name', api_id, api_hash).start() 
        
def get_total_chat_count_for_n_days(group_chat_username, date_range): 
    date_with_chat_count_dict = {} 
    start_date = datetime.date.today() + datetime.timedelta(-abs(date_range))
    end_date = datetime.date.today() + datetime.timedelta(-1)
    while start_date <= end_date: 
        for chat in client.iter_messages(group_chat_username, offset_date=start_date): 
            if start_date in date_with_chat_count_dict:
                date_with_chat_count_dict[start_date] += 1 
            else:
                date_with_chat_count_dict[start_date] = 1 
    return date_with_chat_count_dict
    
def get_chats_from_group(group_chat_username):
    chats = client.iter_messages(group_chat_username, limit=10000) 
    return chats  
    
def get_members_id_and_their_chat_count(group_chat_username): 
    chats = get_chats_from_group(group_chat_username)
    members_id_with_count = {} 
    for chat in chats: 
        sender_id = chat.get_sender().id
        if sender_id not in members_id_with_count: 
            members_id_with_count[sender_id] = 1 
        else: 
            members_id_with_count[sender_id] += 1
    return members_id_with_count    
  
def get_most_active_member_id(group_chat_username): 
    members_id_with_count_dict = get_members_id_and_their_chat_count(group_chat_username)
    member_id_of_highest_count = max(zip(members_id_with_count_dict.values(), members_id_with_count_dict.keys()))[1] 
    return member_id_of_highest_count   

def get_user_details_by_userid(userid): 
    username = client(functions.users.GetFullUserRequest(id=userid)).user.username 
    first_name = client(functions.users.GetFullUserRequest(id=userid)).user.first_name 
    last_name = client(functions.users.GetFullUserRequest(id=userid)).user.last_name
    return username, first_name, last_name
    
def get_most_active_member_details(group_chat_username):
    most_active_member_id = get_most_active_member_id(group_chat_username) 
    return get_user_details_by_userid(most_active_member_id) 
    
def get_all_chat_from_user(group_chat_username, user, msg_limit): 
    chats = []
    for chat in client.iter_messages(group_chat_user_name, from_user=user, limit = msg_limit):
        chats.append(chat.message) 
    return chats     
    
group_username = input("\nGroup username? ") 

#print any function by passing group username
