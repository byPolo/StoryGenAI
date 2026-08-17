from datetime import datetime
from typing import Any, List, Optional

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String, JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.database import Base

class Story(Base):
    __tablename__ = "stories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String, index=True)
    session_id: Mapped[Optional[str]] = mapped_column(String, index=True, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    nodes: Mapped[List["StoryNode"]] = relationship(back_populates="story")


class StoryNode(Base):
    __tablename__ = "story_nodes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    story_id: Mapped[int] = mapped_column(ForeignKey("stories.id"), index=True)
    content: Mapped[str] = mapped_column(String)
    is_root: Mapped[bool] = mapped_column(Boolean, default=False)
    is_ending: Mapped[bool] = mapped_column(Boolean, default=False)
    is_winning_ending: Mapped[bool] = mapped_column(Boolean, default=False)
    options: Mapped[List[dict[str, Any]]] = mapped_column(JSON, default=list)

    story: Mapped["Story"] = relationship(back_populates="nodes")
