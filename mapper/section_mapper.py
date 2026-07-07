from mapper.base_mapper import BaseMapper
from models.section import Section


class SectionMapper(BaseMapper):

    def map_sections(self):

        sections = {}

        for _, row in self.df.iterrows():

            section_id = self.get_str(row, "FINAL SECTION")

            if section_id == "":
                section_id = self.get_str(row, "Section")

            if section_id == "":
                continue

            if section_id not in sections:

                sections[section_id] = Section(

                    section_id=section_id,

                    school=self.get_str(row, "School"),

                    program=self.get_str(row, "Program"),

                    year=self.get_str(row, "Year"),

                    term=self.get_str(row, "Term"),

                    student_count=self.get_int(row, "No of Students")

                )

        return list(sections.values())