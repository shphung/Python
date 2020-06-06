'''
    File: ListAndTupleStructures.py
    Author: Steven Phung
    Purpose: Working with unsorted list and tuple structures
    Given three unsorted lists, a name list (e.g. nameList = ["Betty", 
    "Andrew", "Zach", "Cathy", ...]), and Exam1 score list (e.g. score1 = 
    [50, 45, 48, 48, ...]), and an Exam2 score list (e.g. score2 = [35, 48, 50,
    37, ...]) write the following functions:
        
    (1) makeList(aNameList, e1ScoreList, e2ScoreList): function will return
    tuples in the following form:
    [("Betty", (50,35)), ("Andrew", (45,48)), ("Zach", (48,50)), ("Cathy", (48,37)), ...].
        
    (2) personalAverage(aList): takes a class list in the form of:
    [("Betty", (50,35)), ("Andrew", (45,48)), ...] and returns another class list in the form:
    [("Betty", (42.5)), ("Andrew", (46.5)), ...].
    
    (3) sortByName(bList): takes a class list in the form of:
    [("Betty", (42.5)), ("Andrew", (46.5)), ...] and returns another class list in the form:
    [("Andrew", (46.5)), ("Betty", (42.5)), ...]. i.e. sort by name in ascending order.
    
    (4) sortByAverageScore(bList): takes a class list in the form of:
    [("Betty", (42.5)), ("Andrew", (46.5)), ...] and returns another class list in the form:
    [("Zach", (48.0)), ("Andrew", (46.5)), ...]. i.e. sort by average score in descending order.
        
    (5) classMean(aList): takes a class list in the form of:
    [("Betty", (50,35)), ("Andrew", (45,48)), ...] and returns the exam1MeanScore
    and exam2MeanScore for the class.
    
    (6) classMedian(aList): similar to (5) but returns the exam1MedianScore and
    exam2MedianScore.
    
    (7) classStandardDeviation(aList): similar to (5) but returns the standard
    deviation for Exam1 and Exam2 respectively
    
    (8) main(): test all above functions
'''
import math
import sys

#Data sets for testing
nameList = ["Betty", "Andrew", "Zach", "Cathy", "Jay", "Kevin", "Cassie", "Matt", "Lux", "Xavier", "Peter", "John", "Jamie", "Joe", "Ellen", "Nancy", "Ray", "Bryce", "Gordon", "Gee"]
exam1Scores = [50, 45, 48, 48, 46, 49, 35, 38, 42, 50, 44, 37, 35, 32, 48, 32, 44, 45, 41, 46]
exam2Scores = [35, 48, 50, 37, 45, 41, 47, 50, 47, 41, 47, 48, 46, 49, 41, 38, 46, 42, 33, 39]

nameList2 = []
exam1Scores2 = []
exam2Scores2 = []

nameList3 = ['A', 'D', 'W', 'K', 'Z']
exam1Scores3 = [30, 20, 50]
exam2Scores3 = [50, 30, 25, 49, 23, 42]

#Function: makeList(list, list, list)
#Purpose: Given a list of names and two scores, all of equal length, merge into
#a new list where the scores are a tuple, and the student is a tuple with its scores
def makeList(aNameList, e1ScoreList, e2ScoreList) :
    #Terminate program if not given a list
    if not aNameList :
        sys.exit("Empty list... Terminating.")
    #All 3 lists must be equal length
    elif len(aNameList) == len(e1ScoreList) and len(e1ScoreList) == len(e2ScoreList) : 
        classList = []
        for x in range(len(aNameList)) :
            #Tuple of scores
            scoreTup = (e1ScoreList[x], e2ScoreList[x])
            #Tuple of name and scores
            studentTup = (aNameList[x], scoreTup)
            classList.append(studentTup)
        return classList
    else :
        sys.exit("Missing data... Terminating.")
        
#Function: personalAverage(list)
#Purpose: Given a formatted list, return a new list with scores averaged
def personalAverage(aList) :
    newClassList = []
    for x in range(len(aList)) :
        #tuple of the name and average of the two scores
        studentTup = (aList[x][0], (aList[x][1][0] + aList[x][1][1]) / 2)
        newClassList.append(studentTup)
    return newClassList
    
#Function: sortByName(list)
#Purpose: Given a formatted list, return a new list with the same format, but
#sorted by first name A-Z.
def sortByName(bList) :
    newClassList = []
    nameList = []
    
    #Get names and sort
    for x in range(len(bList)) :
        nameList.append(bList[x][0])
    nameList.sort()
    
    #Based on sorted nameList's alphabetical order, whenever the same name
    #is found in bList, add that element to the new list, after all names are
    #added, the final new list will be sorted in alphabetical order.
    found = 0
    while found < len(bList) :
        for x in range(len(bList)) :
            if found == len(bList) :
                break
            #Name[] is not added until we find a match
            #Name[] is also not incremented until we find a match
            #This keeps the alphabetical order correct
            if nameList[found] is bList[x][0] :
                found += 1
                studentTup = (bList[x])
                newClassList.append(studentTup)
    return newClassList
    
#Function sortByAverageScore(list)
#Purpose: Given a formatted list, return a new list with the same format, but
#sorted by sort from greatest value to least value.
def sortByAverageScore(bList) :
    newClassList = []
    scoreList = []
    
    #Get scores and sort, then reverse order to get greatest to least
    for x in range(len(bList)) :
        scoreList.append(bList[x][1])
    scoreList.sort()
    scoreList.reverse()
    
    #Based on sorted scoreList's order, whenever the same score is found in
    #bList, add that element to the new list, after all scores added, the final
    #new list will be sorted from greatest to least.
    found = 0
    while found < len(bList) :
        for x in range(len(bList)) :
            if found == len(bList) :
                break
            #Score[] is not added until we find a match
            #Score[] is also not incremented until we find a match
            #This keeps the correct order
            if scoreList[found] == bList[x][1] :
                found += 1
                studentTup = (bList[x])
                newClassList.append(studentTup)
    return newClassList
    
#Function: classMean(list)
#Purpose: Given our formatted list, find the mean for both scores
def classMean(aList) :
    exam1ScoreList = []
    exam2ScoreList = []
    
    #Get the scores for exam 1 and exam 2
    for x in range(len(aList)) :
        exam1ScoreList.append(aList[x][1][0])
        exam2ScoreList.append(aList[x][1][1])
    
    #Find total value
    totalExam1 = 0;
    totalExam2 = 0;
    for x in range(len(exam1ScoreList)) :
        totalExam1 += exam1ScoreList[x]
        totalExam2 += exam2ScoreList[x]
        
    #Return averages
    return totalExam1 / len(exam1ScoreList), totalExam2 / len(exam2ScoreList)
    
#Function: classMedian(list)
#Purpose: Given our formatted list, find the median for both scores
def classMedian(aList) :
    exam1ScoreList = []
    exam2ScoreList = []
    
    #Get the scores for exam 1 and exam 2
    for x in range(len(aList)) :
        exam1ScoreList.append(aList[x][1][0])
        exam2ScoreList.append(aList[x][1][1])
    exam1ScoreList.sort()
    exam2ScoreList.sort()
    
    #If the number of elements in the list is even, median will be the summation
    #of the two middle values divided by 2
    if len(exam1ScoreList) % 2 == 0 :
        return ((exam1ScoreList[(len(exam1ScoreList)//2)-1] + exam1ScoreList[(len(exam1ScoreList)//2)])/2), ((exam2ScoreList[(len(exam2ScoreList)//2)-1] + exam2ScoreList[(len(exam2ScoreList)//2)])/2)
    #If the number of elements is odd, the middle element is the median
    else :
        return exam1ScoreList[len(exam1ScoreList)//2], exam2ScoreList[len(exam2ScoreList)//2]
    
#Function: classStandardDeviation(list)
#Purpose: Given our formatted list, find the standard deviation for both scores
def classStandardDeviation(aList) :
    exam1ScoreList = []
    exam2ScoreList = []
    
    #Get the scores
    for x in range(len(aList)) :
        exam1ScoreList.append(aList[x][1][0])
        exam2ScoreList.append(aList[x][1][1])
    
    #1. Find the mean values
    exam1Mean, exam2Mean = classMean(aList)
    
    squaredDifferences1 = []
    squaredDifferences2 = []
    #2. For each number, subtract the mean and then square the result
    for x in range(len(exam1ScoreList)) :
        squaredDifferences1.append((exam1ScoreList[x] - exam1Mean)**2)
        squaredDifferences2.append((exam2ScoreList[x] - exam2Mean)**2)
    
    #Get total to find mean of new values
    total1 = 0
    total2 = 0
    for x in range(len(exam1ScoreList)) :
        total1 += squaredDifferences1[x]
        total2 += squaredDifferences2[x]
        
    #3. Find the mean of the squared differences
    meanOfSquaredDifferences1 = total1 / len(squaredDifferences1)
    meanOfSquaredDifferences2 = total2 / len(squaredDifferences2)
    
    #4. Take the square root of our new means, which gives us standard deviation
    return math.sqrt(meanOfSquaredDifferences1), math.sqrt(meanOfSquaredDifferences2)

if __name__ == "__main__" :
    #Test case 1
    list = makeList(nameList, exam1Scores, exam2Scores)
    print("------------------------------------------")
    print("List:")
    print(list)
    
    print("------------------------------------------")
    personalAverageList = personalAverage(list)
    print("Personal Average List:")
    print(personalAverageList)
    
    print("------------------------------------------")
    sortedByNameList = sortByName(personalAverageList)
    print("Sorted By Name List:")
    print(sortedByNameList)
    
    print("------------------------------------------")
    sortedByAverageScore = sortByAverageScore(personalAverageList)
    print("Sorted by Average Score List:")
    print(sortedByAverageScore)
    
    print("------------------------------------------")
    exam1Mean, exam2Mean = classMean(list)
    print("Exam 1 Mean:",exam1Mean, "\nExam 2 Mean:", exam2Mean)
    
    print("------------------------------------------")
    exam1Median, exam2Median = classMedian(list)
    print("Exam 1 Median:", exam1Median, "\nExam 2 Median:", exam2Median)
    
    print("------------------------------------------")
    exam1StandardDeviation, exam2StandardDeviation = classStandardDeviation(list)
    print("Exam 1 Standard Deviation",exam1StandardDeviation, "\nExam 2 Standard Deviation", exam2StandardDeviation)
    print("------------------------------------------")
    
    #Test case 2
#    list = makeList(nameList2, exam1Scores2, exam2Scores2)
#    print("------------------------------------------")
#    print("List:")
#    print(list)
#    
#    print("------------------------------------------")
#    personalAverageList = personalAverage(list)
#    print("Personal Average List:")
#    print(personalAverageList)
#    
#    print("------------------------------------------")
#    sortedByNameList = sortByName(personalAverageList)
#    print("Sorted By Name List:")
#    print(sortedByNameList)
#    
#    print("------------------------------------------")
#    sortedByAverageScore = sortByAverageScore(personalAverageList)
#    print("Sorted by Average Score List:")
#    print(sortedByAverageScore)
#    
#    print("------------------------------------------")
#    exam1Mean, exam2Mean = classMean(list)
#    print("Exam 1 Mean:",exam1Mean, "\nExam 2 Mean:", exam2Mean)
#    
#    print("------------------------------------------")
#    exam1Median, exam2Median = classMedian(list)
#    print("Exam 1 Median:", exam1Median, "\nExam 2 Median:", exam2Median)
#    
#    print("------------------------------------------")
#    exam1StandardDeviation, exam2StandardDeviation = classStandardDeviation(list)
#    print("Exam 1 Standard Deviation",exam1StandardDeviation, "\nExam 2 Standard Deviation", exam2StandardDeviation)
    
    #Test case 3
#    list = makeList(nameList3, exam1Scores3, exam2Scores3)
#    print("------------------------------------------")
#    print("List:")
#    print(list)
#    
#    print("------------------------------------------")
#    personalAverageList = personalAverage(list)
#    print("Personal Average List:")
#    print(personalAverageList)
#    
#    print("------------------------------------------")
#    sortedByNameList = sortByName(personalAverageList)
#    print("Sorted By Name List:")
#    print(sortedByNameList)
#    
#    print("------------------------------------------")
#    sortedByAverageScore = sortByAverageScore(personalAverageList)
#    print("Sorted by Average Score List:")
#    print(sortedByAverageScore)
#    
#    print("------------------------------------------")
#    exam1Mean, exam2Mean = classMean(list)
#    print("Exam 1 Mean:",exam1Mean, "\nExam 2 Mean:", exam2Mean)
#    
#    print("------------------------------------------")
#    exam1Median, exam2Median = classMedian(list)
#    print("Exam 1 Median:", exam1Median, "\nExam 2 Median:", exam2Median)
#    
#    print("------------------------------------------")
#    exam1StandardDeviation, exam2StandardDeviation = classStandardDeviation(list)
#    print("Exam 1 Standard Deviation",exam1StandardDeviation, "\nExam 2 Standard Deviation", exam2StandardDeviation)


    
'''
Test case #1
runfile('E:/Steven/CSU Pomona Files/Year 6/17 Spring 2020/CS2520 [Python]/Assignment 3/Assignment3.py', wdir='E:/Steven/CSU Pomona Files/Year 6/17 Spring 2020/CS2520 [Python]/Assignment 3')
------------------------------------------
List:
[('Betty', (50, 35)), ('Andrew', (45, 48)), ('Zach', (48, 50)), ('Cathy', (48, 37)), ('Jay', (46, 45)), ('Kevin', (49, 41)), ('Cassie', (35, 47)), ('Matt', (38, 50)), ('Lux', (42, 47)), ('Xavier', (50, 41)), ('Peter', (44, 47)), ('John', (37, 48)), ('Jamie', (35, 46)), ('Joe', (32, 49)), ('Ellen', (48, 41)), ('Nancy', (32, 38)), ('Ray', (44, 46)), ('Bryce', (45, 42)), ('Gordon', (41, 33)), ('Gee', (46, 39))]
------------------------------------------
Personal Average List:
[('Betty', 42.5), ('Andrew', 46.5), ('Zach', 49.0), ('Cathy', 42.5), ('Jay', 45.5), ('Kevin', 45.0), ('Cassie', 41.0), ('Matt', 44.0), ('Lux', 44.5), ('Xavier', 45.5), ('Peter', 45.5), ('John', 42.5), ('Jamie', 40.5), ('Joe', 40.5), ('Ellen', 44.5), ('Nancy', 35.0), ('Ray', 45.0), ('Bryce', 43.5), ('Gordon', 37.0), ('Gee', 42.5)]
------------------------------------------
Sorted By Name List:
[('Andrew', 46.5), ('Betty', 42.5), ('Bryce', 43.5), ('Cassie', 41.0), ('Cathy', 42.5), ('Ellen', 44.5), ('Gee', 42.5), ('Gordon', 37.0), ('Jamie', 40.5), ('Jay', 45.5), ('Joe', 40.5), ('John', 42.5), ('Kevin', 45.0), ('Lux', 44.5), ('Matt', 44.0), ('Nancy', 35.0), ('Peter', 45.5), ('Ray', 45.0), ('Xavier', 45.5), ('Zach', 49.0)]
------------------------------------------
Sorted by Average Score List:
[('Zach', 49.0), ('Andrew', 46.5), ('Jay', 45.5), ('Xavier', 45.5), ('Peter', 45.5), ('Ray', 45.0), ('Kevin', 45.0), ('Lux', 44.5), ('Ellen', 44.5), ('Matt', 44.0), ('Bryce', 43.5), ('Gee', 42.5), ('Betty', 42.5), ('Cathy', 42.5), ('John', 42.5), ('Cassie', 41.0), ('Jamie', 40.5), ('Joe', 40.5), ('Gordon', 37.0), ('Nancy', 35.0)]
------------------------------------------
Exam 1 Mean: 42.75 
Exam 2 Mean: 43.5
------------------------------------------
Exam 1 Median: 44.5 
Exam 2 Median: 45.5
------------------------------------------
Exam 1 Standard Deviation 5.795472370739075 
Exam 2 Standard Deviation 5.014977567247933
------------------------------------------
'''

'''
Test case #2
An exception has occurred, use %tb to see the full traceback.

SystemExit: Empty list... Terminating.
'''

'''
Test case #3
An exception has occurred, use %tb to see the full traceback.

SystemExit: Missing data... Terminating.
'''