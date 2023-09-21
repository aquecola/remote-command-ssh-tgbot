import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
import paramiko

logging.basicConfig(level=logging.INFO)

# Замените этот chat_id на chat_id вашего чата
ALLOWED_CHAT_ID = 123456789

bot = Bot(token='6682546220:AAFhZvONhdsadas:321ffhhksdf')
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

@dp.message_handler(commands=['exec'])
async def execute_command(message: types.Message):
    if message.chat.id != ALLOWED_CHAT_ID:
        await message.answer("Этот бот разрешен только в определенном чате.")
        return

    command = message.get_args()
    if not command:
        await message.answer("Пожалуйста, укажите команду для выполнения.")
        return

    try:
        
        SSH_HOST='192.168.1.1'
        SSH_PORT='5500'
        SSH_USERNAME='admin'
        
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # Подключаемся к серверу
        ssh.connect(SSH_HOST, username=SSH_USERNAME, port=SSH_PORT)

        stdin, stdout, stderr = ssh.exec_command(command)

        output = stdout.read().decode('utf-8')

        await message.reply(output, reply=False)
        ssh.close()
    except Exception as e:
        await message.answer(f"Error: {str(e)}")

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
    