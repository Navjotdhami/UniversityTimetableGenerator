from dataclasses import dataclass


@dataclass
class Room:

    room_id: str

    room_type: str

    capacity: int