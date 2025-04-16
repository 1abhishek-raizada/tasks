
def q4():

    N=int(input("Enter the number "))
    countries=[]
    for x in range(N):
        y=input()
        countries.append(y)

    unique=len(set(countries))
    
    print(unique)
q4()
    