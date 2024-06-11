from aiogram import Router
from for_user.youtube_downloader import router as yt_router


router = Router(name=__name__)

router.include_routers(
    yt_router
)