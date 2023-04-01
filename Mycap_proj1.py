# PROJECT - 1: School administration
import csv
def write(info_list):
    with open('student_file.csv','a',newline=" ") as csv_file:
        writer=csv.writer(csv_file)
        if csv_file.tell()==0:
            writer.writerow(["Name","Age","Phone number","Email ID"])
        writer.writerow(info_list)
if __name__=='__main__':
    con=True
    std_num=1
    while(con):
        std_info=input(f"Enter information (Name,Age,Phone number,Email ID) for student {std_num} : ")
        std_info_list=std_info.split(' ')
        print(f"\nThe entered information : \n Name :{std_info_list[0]}\n Age : {std_info_list[1]}\n Phone number :{std_info_list[2]}\n Email ID : {std_info_list[4]}")
        write_into_csv(std_info_list)
        conti=input("Is the entered information is correct (yes/no) : ").lower()
        if conti=="yes":
             write_into_csv(std_info_list)
             conti_2=input("Do you want to enter information of another student (yes/no) : ").lower()
             if conti_2=="yes":
                con=True
                std_num+=1
             elif conti=="no":
                con=False
        elif conti=="no":
            print("Re enter the information !")
