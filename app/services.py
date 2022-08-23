import asyncio
import hashlib
import qrcode
import pathlib
	
from .config import PATH_TO_IMAGES


async def delete_qrcode_file(path: str, sleep: int) -> None:
	""" Удаляет qr code из статических файлов после истечения времени задержки. """

	try:
		file = pathlib.Path(path)

		await asyncio.sleep(sleep)
	
		file.unlink()

	except (FileNotFoundError, Exception):
		print('Удаление невозможно так как отсутствует файл для qr code.')


async def create_qr_code(content: str) -> tuple[str]:
	""" Генерирует qr code и сохраняет его в статику. """

	filename = hashlib.sha256(bytes(content, encoding='utf-8')).hexdigest()
	filename_path = f'{PATH_TO_IMAGES}/{filename}.png'

	img = qrcode.make(content)
	img.save(filename_path)

	return (filename_path,)