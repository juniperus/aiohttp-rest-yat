from aiohttp import web
import uuid


@web.middleware
async def render_json(request, handler):
    response = await handler(request)
    return web.json_response(response)


@web.middleware
async def correlation_id(request, handler):
    response = await handler(request)
    response.headers['X-Request-ID'] = request.headers.get('X-Request-ID', str(uuid.uuid4()))
    return response