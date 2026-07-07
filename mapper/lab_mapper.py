from mapper.base_mapper import BaseMapper
from models.lab import Lab


class LabMapper(BaseMapper):

    def map_labs(self):

        labs = []

        seen = set()

        for _, row in self.df.iterrows():

            lab_id = self.get_str(row, "Lab number")

            if lab_id == "":
                continue

            if lab_id in seen:
                continue

            seen.add(lab_id)

            lab = Lab(

                lab_id=lab_id,

                lab_type=self.get_str(row, "Type")

            )

            labs.append(lab)

        return labs