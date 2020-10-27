class Salary:
    def __init__(self):
        self.basic = float(input("Enter basic pay of employee:"))
        self.leave = float(input("Enter Leave of employee "))
        self.total_days = float(input("Enter the Total days"))
        if self.leave == 1 :
            self.total_days = self.total_days
            self.per_day = self.basic/self.total_days

        elif self.leave >= 1 :
            self.total_days = self.total_days - (self.leave-1)
            self.per_day = self.basic/self.total_days
            


    def calculate_salary(self):
        return (self.total_days * self.per_day)

    

def main():
    salary = Salary();
    print("Gross salary of employee:",salary.calculate_salary())


if __name__ == '__main__':
    main()

