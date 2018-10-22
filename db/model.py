from create_app_db.create_db import create_db


class Note:
    def __init__(self):
        self.db = create_db()['note']

    async def get_all(self):
        notes = self.db.find()
        return await notes.to_list(length=None)

    async def create(self, name):
        print(dir(self.db))
        return await self.db.insert({'name': name})
