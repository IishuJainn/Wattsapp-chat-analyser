import pandas as pd
import re
f=open("WhatsApp Chat with GAME OF 4th SEM☺️.txt","r",encoding='utf-8')
data=f.read()
# print(data)
pattern = '\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s-\s'
messages = re.split(pattern, data)[1:]
dates = re.findall(pattern, data)
# print(dates)
df=pd.DataFrame({"user_message" :messages,"Message_Date":dates})
print(df.head())
df['Message_Date'] = pd.to_datetime(df['Message_Date'], format='%m/%d/%y, %H:%M - ')
df.rename(columns={'message_date': 'date'}, inplace=True)

users = []
messages = []
for message in df['user_message']:
    entry = re.split('([\w\W]+?):\s', message)
    if entry[1:]:  # user name
        users.append(entry[1])
        messages.append(" ".join(entry[2:]))
    else:
        users.append('group_notification')
        messages.append(entry[0])

df['user'] = users
df['message'] = messages
df.drop(columns=['user_message'], inplace=True)
# print(df.head(20))
print(len(df[df['user']=='Harshit DIT']))
print(len(df[df['user']=='Ishu Jain']))
print(len(df[df['user']=='Amitesh DIT']))
print(len(df[df['user']=='Himanshu (19 June)']))
print(len(df[df['user']=='Arkam(29 Dec)']))
print(len(df[df['user']=='Rishab DIT']))
import datetime as dt

df['only_date'] = df['Message_Date'].dt.date
df['year'] = df['Message_Date'].dt.year
df['month_num'] = df['Message_Date'].dt.month
df['month'] = df['Message_Date'].dt.month_name()
df['day'] = df['Message_Date'].dt.day
df['day_name'] = df['Message_Date'].dt.day_name()
df['hour'] = df['Message_Date'].dt.hour
df['minute'] = df['Message_Date'].dt.minute
pd.set_option('display.max_columns',None)
print(df.head())