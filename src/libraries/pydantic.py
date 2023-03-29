import pydantic
from pydantic import BaseModel

from typing import List, Optional


class SearchItem(BaseModel):
    category: str
    id: Optional[int]
    item_id: Optional[int]
    url: str
    title: str
    description: str


class SearchResponse(BaseModel):
    elapsed_ms: float
    keywords: List[str]
    results: List[SearchItem] = pydantic.Field(default_factory=list)
    episodes: List[SearchItem] = pydantic.Field(default_factory=list)
