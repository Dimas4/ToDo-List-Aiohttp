from create_app_db.create_db import create_db
from bson.objectid import ObjectId


class Note:
    def __init__(self):
        self.db = create_db()['test_db']
        self.note_db = self.db['note']
        self.todo_db = self.db['todo']

    async def get_where(self, **kwargs):
        todo = self.todo_db.find(kwargs)
        return await todo.to_list(length=None)

    async def create_note(self, name):
        obj_id = (await self.note_db.insert_one({'name': name})).inserted_id
        return await self.note_db.find_one({'_id': obj_id})

    async def create_todo(self, id, name):
        obj_id = (await self.todo_db.insert_one({'name': name, 'note_id': id})).inserted_id
        return await self.todo_db.find_one({'_id': obj_id})

    async def delete_todo(self, todo_id):
        await self.todo_db.delete_one({'_id': ObjectId(todo_id)})
