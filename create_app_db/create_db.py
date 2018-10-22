from motor import motor_asyncio as ma


def create_db():
    return ma.AsyncIOMotorClient('localhost')
