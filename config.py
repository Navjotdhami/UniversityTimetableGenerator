# ==========================================================
# UNIVERSITY CONFIGURATION
# ==========================================================

WORKING_DAYS = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday"
]

PERIODS = [
    1,2,3,4,5,6,7,8
]

PERIOD_TIMES = {

    "8-4":[
        "08:00-08:50",
        "08:50-09:40",
        "09:50-10:40",
        "10:40-11:30",
        "12:00-12:50",
        "12:50-01:40",
        "02:30-03:20",
        "03:20-04:10"
    ],

    "9-5":[
        "09:00-09:50",
        "09:50-10:40",
        "10:50-11:40",
        "11:40-12:30",
        "01:20-02:10",
        "02:10-03:00",
        "03:10-04:00",
        "04:00-04:50"
    ],

    "10-6":[
        "10:00-10:50",
        "10:50-11:40",
        "11:50-12:40",
        "12:40-01:30",
        "02:20-03:10",
        "03:10-04:00",
        "04:10-05:00",
        "05:00-05:50"
    ]
}

MAX_FACULTY_LOAD = 23

MAX_LAB_STRENGTH = 36

LAB_DURATION = 2

WORKING_DAYS_COUNT = 5

# -------------------------------------------------------
# Fixed Open Minor Slots
# -------------------------------------------------------

OPEN_MINOR = {

    "3": [5,6],

    "4": [7,8]
}

# -------------------------------------------------------
# Courses that MUST be scheduled in ECE Labs
# -------------------------------------------------------

ECE_COURSES = {

"BASIC ELECTRICAL AND ELECTRONICS ENGINEERING",

"BASIC ELECTRICAL AND ELECTRONICS ENGINEERING LABORATORY",

"PRINCIPLES OF ELECTRONICS",

"PRINCIPLES OF ELECTRONICS LABORATORY",

"ELECTRONICS FOR ROBOTS",

"DIGITAL ELECTRONICS"

}