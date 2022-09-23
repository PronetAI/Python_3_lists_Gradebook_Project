last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

subjects=["physics","calculas","poetry","history"]
grades=[98,97,85,88]
gradebook=[]
for i in range(0,len(subjects),1):
  gradebook.append([subjects[i],grades[i]])
gradebook.append(["computer science",100])
gradebook.append(["visual arts",93])
gradebook[5][1]="98"
gradebook[2].remove('poetry')
gradebook[2].append('Pass')
full_gradebook=last_semester_gradebook+gradebook
print(full_gradebook)
