from pydantic import BaseModel, Field
from typing import Annotated, List
from annotated_types import Len
from datetime import datetime

class Reading(BaseModel):
    timestamp: datetime
    count: int

class Device(BaseModel):
    id: str
    readings: Annotated[List[Reading], Len(min_length=1)]

    def add(self, reading: Reading) -> None:
        # check if timestamp already exists in readings before adding to avoid duplicates
        if not any(r.timestamp == reading.timestamp for r in self.readings):
            self.readings.append(reading)

    def sum(self) -> int:
        # add up all the counts
        return sum(reading.count for reading in self.readings)

    def get_latest_timestamp(self) -> str:
        # get the max timestamp
        latest_reading = max(r.timestamp for r in self.readings)
        return latest_reading.isoformat()

class InMemoryDevices(BaseModel):
    devices: dict[str, Device] = Field(default_factory=dict)
