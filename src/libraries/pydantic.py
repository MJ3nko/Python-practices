from typing import List, Optional
from pydantic import BaseModel, Field


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
    results: List[SearchItem] = Field(default_factory=list)
    episodes: List[SearchItem] = Field(default_factory=list)
