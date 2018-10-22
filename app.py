from aiohttp import web

from create_app_db.create_app import create_app
from routers.add_routers import add_routers


if __name__ == "__main__":
    app = create_app()
    add_routers(app)
    web.run_app(app, port=8000)
