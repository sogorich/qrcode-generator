from starlette.staticfiles import StaticFiles
from starlette.routing import Route, Mount

from .views import home_page


def get_routes() -> list[Route | Mount]:
	""" Возвращает список роутов. """

	return [
		Route('/', home_page),
		Mount('/static', app=StaticFiles(directory='static'), name='static'),
	] 