import aiohttp_jinja2

from logger.create_logger import create_logger
from config.get_config import get_config
from aiohttp.web import json_response
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
        return {'': ''}

    @aiohttp_jinja2.template('home/index.html')
    async def post(self):
        name = (await self.request.post()).get('name')
        print(name)
        note = await service.create(name)
        print('complete')
