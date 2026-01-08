basic = float(input())
hra = 0.2 * basic
da = 0.1 * basic
total = basic + hra + da
tax = 0.05 * total
net_salary = total - tax
print("Net Salary:", net_salary)
