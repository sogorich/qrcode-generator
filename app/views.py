from starlette.requests import Request
from starlette.background import BackgroundTask
from starlette.responses import HTMLResponse

from .services import create_qr_code, delete_qrcode_file
from .config import BASE_SLEEP_FOR_BG_TASKS


async def home_page(request: Request) -> HTMLResponse:
	""" Cтраница на которой отображается qr code. """

	filename_path, = await create_qr_code(
		request.query_params.get('content', 'No content'))

	task = BackgroundTask(delete_qrcode_file, 
		path=filename_path, 
		sleep=BASE_SLEEP_FOR_BG_TASKS)

	return HTMLResponse(f'<img src="{filename_path}" alt="qrcode" />', background=task)