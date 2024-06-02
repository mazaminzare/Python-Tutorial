
# index

myCourse = ["Python", "Kotlin", "Ionic","Python", "Kotlin", "Ionic","Python", "Kotlin", "Ionic"]
index_kotlin=myCourse.index("Kotlin")
index_ionic=myCourse.index("Ionic")
index_ionic=myCourse.index("Python",0,3)
print(index_kotlin)

# Count
numberOfPython = myCourse.count("python")
print(numberOfPython)

myNumbers=[1,2,3,4,5,6,7,8,9,10]
print(myNumbers)
myNumbers.reverse()
print(myNumbers)

# sort()

unOrderdNumbers = [5,6,9,3,18,45,89]
print(unOrderdNumbers)
unOrderdNumbers.sort()
print(unOrderdNumbers)

# join

secondCourses= " - ".join(myCourse)
secondCourses= " , ".join(myCourse)
print(secondCourses)