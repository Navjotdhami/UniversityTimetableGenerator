from loader.load_complete_data import LoadCompleteData

from validator.data_validator import DataValidator

from mapper.course_mapper import CourseMapper
from mapper.section_mapper import SectionMapper

from core.university_database import UniversityDatabase
from core.scheduler_context import SchedulerContext

from scheduler.scheduler_engine import SchedulerEngine
from scheduler.activity_generator import ActivityGenerator


def main():

    print("=" * 60)
    print("University Timetable Generator")
    print("=" * 60)

    # ---------------------------------------------------------
    # Load Excel Data
    # ---------------------------------------------------------

    loader = LoadCompleteData()

    dataframe = loader.load()

    # ---------------------------------------------------------
    # Validate Data
    # ---------------------------------------------------------

    validator = DataValidator(dataframe)

    validator.validate()

    # ---------------------------------------------------------
    # Map Courses
    # ---------------------------------------------------------

    course_mapper = CourseMapper(dataframe)

    courses = course_mapper.map_courses()

    # ---------------------------------------------------------
    # Map Sections
    # ---------------------------------------------------------

    section_mapper = SectionMapper(dataframe)

    sections = section_mapper.map_sections()

    # ---------------------------------------------------------
    # Build University Database
    # ---------------------------------------------------------

    database = UniversityDatabase()

    database.courses = courses
    database.sections = sections

    # Faculties, Rooms and Labs will be added
    # after their respective mappers are created.

    # ---------------------------------------------------------
    # Database Summary
    # ---------------------------------------------------------

    print("\n" + "=" * 60)
    print("UNIVERSITY DATABASE SUMMARY")
    print("=" * 60)

    print(f"Courses   : {len(database.courses)}")
    print(f"Sections  : {len(database.sections)}")
    print(f"Faculties : {len(database.faculties)}")
    print(f"Rooms     : {len(database.rooms)}")
    print(f"Labs      : {len(database.labs)}")

    # ---------------------------------------------------------
    # Scheduler Context
    # ---------------------------------------------------------

    context = SchedulerContext()

    context.courses = database.courses
    context.sections = database.sections
    context.faculties = database.faculties
    context.rooms = database.rooms
    context.labs = database.labs

    # ---------------------------------------------------------
    # Initialize Scheduler
    # ---------------------------------------------------------

    engine = SchedulerEngine(context)

    engine.initialize()

    # ---------------------------------------------------------
    # Generate Activities
    # ---------------------------------------------------------

    activity_generator = ActivityGenerator(database.courses)

    activities = activity_generator.generate()

    # Store generated activities in scheduler context
    context.activities = activities

    print("\nTotal Activities :", len(activities))

    print("\nFirst Five Activities\n")

    for activity in activities[:5]:
        print(activity)

    # ---------------------------------------------------------
    # Sample Output
    # ---------------------------------------------------------

    print("\nTotal Sections :", len(sections))

    print("\nFirst Five Sections\n")

    for section in sections[:5]:
        print(section)


if __name__ == "__main__":
    main()