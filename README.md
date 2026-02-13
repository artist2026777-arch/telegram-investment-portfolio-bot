# Investment Portfolio Bot

A simple Telegram bot to simulate an investment portfolio tracker. This bot demonstrates command handling, state management (in-memory), and secure configuration using environment variables.

## ⚠️ Security Notice

**NEVER** share your Bot Token publicly or paste it into code repositories. The token you provided in the prompt was removed from this generated code for your safety. If that token was posted publicly, you should **Revoke** it immediately in BotFather.

## Features

- `/start`: Initialize profile.
- `/balance`: View current portfolio value.
- `/invest <amount>`: Add mock funds.
- `/withdraw <amount>`: Remove mock funds.

## Local Installation

1. **Clone the repository**
2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure Environment**:
   - Rename `.env.example` to `.env`.
   - Paste your **new** token into `.env`.
5. **Run the bot**:
   ```bash
   python bot.py
   ```

## Deployment (Docker)

To run 24/7 on a VPS or cloud server:

1. **Build the image**:
   ```bash
   docker build -t invest-bot .
   ```
2. **Run container**:
   ```bash
   docker run -d --name my-invest-bot --env-file .env invest-bot
   ```
