from fastapi import APIRouter
from sample_data import episodes

router = APIRouter(
    prefix="/search",
    tags=["Search"]
)


@router.get("/")
def search(q: str):
    results = []

    for episode in episodes:
        if q.lower() in episode["title"].lower():
            results.append(episode)

    return results
