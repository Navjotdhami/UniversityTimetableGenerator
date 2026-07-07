from validator.course_validator import CourseValidator
from validator.room_validator import RoomValidator
from validator.faculty_validator import FacultyValidator
from validator.validation_report import ValidationReport


class DataValidator:

    def __init__(self, dataframe):

        self.df = dataframe

    def validate(self):

        report = ValidationReport()

        report.start()

        CourseValidator(self.df).validate()

        RoomValidator().validate()

        FacultyValidator().validate()

        report.end()