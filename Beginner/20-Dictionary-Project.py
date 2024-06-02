Course = {
    "title": "Python Course",
    "teacher": "Mohammad Ordukhani",
    "Time": 8.5,
    "videoCount": 30,
    "tags": ["python", "online course", "free python course"],
    "short_link": "toplearn.com/c/ovlc",
    "sessions": [
        {
            "title": "session-1",
            "time": 5

        },
        {
            "title": "session-2",
            "time": 7

        },
        {
            "title": "session-4",
            "time": 9

        }
    ],
    "relatedCourses": [
        {
            "title": "Java Course",
            "teacher": "Mohammad Ghari",
            "Time": 20,
            "videoCount": 42,
            "tags": ["Java", "online course", "free java course"],
            "short_link": "toplearn.com/c/ovlc",
        },
        {
            "title": "CSharp Course",
            "teacher": "Iman Madaeni",
            "Time": 8,
            "videoCount": 22,
            "tags": ["CSharp", "online course", "free CSharp course"],
            "short_link": "toplearn.com/c/ovlc",
        }
    ]
}
print(Course["relatedCourses"])

for related in Course["relatedCourses"]:
    print(related)

for related in Course["relatedCourses"]:
    print(related["title"])

totalTime=0
for sesseion in Course["sessions"]:
    totalTime+=sesseion["time"]

print(f"total teaching time is:{totalTime}")
