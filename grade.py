class student:

    def __init__(self,s):
        self.total=0
        self.per=0
        self.grade=0
        self.marks=list();
        for i in range(0,5):
            self.marks.append(s[i])

    def total_f(self):
        for i in range(0,5):
           self.total = self.total+self.marks[i]
        self.per=(self.total/500)*100;
    
    def grade_f(self):
        if self.per>=90 and self.per<=100:
            self.grade="merit"
        elif self.per>=60 and self.per<=89:
            self.grade="Ist"
        elif self.per>=50 and self.per<=59:
            self.grade="2nd"
        elif self.per>=33 and self.per<=49:
            self.grade="3rd"
        else:
            self.grade="Fail"

    def show(self):
        for i in range(0,5):
            print(self.marks[i])
        print("total : ",self.total)
        print("Grade : ",self.grade)
        print("Per : ",self.per)

def start():
    l=list();

    print("enter marks of five subj :")
    for i in range(0,5):
        m=float(input( "{} sub : ".format((i+1))))
        try:
            if m>100 or m<0:
                raise Exception("invalid marks")
            else:
                l.append(m)
        except Exception:
            print("Exception ",Exception)
            start();
    obj=student(l);
    obj.total_f();
    obj.grade_f();
    obj.show();

start()       



        