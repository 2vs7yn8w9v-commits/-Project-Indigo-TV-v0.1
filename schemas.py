from pydantic import BaseModel


class Channel(BaseModel):
    id: str
    title: str
    description: str
    banner: str
    stunt: bool

    class Config:
        from_attributes = True


class Episode(BaseModel):
    id: str
    channel_id: str
    season: int
    episode: int
    title: str
    description: str
    thumbnail: str
    stream_url: str

    class Config:
        from_attributes = True
    
