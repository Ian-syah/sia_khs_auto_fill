import datetime

x = datetime.datetime.now()

curr_month = x.month
curr_year  = x.year

sem_ganjil = [7, 8, 9, 10, 11, 12]
sem_genap  = [1, 2, 3,  4,  5,  6]

for i in sem_ganjil:
    if i == curr_month:
        isGanjil = True
        break
    else:
        isGanjil = False

for i in sem_genap:
    if i == curr_month:
        isGenap = True
        break
    else:
        isGenap = False

if isGanjil == True:
    print("Tahun Ajaran %i/%i Semester 1" %(curr_year, curr_year+1))
elif isGenap == True:
    print("Tahun Ajaran %i/%i Semester 2" %(curr_year-1, curr_year))

