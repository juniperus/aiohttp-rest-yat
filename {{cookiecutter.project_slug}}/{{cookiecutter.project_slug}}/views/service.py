from {{cookiecutter.project_slug}}.urls import routes
from aiohttp.web import View


@routes.view("/example")
class ExampleView(View):

    async def get(self):
        pass
    
    async def post(self):
        pass