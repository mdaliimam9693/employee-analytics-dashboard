import pandas as pd

# create file .txt
with open("report.txt","w") as file :
    file.write("Report of Employees Dashboard\n")
    file.write("-"*40)

dt=pd.read_csv("employees_1000.csv")
print("Employees Dashboard")
print("-"*40)

# --------------------------------------->

# total number of employees
def total_emp(dt):
    total_emp=len(dt['Emp_ID'])
    print("Total Employees :",total_emp)
    with open("report.txt","a") as file:
        file.write('\n'+"Total Employees :"+str(total_emp))


# total average salary
def avg_salary(dt):
    avg_sala=round(dt['Salary'].mean(),2)
    print("Average Salary :",avg_sala)
    with open("report.txt","a") as file:
        file.write('\n'+"Average Salary :"+str(avg_sala))


# highest salary
def highest_salary(dt):
    high_sala=dt['Salary'].max()
    print("Highest Salary :",high_sala)
    with open("report.txt","a") as file:
        file.write('\n'+"Highest Salary :"+str(high_sala)+'\n'+'-'*40)

# department wise emloyees count
def depart_emp_count(dt):
    depart_emp=dt.groupby("Department")['Name'].count()
    print("Department Wise Employees Count :\n",depart_emp)
    with open("report.txt","a") as file:
        file.write('\n'+"Department Wise Employees Count :\n"+str(depart_emp)+'\n'+'-'*40)

# city wise employees count
def city_emp_count(dt):
    city_emp=dt.groupby("City")['Name'].count()
    print("City Wise Employees Count :\n",city_emp)
    with open("report.txt","a") as file:
        file.write('\n'+"City Wise Employees Count :\n"+str(city_emp)+'\n'+'-'*40)


# top 5 salary - employees
def top_salary_emp(dt):
    top_salary=dt.sort_values('Salary',ascending=False).head(5)
    print("Top 5 salary Employees :\n",top_salary)
    with open("report.txt","a") as file:
        file.write('\n'+"Top 5 salary Employees :\n"+str(top_salary)+'\n'+'-'*40)


# latest join employees 
def latest_join_emp(dt):
    latest_join=dt.loc[dt['Joining_Date'].idxmax()]
    print("Latest Join Employees :\n",latest_join)
    with open("report.txt","a") as file:
        file.write('\n'+"Latest Join Employees :\n"+str(latest_join)+'\n'+'-'*40)

# Lowest Salary
def lowest_salary(dt):
    lowest=dt['Salary'].min()
    print("Lowest Salary :",lowest)
    with open("report.txt","a") as file:
        file.write('\n'+"Lowest Salary :"+str(lowest)+'\n'+'-'*40)

# department wise average salary
def depart_avg_salary(dt):
    deaprt=dt.groupby("Department")['Salary'].mean()
    print("Department Wise Average Salary :\n",deaprt)
    with open("report.txt","a") as file:
        file.write('\n'+"Department Wise Average Salary :\n"+str(deaprt)+'\n'+'-'*40)    

total_emp(dt)
avg_salary(dt)
highest_salary(dt) 
depart_emp_count(dt)  
city_emp_count(dt) 
top_salary_emp(dt)
latest_join_emp(dt)
lowest_salary(dt)
depart_avg_salary(dt)



