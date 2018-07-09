import sys
import os
import pkgutil
import logging
from aiohttp import web
from {{cookiecutter.project_slug}}.middlewares import correlation_id, render_json
from {{cookiecutter.project_slug}}.urls import routes


def autoload(module):
    dirname = os.path.dirname(pkgutil.get_loader(module).get_filename())
    for path, directories, files in os.walk(dirname):
        for importer, package_name, _ in pkgutil.iter_modules([path]):
            importer.find_module(package_name).load_module(package_name)


async def create():
    autoload('{{cookiecutter.project_slug}}.views')
    # ap = argparse.ArgumentParser()
    # init logging
    logging.basicConfig(level=logging.DEBUG)
    # setup application and extensions
    app = web.Application()
    app.router.add_routes(routes)
    app.middlewares.append(web.normalize_path_middleware(append_slash=True))
    app.middlewares.append(correlation_id)
    app.middlewares.append(render_json)
    return app


def main(argv):
    web.run_app(create(), host='localhost', port='7456')


if __name__ == '__main__':
    main(sys.argv[1:])