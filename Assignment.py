__author__ = 'gp'

import numpy as np
import time
import sys
import re
from datetime import datetime as dt
from datetime import timedelta as dur
import time

"Global Variables for lecture duration and recitation duration"
c_dur = dur(minutes=80)
r_dur = dur(minutes=90)

"Input file name"
file = open('sample_data_set1', 'r')

"line break counter while reading from input file"
line_counter=0

#data from file
course_timings=[]
course_recitations=[]
course_details=[]
course_requirements=[]
ta_responsibilities=[]
ta_skills=[]

#print file.readlines()
for line in file:
    line = line.lower()
    if line in ['\n', '\r\n']:
        line_counter=line_counter+1
    else:
        #1
        if(line_counter==1):
            course_timings.append(line)

        #2
        if(line_counter==3):
            course_recitations.append(line)

        #3
        if(line_counter==5):
            course_details.append(line)

        #4
        if(line_counter==7):
            course_requirements.append(line)

        #5
        if(line_counter==9):
            ta_responsibilities.append(line)

        #6
        if(line_counter==11):
            ta_skills.append(line)

#1
# Course Details
# Time each course is taking place: Course name followed by list of days and times. Example:
# CSE101, Tue, 11:30, Th, 10:00

item_count = 0
for course_line in course_timings:
     temp_list = []
     course_info=course_line.split(",")
     #course name

     temp_data=""

     for i in range(0,len(course_info)-1):
        if(i==0):
            #0,1,2,3,4,5,6,7
            course_name = course_info[i]
            #print course_name
        else:
            #0,1,2,3,4,5,6,7
            if((i+1)%2==0):
                    #day_name and day_time
                    temp_data = (course_info[i].strip(),course_info[i+1].strip())
                    temp_list.append(temp_data)

     if(item_count == 0):
        course_timing_dict = dict({course_name: tuple(temp_list)})
     else:
        course_timing_dict.update({course_name: tuple(temp_list)})

     item_count = item_count + 1
     #print course_name + "::" + temp_data


#print "Course Timing Details"
#print "-------------------------"
#print course_timing_dict
#print ""

#2
#Course recitations: Course name followed by list of days and times of recitations (as above)
#Assume each recitation takes 90 minutes.
#CSE306, Mon, 2:30 PM
item_count = 0
for course_recitations_line in course_recitations:
     temp_list = []
     course_recitations_info=course_recitations_line.split(",")
     #course name

     for i in range(0,len(course_recitations_info)-1):
        if(i==0):
            course_name = course_recitations_info[i]
        else:
            #0,1,2,3,4,5,6,7
            if((i+1)%2==0):
                if(i==1):
                    #day_name and day_time
                    temp_data = (course_recitations_info[i].strip(),course_recitations_info[i+1].strip())
                    temp_list.append(temp_data)

     if(item_count == 0):
         course_recitations_dict = dict({course_name: tuple(temp_list)})
     else:
         course_recitations_dict.update({course_name: tuple(temp_list)})

     item_count = item_count + 1
     #print course_name + "::" + temp_data

#print course_recitations_dict

#3
#Course details: Course name followed by number of students enrolled and Boolean value
#indicating if TA has to attend lectures. Example:
#CSE101, 44, yes
course_details_dict = {}
item_count = 0
for course_details_line in course_details:
     course_details_info=course_details_line.split(",")
     #temp_list = []

     for i in range(0,len(course_details_info)-1):
        if(i==0):
            course_name = course_details_info[i]
        else:
            #0,1,2,3,4,5,6,7
            if((i+1)%2==0):
                if(i==1):
                #day_name and day_time
                    temp_data = (int(course_details_info[i].strip()),course_details_info[i+1].strip())
                    #temp_list.append(temp_data)
                    course_details_dict[course_name] = tuple(temp_data)
                    #course_details_dict = dict({course_name: tuple(temp_list)})

     #if(item_count == 0):

     #else:
     #    course_details_dict.update({course_name: tuple(temp_list)})

     item_count = item_count + 1
     #print course_name + "::" + temp_data

#print "Course Details"
#print "-------------------------"
#print course_details_dict

#4
#Course requirements: skills required from a TA of the course: course name followed by a list of
#skills. Example:
#CSE101, Java, C#, Awesome Hacking Skills
#print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
#print course_requirements
#print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

item_count = 0
for course_requirements_line in course_requirements:
     course_requirements_info=course_requirements_line.split(",")
     temp_list = []
     for i in range(0,len(course_requirements_info)):
        if(i==0):
            course_name = course_requirements_info[i].strip()
        else:
            temp_data = course_requirements_info[i].strip()
            temp_list.append(temp_data)

     if(item_count == 0):
         course_requirements_dict = dict({course_name: tuple(temp_list)})
     else:
         course_requirements_dict.update({course_name: tuple(temp_list)})

     item_count = item_count + 1
     #print course_name + "::" + temp_data

#print "Course Requirements"
#print "-------------------------"
#print course_requirements_dict
#print ""

#5
#TA responsibilities: TA name followed by list of days and times of classes TA is taking (no class
#names). Example:
#Mrs. Lauren Smith, Wed, 11:30
item_count = 0
ta_names = []
for ta_responsibilities_line in ta_responsibilities:
     ta_responsibilities_info=ta_responsibilities_line.split(",")
     #course name
     temp_list = []
     for i in range(0,len(ta_responsibilities_info)-1):
        if(i==0):
            ta_name = ta_responsibilities_info[i]
            ta_names.append(ta_name)
        else:
            #0,1,2,3,4,5,6,7
            if((i+1)%2==0):
                if(i==1):
                    #day_name and day_time
                    temp_data = (ta_responsibilities_info[i].strip(),ta_responsibilities_info[i+1].strip())
                    temp_list.append(temp_data)

     if(item_count == 0):
         ta_responsibilities_dict = dict({ta_name: tuple(temp_list)})
     else:
         ta_responsibilities_dict.update({ta_name: tuple(temp_list)})

     item_count = item_count + 1
     #print course_name + "::" + temp_data

#print "TA Responsibilites"
#print "-------------------------"
#print ta_responsibilities_dict

#print ta_names


#6
#TA skills: skills possessed by each TA: name followed by list of skills.
#Example:
#TA1, C, C++, Java, JavaScript
item_count = 0

#List which stores all the names of TA's

for ta_skills_line in ta_skills:
     temp_list = []

     ta_skills_info=ta_skills_line.split(",")
     #course name
     for i in range(0,len(ta_skills_info)-1):
        if(i==0):
            ta_name = ta_skills_info[i]
        else:
            temp_data = temp_list.append(ta_skills_info[i].strip())

     if(item_count == 0):
         ta_skills_dict = dict({ta_name: tuple(temp_list)})
     else:
         ta_skills_dict.update({ta_name: tuple(temp_list)})

     item_count = item_count + 1
     #print course_name + "::" + temp_data

#print "TA Skills"
#print "-------------------------"
#print ta_skills_dict

#Forming Domain Values of each course

item_count = 0
for course_requirements_line in course_requirements:
    course_requirements_info=course_requirements_line.split(",")

    for i in range(0,len(course_requirements_info)):
        if(i==0):
            course_name = course_requirements_info[i].strip()
    if(item_count == 0):
        course_dom_dict = dict({course_name: tuple(ta_names)})
    else:
        course_dom_dict.update({course_name: tuple(ta_names)})
    item_count = item_count + 1


#print course_dom_dict

#Code to form Course X TA Matrix
#This matrix shows best TA matching to a course

total_values=0
total_courses=0
total_ta=0

for course_req in course_requirements_dict:
    #print course_req,"::",course_requirements_dict[course_req]
    total_courses = total_courses + 1

    for ta_skills_req in ta_skills_dict:
        #print ta_skills_req,"::",ta_skills_dict[ta_skills_req]
        total_values=total_values + 1

total_ta=(total_values/total_courses)

#print suit_matrix

#Find Number of TA Required For A Course
course_stud_counter = 0
for c_name in course_details_dict:
    course_stud_counter = course_stud_counter + 1

course_stud_arr = []
#Extract Total Student Enrollment for the course
#Find number of TA's required for a course
course_counter=0
for c_name in course_details_dict:
    tot_temp_arr = course_details_dict[c_name]

    tot_stud = int(tot_temp_arr[0])
    #print tot_stud
    if(tot_stud < 25):
        ta_req = 0

    if(tot_stud >= 25 and tot_stud < 40):
        ta_req = 0.5

    if(tot_stud >= 40 and tot_stud < 60):
        ta_req = 1.5

    if(tot_stud >= 60):
        ta_req = 2

    course_stud_temp = str(c_name),ta_req
    course_stud_arr.append(course_stud_temp)

    if(course_counter == 0):
        course_ta_dict = dict({c_name: ta_req})
    else:
        course_ta_dict.update({c_name: ta_req})

    course_counter = course_counter + 1

#print course_ta_dict

#TA Quota Code Starts
ta_quota_val = 1
ta_val_counter = 0

for ta_name in ta_skills_dict:
    if(ta_val_counter == 0):
         ta_quota_dict = dict({ta_name: ta_quota_val})
    else:
         ta_quota_dict.update({ta_name: ta_quota_val})

    ta_val_counter = ta_val_counter + 1
#TA Quota Code Ends
#print ta_quota_dict

def get_day(day):
    if day == 'mon': return 1
    elif day == 'tue': return 2
    elif day == 'wed': return 3
    elif day == 'thu' or day =='th': return 4
    elif day == 'fri': return 5
    elif day == 'sat': return 6
    elif day == 'sun': return 7
    else:
        print day
        return -1

def format_time(dic,t_dur):
    for key in dic:
        time_list = []
        for val in dic[key]:
            day = get_day(val[0])

            time = re.split('\s|:',val[1])
            hour = int(time[0])
            if time[2] == 'pm' and hour is not 12: hour = hour + 12
            if time[2] == 'am' and hour is 12: hour = hour - 12
            minute = int(time[1])

            t_start = dt(2015, 1, day, hour, minute)
            t_end = t_start + t_dur
            time_list.append((t_start,t_end))

        dic[key] = tuple(time_list)

    return dic

course_timing_dict = format_time(course_timing_dict, c_dur)
course_recitations_dict = format_time(course_recitations_dict, r_dur)
ta_responsibilities_dict = format_time(ta_responsibilities_dict, c_dur)

def prune_domain(course_dom, ta_time, course_time, check=False):
    for course in course_dom.keys():
        if course not in course_time:
            continue

        if check == True:
            if course_details_dict[course][1] == 'no':
                continue

        for c_val in course_time[course]:
            remaining_ta=course_dom[course]

            for ta in remaining_ta:
                for t_val in ta_time[ta]:
                    if (t_val[0]>=c_val[0] and t_val[0]<c_val[1]) or (t_val[1]>c_val[0] and t_val[1]<=c_val[1]):
                        #clash happeneing
                        temp = list(course_dom[course])
                        temp.remove(ta)
                        course_dom[course] = tuple(temp)
                        break
    return course_dom

#print course_dom_dict


course_dom_dict = prune_domain(course_dom_dict, ta_responsibilities_dict, course_timing_dict, True)

course_dom_dict = prune_domain(course_dom_dict, ta_responsibilities_dict, course_recitations_dict)

#print course_dom_dict

for course in course_dom_dict:
    count = []
    for ta in course_dom_dict[course]:
        count.append(len(set(ta_skills_dict[ta]).intersection(course_requirements_dict[course])))
    course_dom_dict[course] = [p for (q,p) in sorted(zip(count,course_dom_dict[course]),reverse=True)]

#print course_dom_dict
assigned_values = []
ta_assign = {}
courses =  course_dom_dict.keys()

def adjacancy(graph, course_time_1, course_time_2, check1=False, check2=False):
    for c1 in course_time_1:
        if check1 == True:
            if course_details_dict[c1][1] == 'no':
                continue

        for c1_val in course_time_1[c1]:
            for c2 in course_time_2:
                if check2 == True:
                    if course_details_dict[c2][1] == 'no':
                        continue

                for c2_val in course_time_2[c2]:
                    if c1 == c2: continue

                    if (c2_val[0]>=c1_val[0] and c2_val[0]<c1_val[1]) or (c2_val[1]>c1_val[0] and c2_val[1]<=c1_val[1]):
                        #Courses are clashing
                        if c1 not in graph:
                            graph[c1] = set([c2])
                        else:
                            graph[c1].update([c2])
                        break

    return graph

graph = {}
graph = adjacancy(graph, course_timing_dict, course_timing_dict, True, True)
graph = adjacancy(graph, course_timing_dict, course_recitations_dict, True)
graph = adjacancy(graph, course_recitations_dict, course_timing_dict, False, True)
graph = adjacancy(graph, course_recitations_dict, course_recitations_dict)

print "Course Domains:", course_dom_dict
print "Graph:",graph

#LOL = False
Best_Score = -1
Best_Assignment = ()
rec_count = 0
max_ta_quota_count = 0
for ta in ta_quota_dict:
    max_ta_quota_count += ta_quota_dict[ta]

def dfs(algo, course_domain, ta_time, course_index,update=False):
    global Best_Score, Best_Assignment, rec_count
    rec_count += 1

    #Exiting Condition
    if course_index >= len(course_dom_dict):
        assigned_values.append(ta_assign)

        #Calculate Score
        cnt1=0
        cnt2=0
        cnt3=0
        for course in ta_assign:
            if ta_assign[course]: cnt1 += 1                 #Number of courses ta assigned
            if course_ta_dict[course] == 0: cnt2 += 1       #Number of completely satisfied courses

        for ta in ta_quota_dict:
            cnt3 += ta_quota_dict[ta]                       #Number of TA's assigned


        score = cnt1+cnt2+(max_ta_quota_count-cnt3)

        #Print every possible value
        #print ta_assign
        if score > Best_Score:
            #print "score::", score
            #print "best score::", Best_Score
            Best_Score = score
            Best_Assignment = (ta_assign.copy(),)
            print "New Best:", Best_Assignment
        return

    #Update domain for every new course after assigning TA's
    if update:
        course_domain = prune_domain(course_domain,ta_time, course_timing_dict, True)
        course_domain = prune_domain(course_domain,ta_time, course_recitations_dict)

    course = courses[course_index]
    #print course

    for ta in course_domain[course]:
        #check if assignment possible
        if ta_quota_dict[ta] == 0: continue

        #Assign values
        if course not in ta_assign:
            ta_assign[course] = [ta]
        else:
            ta_assign[course].append(ta)

        #Update data after assigning
        ta_time_new = ta_time.copy()
        ta_time_new[ta] = tuple(set(list(ta_time[ta])+list(course_timing_dict[course])))
        ta_quota_dict[ta] -= 0.5
        course_ta_dict[course] -= 0.5


        course_domain_new = course_domain.copy()

        if algo == 2:   #1->BT #2->BT+FC #3->BT+FC+CP
            if course in graph:
                #print "course:",course
                for adj_node in graph[course]:
                    #print "domain before pruning:", course_domain_new
                    if ta in course_domain_new[adj_node]:
                        temp = list(course_domain_new[adj_node])
                        temp.remove(ta)
                        course_domain_new[adj_node] = tuple(temp)
                        #print "domain after pruning:", course_domain_new

        #print course, course_ta_dict[course]
        if course_ta_dict[course] == 0:
            dfs(algo, course_domain_new, ta_time_new, course_index+1,True)
        else:
            dfs(algo, course_domain_new, ta_time_new, course_index)

        #Undo assigned values
        ta_quota_dict[ta] += 0.5
        course_ta_dict[course] += 0.5

        ta_assign[course].remove(ta)


    dfs(algo, course_domain,ta_time, course_index+1,True)

def traverse(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        #print "going from:", start, "to:",next
        for ta in course_dom_dict[start]:
            if (len(set(course_dom_dict[next]) - set([ta])) == 0) and course_dom_dict[next]:
                course_dom_dict[start].remove(ta)
                visited = visited - graph[start] - set([start])
                #print "removing:", ta, "from:",start

        traverse(graph, next, visited)
    return visited


#print "New Domain:", course_dom_dict

if __name__ == "__main__":

    global Best_Score, rec_count

    print
    print "------------------------Plain Backtracking search (BS) Starts--------------------------------"
    algo = 1
    #assigned_values[:] = []
    #ta_assign.clear()
    Best_Score = -1
    Best_Assignment = ()
    rec_count = 0

    #print "before dfs"
    start = time.time()
    dfs(algo, course_dom_dict, ta_responsibilities_dict, 0)
    end = time.time()
    elapsed = end - start
    print "Plain Backtracking search (BS) Execution Time::",elapsed, "seconds"
    print "Number of Recursion Calls::", rec_count
    #print "after dfs"
    #print "Assigned Value:", Best_Assignment
    print "------------------------Plain Backtracking search (BS) Output Ends--------------------------------"

    print
    print "------------------------BS + Forward Checking (FC) Output Starts--------------------------------"
    algo = 2
    #assigned_values[:] = []
    #ta_assign.clear()
    Best_Score = -1
    Best_Assignment = ()
    rec_count = 0

    #print "before dfs"
    start = time.time()
    dfs(algo, course_dom_dict, ta_responsibilities_dict, 0)
    end = time.time()
    elapsed = end - start
    print "BS + Forward Checking (FC) Execution Time::",elapsed, "seconds"
    print "Number of Recursion Calls:", rec_count
    #print "after dfs"
    #print "Assigned Value:", Best_Assignment
    print "------------------------BS + Forward Checking (FC) Output Ends--------------------------------"

    print
    print "------------------------BS+FC + Constraint propagation Starts--------------------------------"
    #course_dom_dict['cse307'].remove('ta2')
    #print "Graph:", graph
    #print "Old Domain:", course_dom_dict
    visited = None
    for course in course_dom_dict:
        if course not in graph:
            graph[course] = set([])
        if visited is None:
            visited = traverse(graph, course, visited)

        if course not in visited:
            visited = traverse(graph, course, visited)

    #print "New Domain:", course_dom_dict
    #print "graph::",graph

    "algorithm 3"
    algo = 2
    #assigned_values[:] = []
    #ta_assign.clear()
    Best_Score = -1
    Best_Assignment = ()
    rec_count = 0

    #print "before dfs"
    start = time.time()
    dfs(algo, course_dom_dict, ta_responsibilities_dict, 0)
    end = time.time()
    elapsed = end - start
    print "BS+FC + Constraint propagation Execution Time::",elapsed, "seconds"
    print "Number of Recursion Calls:", rec_count
    #print "after dfs"
    #print "Assigned Value:", Best_Assignment

    print "------------------------BS+FC + Constraint propagation Output Ends--------------------------------"