from starlette.applications import Starlette

from app.urls import get_routes
from app.config import DEBUG_MODE

	
app = Starlette(
	debug=DEBUG_MODE, 
	routes=get_routes()
)