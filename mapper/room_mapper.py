from mapper.base_mapper import BaseMapper
from models.room import Room


class RoomMapper(BaseMapper):

    def map_rooms(self):

        rooms = []

        seen = set()

        for _, row in self.df.iterrows():

            room_id = self.get_str(row, "Room Number")

            if room_id == "":
                continue

            if room_id in seen:
                continue

            seen.add(room_id)

            room = Room(

                room_id=room_id,

                room_type=self.get_str(row, "Type"),

                capacity=self.get_int(row, "Capacity")

            )

            rooms.append(room)

        return rooms