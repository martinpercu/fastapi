from pydantic import BaseModel, Field
from typing import Optional, List






class Film(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=5, max_length=35)
    overview: str = Field(min_length=12, max_length=200)
    year: int = Field(default=1987, le=2023)
    rating: float = Field(ge=1, le=10)
    category: str = Field(min_length=5, max_length=16)

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "title": "Nom du film",
		        "overview": "Bla bla bla descrition du notre film",
		        "year": 1980,
		        "rating": 8.6,
		        "category": "Comedie"
            },
        }
