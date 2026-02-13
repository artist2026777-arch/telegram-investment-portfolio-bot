import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
# NEVER hardcode tokens in source code.
TOKEN = os.getenv("BOT_TOKEN")

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize bot and dispatcher
if not TOKEN:
    logger.error("BOT_TOKEN is not set in environment variables.")
    exit(1)

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

# Mock database for demonstration (In-memory)
user_balances = {}

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    """
    Handle the /start command.
    """
    user_id = message.from_user.id
    if user_id not in user_balances:
        user_balances[user_id] = 0.0
    
    await message.answer(
        "👋 Welcome to the Investment Portfolio Tracker!\n\n"
        "This bot simulates a simple investment account.\n"
        "Commands:\n"
        "/balance - Check your balance\n"
        "/invest <amount> - Simulate a deposit\n"
        "/withdraw <amount> - Simulate a withdrawal\n\n"
        "⚠️ This is a demo bot. No real money is involved."
    )

@dp.message(Command("balance"))
async def cmd_balance(message: types.Message):
    """
    Check current balance.
    """
    user_id = message.from_user.id
    balance = user_balances.get(user_id, 0.0)
    await message.answer(f"💰 Your current portfolio value: ${balance:.2f}")

@dp.message(Command("invest"))
async def cmd_invest(message: types.Message):
    """
    Simulate adding funds.
    Usage: /invest 100
    """
    args = message.text.split()
    if len(args) != 2:
        await message.answer("Usage: /invest <amount>")
        return

    try:
        amount = float(args[1])
        if amount <= 0:
            raise ValueError
        
        user_id = message.from_user.id
        current_balance = user_balances.get(user_id, 0.0)
        user_balances[user_id] = current_balance + amount
        
        await message.answer(f"✅ Successfully invested ${amount:.2f}. New balance: ${user_balances[user_id]:.2f}")
    except ValueError:
        await message.answer("❌ Please enter a valid positive number.")

@dp.message(Command("withdraw"))
async def cmd_withdraw(message: types.Message):
    """
    Simulate withdrawing funds.
    Usage: /withdraw 50
    """
    args = message.text.split()
    if len(args) != 2:
        await message.answer("Usage: /withdraw <amount>")
        return

    try:
        amount = float(args[1])
        if amount <= 0:
            raise ValueError
        
        user_id = message.from_user.id
        current_balance = user_balances.get(user_id, 0.0)
        
        if current_balance < amount:
            await message.answer("❌ Insufficient funds.")
            return
            
        user_balances[user_id] = current_balance - amount
        await message.answer(f"✅ Successfully withdrew ${amount:.2f}. New balance: ${user_balances[user_id]:.2f}")
    except ValueError:
        await message.answer("❌ Please enter a valid positive number.")

async def main():
    """
    Main entry point.
    """
    logger.info("Starting bot...")
    # Delete webhook if set, to ensure polling works
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot stopped.")