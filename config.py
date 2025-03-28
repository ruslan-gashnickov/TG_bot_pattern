import os
from dataclasses import dataclass, field
from typing import List
from dotenv import load_dotenv


load_dotenv()

def get_admin_ids() -> List[int]:
    admin_ids_str = os.getenv("ADMIN_IDS", "")
    return [int(id) for id in admin_ids_str.split(",") if id]


@dataclass
class Config:
    BOT_TOKEN: str = os.getenv("BOT_TOKEN")
    ADMIN_IDS: List[int] = field(default_factory=get_admin_ids)
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///database.db")



config = Config()