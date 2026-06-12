def generate_timetable(focus, study_time):

    if study_time == "Morning":
        times = [
            "6:00 AM - 8:00 AM",
            "8:00 AM - 9:00 AM",
            "9:00 AM - 10:00 AM",
            "10:00 AM - 11:00 AM"
        ]

    elif study_time == "Evening":
        times = [
            "6:00 PM - 8:00 PM",
            "8:00 PM - 9:00 PM",
            "9:00 PM - 10:00 PM",
            "10:00 PM - 11:00 PM"
        ]

    else:
        times = [
            "9:00 PM - 11:00 PM",
            "11:00 PM - 12:00 AM",
            "12:00 AM - 1:00 AM",
            "1:00 AM - 2:00 AM"
        ]

    if focus == "DSA":

        activities = [
            "DSA",
            "Aptitude",
            "Projects",
            "CS Fundamentals"
        ]

    elif focus in [
        "ML Foundations",
        "ML Projects",
        "Deep Learning"
    ]:

        activities = [
            "ML Learning",
            "Python",
            "Projects",
            "Mathematics"
        ]

    elif focus == "Research":

        activities = [
            "Research Papers",
            "Literature Review",
            "Implementation",
            "Documentation"
        ]

    elif focus == "Core Subjects":

        activities = [
            "Operating Systems",
            "DBMS",
            "Computer Networks",
            "Aptitude"
        ]

    elif focus == "Mock Tests":

        activities = [
            "Mock Test",
            "Analysis",
            "Weak Topics",
            "Revision"
        ]

    elif focus == "Interviews":

        activities = [
            "DSA Revision",
            "Mock Interview",
            "Projects",
            "HR Preparation"
        ]

    elif focus == "Academics":

        activities = [
            "College Subjects",
            "Assignments",
            "Revision",
            "Notes"
        ]

    elif focus == "CP":

        activities = [
            "Problem Solving",
            "Algorithms",
            "Contest Practice",
            "Revision"
        ]

    elif focus == "GRE Prep":

        activities = [
            "Quantitative Aptitude",
            "Verbal Ability",
            "Reading",
            "Mock Test"
        ]

    else:

        activities = [
            focus,
            "Practice",
            "Revision",
            "Notes"
        ]

    timetable = []

    for i in range(4):
        timetable.append(
            [times[i], activities[i]]
        )

    return timetable