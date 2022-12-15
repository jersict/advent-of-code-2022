import re
f = open('04\input.txt', 'r')
lines = f.readlines()
complete_overlap = 0
partial_overlap = 0
for line in lines:
    sections = [int(x) for x in re.split('-|,', line.strip())]
    if (sections[0]>=sections[2] and sections[1]<=sections[3]) or (sections[0]<=sections[2] and sections[1]>=sections[3]):
        complete_overlap += 1
        partial_overlap += 1
    elif not ((sections[0]<sections[3] and sections[1]<sections[2]) or (sections[0]>sections[3] and sections[1]>sections[2])):
        partial_overlap += 1
print('There are {0} complete overlaps and {1} partial overlaps.'.format(complete_overlap, partial_overlap))
