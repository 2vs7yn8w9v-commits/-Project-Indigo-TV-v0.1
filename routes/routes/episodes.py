from fastapi import APIRouter
from sample_data import episodes

router = APIRouter(
    prefix="/episodes",
    tags=["Episodes"]
)


@router.get("/")
def get_episodes():
    return episodes


@router.get("/{episode_id}")
def get_episode(episode_id: str):
    for episode in episodes:
        if episode["id"] == episode_id:
            return episode

    return {"error": "Episode not found"}
