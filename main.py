"""
@Author: github.com/0xdevbyte
@Date: 10/25/2024
"""

import os
import requests
import time

class Scraper:
    
    def __init__(self, channel_id, token, amount):
        self.token = token
        self.channel_id = channel_id
        self.usernames = []
        self.amount = amount
        self.params = {'limit': 100}
        self.output_file = './scraped.txt'

        os.system("title made by devbyte")

    def get_usernames(self):
        print(f"Starting scraping for {self.amount} usernames...\n")
        
        while len(self.usernames) < self.amount:
            response = requests.get(
                url=f'https://discord.com/api/v9/channels/{self.channel_id}/messages', 
                params=self.params, 
                headers={
                    'Authorization': f"{self.token}",
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
                }
            )
            
            if response.status_code != 200:
                print("Error: Unable to fetch messages.")
                break

            messages = response.json()
            if not messages:
                print("No more messages to fetch.")
                break

            for message in messages:
                username = message['author']['username']
                if username not in self.usernames:
                    self.usernames.append(username)
                    print(f"Scrapped ({len(self.usernames)}/{self.amount}): {username}")

            self.params['before'] = messages[-1]['id']

        self.save_usernames()

    def save_usernames(self):
        print("\nSaving usernames to file...")
        with open(self.output_file, 'a', encoding='utf-8') as file:
            for username in self.usernames:
                if '�' not in username:
                    file.write(username + '\n')
        print(f"Usernames saved to {self.output_file}")

if __name__ == "__main__":
    scraper = Scraper(
        channel_id='1297276152985161789',
        token="ODc4Mzk2NDY0ODI3NjI5NTg4.Gg-GLB.7tdz69glUrm7-0LkpCV9SHfn7wnM9c4qiQAO1I",
        amount=1000 # amount of usernames scrapped
    )
    scraper.get_usernames()
