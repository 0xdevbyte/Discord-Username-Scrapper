# Discord Username Scraper

## Author
0xdevbyte

## Date
10/25/2024

## Description
This project is a Python-based scraper designed to extract usernames from a specified Discord channel. It retrieves messages from the Discord API and collects unique usernames, saving them to a text file for further use.

## Features
- Scrapes a specified number of usernames from a Discord channel.
- Saves the collected usernames to a text file.
- Handles API requests and responses with error checking.

## Prerequisites
- Python 3.x
- `requests` library (install via pip)

## Installation
1. Clone the repository or download the script file.
2. Install the required dependencies:
   ```bash
   pip install requests
3. Update the channel_id, token, and amount in the if __name__ == "__main__": part of main.py to your liking

## Usage
To run the scraper, execute the following command in your terminal:
- `py main.py`

## Parameters
channel_id: The ID of the Discord channel from which to scrape usernames
token: Your account token
amount: The number of usernames to scrape

## Output
The scraped usernames will be saved in a text file named scraped.txt in the same folder as the script.

## Notes
- Be aware of Discord's rate limits and terms of service when using this script

## Contact
For any qestions dm me on discord 
- `devbyte.py`
