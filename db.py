import asyncpg

import settings
from coin_checker import Coin

pool = None  # asyncpg connection pool


async def create_tables():
    async with pool.acquire() as conn:
        await conn.fetch(
            '''CREATE TABLE IF NOT EXISTS coin(
                id VARCHAR PRIMARY KEY UNIQUE)'''
        )


async def init_db():
    global pool
    pool = await asyncpg.create_pool(settings.DATABASE_URL)
    await create_tables()


async def add_coins(coin_ids):
    async with pool.acquire() as conn:
        await conn.executemany(
            '''INSERT INTO coin (id)
               VALUES ($1)''',
            ((c_id,) for c_id in coin_ids),
        )


async def get_coins():
    async with pool.acquire() as conn:
        result = await conn.fetch(
            '''SELECT id FROM coin'''
        )
        return set(c['id'] for c in result)
