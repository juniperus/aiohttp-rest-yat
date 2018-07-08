from aiohttp import web
import logging
import uuid


@web.middleware
async def render_json(request, handler):
    response = await handler(request)
    return web.json_response(response)

@web.middleware
async def correlation_id(request, handler):
    response = await handler(request)
    response.headers['X-Request-ID'] = request.headers.get('X-Request-ID', uuid.uuid4())
    return response