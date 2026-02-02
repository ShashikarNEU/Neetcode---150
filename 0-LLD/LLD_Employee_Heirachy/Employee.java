package LLD_Employee_Heirachy;

import java.util.ArrayList;
import java.util.List;

public class Employee {
  private String name;
  private int age;
  private Department department;
  private String designation;
  private String salary;
  private Level level;
  private String experience;
  private Employee manager;
  private List<Employee> childEmployees;

  private List<Report> reports;

  public Employee(String name, int age, Department department, String designation, String salary, Level level, String experience) {
    this.name = name;
    this.age = age;
    this.department = department;
    this.designation = designation;
    this.salary = salary;
    this.level = level;
    this.experience = experience;
  }

  public List<Report> getDirectReports() {
    List<Report> directReports = new ArrayList<>();
    for (Employee employee: this.childEmployees)
    {
      for (Report report : employee.reports)
      {
        directReports.add(report);
      }
    }
    return directReports;
  }

    public List<Report> getInDirectReports() {
      List<Report> IndirectReports = new ArrayList<>();
      // Perform dfs on employee (Studied python for dsa)
      // def dfs(node):
      //   if not node:
      //   return
      //   for i in childEmployees:
      //     for report in i.reports:
      //       IndirectReports.add(report)
      //     dfs(i)
      return getInDirectReports();
      // Add department or experience in dfs fn as a argument and get only those reports also
    }





  
}
