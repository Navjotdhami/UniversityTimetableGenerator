from models.activity import Activity


class ActivityGenerator:

    def __init__(self, courses):

        self.courses = courses

    def generate(self):

        activities = []

        for course in self.courses:

            # --------------------------
            # Lectures
            # --------------------------

            for i in range(course.lecture_hours):

                activities.append(

                    Activity(

                        activity_id=f"{course.course_code}_L{i+1}",

                        course_code=course.course_code,

                        course_title=course.course_title,

                        section=course.section,

                        faculty_uid=course.uid,

                        activity_type="Lecture",

                        duration=1,

                        group_no=0,

                        total_groups=1,

                        students=course.student_count,

                        room_type="CLASSROOM",

                        shift=course.shift,

                    )

                )

            # --------------------------
            # Tutorials
            # --------------------------

            for i in range(course.tutorial_hours):

                activities.append(

                    Activity(

                        activity_id=f"{course.course_code}_T{i+1}",

                        course_code=course.course_code,

                        course_title=course.course_title,

                        section=course.section,

                        faculty_uid=course.uid,

                        activity_type="Tutorial",

                        duration=1,

                        group_no=0,

                        total_groups=1,

                        students=course.student_count,

                        room_type="CLASSROOM",

                        shift=course.shift,

                    )

                )

            # --------------------------
            # Practical
            # --------------------------

            if course.practical_hours > 0:

                students = course.student_count

                groups = max(course.groups, 1)

                group_size = max(1, students // groups)

                if students % groups != 0:
                    group_size += 1

                for g in range(groups):

                    room_type = "LAB"

                    title = course.course_title.upper()

                    if "ELECTRONICS" in title or "ELECTRICAL" in title:

                        room_type = "ECE LAB"

                    elif "COMPUTER" in title:

                        room_type = "COMPUTER LAB"

                    elif course.course_type.upper() == "BYOD":

                        room_type = "BYOD"

                    activities.append(

                        Activity(

                            activity_id=f"{course.course_code}_P{g+1}",

                            course_code=course.course_code,

                            course_title=course.course_title,

                            section=course.section,

                            faculty_uid=course.uid,

                            activity_type="Practical",

                            duration=2,

                            group_no=g + 1,

                            total_groups=groups,

                            students=group_size,

                            room_type=room_type,

                            shift=course.shift,

                        )

                    )

        return activities