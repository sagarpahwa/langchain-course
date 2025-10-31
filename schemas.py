from typing import List

from pydantic import BaseModel, Field


class Source(BaseModel):
    """Schema of a source used by the agent"""

    url: str = Field(description="The url of the source")


class AgentResponse(BaseModel):
    """Schema of the response from the agent"""

    sources: List[Source] = Field(
        default_factory=list, description="The sources used by the agent"
    )
    answer: str = Field(description="The agent's answer to the query")
