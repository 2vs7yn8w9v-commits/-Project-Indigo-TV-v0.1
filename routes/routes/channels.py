from fastapi import APIRouter
from sample_data import channels

router = APIRouter(
    prefix="/channels",
    tags=["Channels"]
)


@router.get("/")
def get_channels():
    return channels
