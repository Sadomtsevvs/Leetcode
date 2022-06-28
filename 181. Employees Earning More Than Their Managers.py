# /* Write your T-SQL query statement below */
# SELECT
# employee.name as Employee
# FROM Employee AS employee
# LEFT JOIN Employee AS manager
# ON employee.managerId = manager.id
# WHERE employee.salary > manager.salary

# SELECT
# employee.name AS Employee
# FROM Employee AS employee
# INNER JOIN Employee AS manager
# ON employee.managerId = manager.id
# WHERE employee.salary > manager.salary