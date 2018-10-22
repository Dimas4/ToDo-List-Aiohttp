from db.model import Note


class Service:

    def __init__(self):
        self.db = Note()

    async def get_where(self, **kwargs):
        return await self.db.get_where(**kwargs)

    async def create_note(self, name):
        return await self.db.create_note(name)

    async def create_todo(self, id, name):
        return await self.db.create_todo(id, name)
