from itertools import *
def sol_mincover(n=5,m=5,pages=1,subjects=[{1, 3}, {1, 4}, {2},{2, 5}, {3, 5}]):
    subjects_needs = set(i for i in range(m))
    for i in range(1,n):
        for x in combinations(subjects, i):
            current_subjects = set(l for k in x for l in k)
            print(current_subjects)
            if current_subjects==subjects_needs:
                
            # if set(x) == subjects_needs:
            #     return x
    # print(*[i for i in combinations(subjects,2)])
sol_mincover()