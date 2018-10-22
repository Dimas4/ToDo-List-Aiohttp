import aiohttp_jinja2

from logger.create_logger import create_logger
from config.get_config import get_config
from service.service import Service
from logger.logging import Loader
from aiohttp import web


config = get_config(Loader)
routes = web.RouteTableDef()
service = Service()
logger = create_logger(config)


@routes.view("/")
class View(web.View):
    @aiohttp_jinja2.template('home/index.html')
    async def get(self):
        return

    @aiohttp_jinja2.template('home/index.html')
    async def post(self):
        note_name = (await self.request.post()).get('name')
        note = await service.create_note(note_name)
        return {'note_id': note['_id'], 'note_name': note['name']}


@routes.view("/note/{note_id}")
class NoteView(web.View):
    @aiohttp_jinja2.template('home/todo_list.html')
    async def get(self):
        note_id = self.request.match_info['note_id']
        todo_list = await service.get_where(note_id=note_id)
        return {'id': note_id, 'todo_list': todo_list}

    @aiohttp_jinja2.template('home/todo_list.html')
    async def post(self):
        note_id = self.request.match_info['note_id']
        todo_name = (await self.request.post()).get('name')
        note = await service.create_todo(note_id, todo_name)
        return {'note_id': note['_id'], 'note_name': note['name']}
