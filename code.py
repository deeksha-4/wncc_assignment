N = int(input())        # N denotes the number of participants

participants = {}       # dictionary to store participant roll numbers and skill levels

for i in range(N):
    inp = input()
    [roll_number, s1, s2, s3, s4, s5] = inp.split()        # making the first element a string to allow for alphanumeric roll numbers
    s1, s2, s3, s4, s5 = int(s1), int(s2), int(s3), int(s4), int(s5)
    participants[roll_number] = [s1, s2, s3, s4, s5]

M = int(input())        # M denotes the number of projects

projects = {}       # dictionary to store project names and roles

for j in range(M):
    inp = input()
    [project_name, r1, r2, r3, r4, r5] = inp.split()
    r1, r2, r3, r4, r5 = int(r1), int(r2), int(r3), int(r4), int(r5)
    projects[project_name] = [r1, r2, r3, r4, r5]

count = 0       # variable to hold the number of projects that can be completed

# Idea : Start with the simplest projects- those involving only one role, since they would compromise at max one other project, so the count balances.

for proj in projects:
    non_zero = 0        # variable to hold the number of non zero roles
    non_zero_index = []     # list to hold the index of those non zero roles
    for k in range(5):
        if projects[proj][k]!=0:
            non_zero+=1
            non_zero_index.append(k)
    if non_zero == 1:
        skill = 10000       # arbitrary large number, assuming the skills are of a lesser order
        role = ''       # variable to hold the roll number of the participant who can complete the project
        for x in participants:
            if participants[x][non_zero_index[0]] >= projects[proj][non_zero_index[0]]:
                if participants[x][non_zero_index[0]] < skill:      # finding the participant with the minimum skill who can complete the project
                    role = x
        if role in participants and role!='':        # checking if suitable participant exists
            count+=1
            del participants[role]      # participant has been assigned project, and project can be completed

# Now we consider the next case, where a project requires two or more roles. Now we will have to include the possibility of participants mentoring each other.

    else:
        roles = {}      # here we need to maintain a dictionary to remember which roles have been fulfilled, as we may need to check these while filling roles where participants are mentors
        for l in non_zero_index:
            skill = 10000
            for x in participants:
                if participants[x][l] >= projects[proj][l]:
                    if participants[x][non_zero_index[0]] < skill:      # finding the least skilled participant who can complete the project
                        roles[l] = x

        if len(roles) == non_zero:     # we were able to find enough skilled participants without co-mentoring
            count += 1
            for a in roles:
                if roles[a] in participants:
                     del participants[roles[a]]        # removing all participants allotted that project from further rounds of allocation

        else:       # we could not find enough skilled participants; now we turn to co-mentoring
            f=0
            f1=0
            while(len(roles)<non_zero):
                for l in non_zero_index:        # iterating through unfulfilled roles
                    if l not in roles:
                        for t in roles:        # iterating through particpants already in the project, in different roles
                            if participants[roles[t]][l]>projects[proj][l]:        # checking if any of the participants can mentor another
                                f1=1
                                for x in participants:
                                    if participants[x][l] == projects[proj][l] - 1:        # checking if any of the unallotted participants can be mentored
                                        roles[l]=x
                                        f=1
                                        break
                                    if f==0:
                                        break       # no participant was skilled enough to be mentored
                            if f1==0:
                                break        # no mentors were available

                        if (f==0 or f1==0):
                            break       # mentor-mentee pair unavailable. no point in checking for the other non zero elements

                if (f==0 or f1==0):
                    break       # condition will never be satisfied, because there are no new elements to be added. so we need a manual break statement to prevent infinite looping

                if (len(roles) == non_zero):        # if the while loop exited normally, i.e. project can be completed through mentorship
                    count += 1
                    for a in roles:
                        if roles[a] in participant:
                            del participants[roles[a]]

print(count)        # final answer