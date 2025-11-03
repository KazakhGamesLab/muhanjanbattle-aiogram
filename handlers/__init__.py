from .start import router as start_router
from .users.register import router as registration_router

all_routers = [
    start_router,
    registration_router,
]

__all__ = ["start_router", "registration_router", "all_routers"]