import asyncio
from aiogram import Bot
import json
from redis import asyncio as aioredis
from config import REDIS_URL
import logging

logger = logging.getLogger(__name__)


async def start_redis_listener(bot : Bot ):
    redis = aioredis.from_url(REDIS_URL)
    logger.info("Redis listener запущен и ожидает сообщения в 'telegram:responses'...")

    while True:
        try:
            result = await redis.blpop("telegram:responses", timeout=0) 

            if not result:
                continue
            
            if result:
                key, data = result  

                if isinstance(data, bytes):
                    data = data.decode('utf-8')

                resp = json.loads(data)
                await bot.send_message(resp["user_id"], resp["text"])
                logger.debug(f"Отправлено сообщение пользователю {resp['user_id']}")

        except asyncio.CancelledError:
            logger.info("Redis listener был остановлен.")
            break
        except Exception as e:
            logger.error(f"Ошибка в Redis listener: {e}")
            await asyncio.sleep(1)  