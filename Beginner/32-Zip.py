number_1 = [1, 2, 3, 4, 5, 6, 7]
number_2 = [8, 9, 10, 11,2,1,1]

result = zip(number_1, number_2)
print(list(result))
print(dict(result))

myList=[(1,5,7),(3,7,6),(6,4,4),(7,9,1)]
print(list(zip(*myList)))

students=["mohammad","iman","sara"]
midterm =[78,80,94]
final =[90,88,92]

# finalGrades=[max(pair) for pair in zip(midterm,final)]
finalGrades = {t[0]:max(t[1],t[2]) for t in zip(students,midterm,final)}
print(finalGrades)

finalGrades2=dict(zip(
    students, list(map(lambda pair:max(pair),zip(midterm,final)))
))
print(finalGrades2)

averageGrades=dict(zip(
    students, list(map(lambda pair:(pair[0]+pair[1])/2,zip(midterm,final)))
))
print(averageGrades)