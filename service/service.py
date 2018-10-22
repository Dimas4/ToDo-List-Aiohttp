from db.model import Note


class Service:

    def __init__(self):
        self.db = Note()

    async def create(self, name):
        return await self.db.create(name)

    async def get_all(self):
        return await self.db.get_all()
