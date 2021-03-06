'''
Simulation_Covid_School_Quarantine_Policy
by: https://github.com/Andy87877

🟩 = No Quarantine
🟨 = Quarantine
🟥 = Covid
🟦 = Is he/she Quarantine?
'''
import random

def judge():
    m = 10 # m > 3
    n = 10 # n > 3
    have_case = 10
    test = []
    is_case = []

    for i in range(m): # start
        test.append([])
        for j in range(n):
            test[i].append("🟩")

    while (have_case != len(is_case)): # case
        flag = True
        temp = random.randint(0,m*n-1)
        for i in is_case:
            if (i == temp):
                flag = False
        if (flag):
            is_case.append(temp)
            test[int(temp/n)][int(temp%n)] = "🟥"
    
    for i in range(m): # judge 
        for j in range(n):
            if (test[i][j] != "🟥"):
                if ((i == 0) and (j == 0)):
                    if ((test[i+1][j] == "🟥") or (test[i+1][j+1] == "🟥") or (test[i][j+1] == "🟥")):
                        test[i][j] = "🟨"
                elif ((i == 0) and (j == n-1)):
                    if ((test[i+1][j] == "🟥") or (test[i+1][j-1] == "🟥") or (test[i][j-1] == "🟥")):
                        test[i][j] = "🟨"
                elif ((i == m-1) and (j == 0)):
                    if ((test[i-1][j] == "🟥") or (test[i-1][j+1] == "🟥") or (test[i][j+1] == "🟥")):
                        test[i][j] = "🟨"
                elif ((i == m-1) and (j == n-1)):
                    if ((test[i-1][j] == "🟥") or (test[i-1][j-1] == "🟥") or (test[i][j-1] == "🟥")):
                        test[i][j] = "🟨"
                elif (i == 0):
                    if ((test[i+1][j] == "🟥") or (test[i+1][j+1] == "🟥") or (test[i+1][j-1] == "🟥") or (test[i][j+1] == "🟥") or (test[i][j-1] == "🟥")):
                        test[i][j] = "🟨"
                elif (j == 0):
                    if ((test[i][j+1] == "🟥") or (test[i+1][j+1] == "🟥") or (test[i-1][j+1] == "🟥") or (test[i+1][j] == "🟥") or (test[i-1][j] == "🟥")):
                        test[i][j] = "🟨"
                elif (i == m-1):
                    if ((test[i-1][j] == "🟥") or (test[i-1][j+1] == "🟥") or (test[i-1][j-1] == "🟥") or (test[i][j+1] == "🟥") or (test[i][j-1] == "🟥")):
                        test[i][j] = "🟨"
                elif (j == n-1):
                    if ((test[i][j-1] == "🟥") or (test[i+1][j-1] == "🟥") or (test[i-1][j-1] == "🟥") or (test[i+1][j] == "🟥") or (test[i-1][j] == "🟥")):
                        test[i][j] = "🟨"
                else:
                    if ((test[i+1][j] == "🟥") or (test[i+1][j+1] == "🟥") or (test[i+1][j-1] == "🟥") or (test[i][j+1] == "🟥") or (test[i][j-1] == "🟥") or (test[i-1][j+1] == "🟥") or (test[i-1][j] == "🟥") or (test[i-1][j-1] == "🟥")):
                        test[i][j] = "🟨"

    # Sus position
    while (is_case.count(temp) != 0):
        temp = random.randint(0,m*n-1)
    if (test[int(temp/n)][int(temp%n)] == "🟨"): flag = True
    else: flag = False
    test[int(temp/n)][int(temp%n)] = "🟦"

    for i in range(m): # show
        for j in range(n):
            print(test[i][j], end=" ")
        print()

    return flag

def percent(n,m):
    for i in range(2,n):
        while(n%i==0 and m%i==0):
            n=n//i
            m=m//i
    return(str(n)+"/"+str(m))

times = 100
quar = 0
for i in range(times):
    if (judge()):
        quar += 1
        #time.sleep(0.1)
    print(percent(quar,times))
