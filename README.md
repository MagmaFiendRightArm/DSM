# DMS

this script hooks up to discord’s gateway n fakes a nitro status, makin it look like u playin a game or streamin. it keeps the connection alive by sendin heartbeats, handles errors, n sets ur custom status. perfect for flexin on discord!

## Features
- Fake discord status with custom activity
- Sends heartbeats to maintain connection
- Handles websocket errors
- Customizable activity details

## Requirements
- Python 3.x
- `requests` library
- `websocket-client` library

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/mxkxkks/DMS.git

## Usage
1. Edit the `usertoken` variable in `main.py` with your Discord token.

2. Run the script:
   ```bash
   python main.py
