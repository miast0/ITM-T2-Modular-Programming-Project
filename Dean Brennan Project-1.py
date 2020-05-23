# Dean Brennan R00179510
# Semester 2 project

# import used to later delay printing outputs
from random import randint
import time
import tkinter as tk








# This function reads in data and orders it into 5 lists
def load_data(FILE):
    employee_id = []
    f_name = []
    l_name = []
    email = []
    salary = []
    load_loop = True
    data_file = open(FILE + ".txt")
    # This loop will continuously add data into the correct columns until the file is empty
    while load_loop == True:
        temp = data_file.readline().rsplit()
        if temp == []:
            load_loop = False
            break
        else:
            employee_id += temp
            f_name += data_file.readline().rsplit()
            l_name += data_file.readline().rsplit()
            email += data_file.readline().rsplit()
            salary += data_file.readline().rsplit()
            salary = [float(i) for i in salary]
    return employee_id, f_name, l_name, email, salary

def main_menu(FILE, employee_id_list, f_name_list, l_name_list, email_list, salary_list):
    banner = "=" * 5
    print(banner + "Welcome" + banner)
    # This causes a delay for half a seccond between the welcome statement and the user inputs
    time.sleep(.5)
    print("\n\nPlease select an option\n\n")
    time.sleep(1)
    quit = False
    #The loop will continue to ask the question untill the user quits the function
    while quit == False:
        #user selection, which lines up to the specific functions
        user_selection = input("\n1. View all employees\n"
                                   "2. View a particular employee\n"
                                   "3. Edit the salary of an employee\n"
                                   "4. Add a new employee\n"
                                   "5. Delete an employee\n"
                                   "6. Give an end of year bonus to each employee\n"
                                   "7. Generate a report for management\n"
                                   "8. Quit\n"
                                   ">>>> ")
        # This statment converts and alphabetic/symbolic input to an invalid user input, to force a loop
        if not user_selection.isnumeric():
            user_selection = 0
        if int(user_selection) < 9 and int(user_selection) > 0:
            user_selection = int(user_selection)
            if user_selection == 1:
                view_all_employee(employee_id_list, f_name_list, l_name_list, email_list, salary_list)
            elif user_selection == 2:
                view_one_employee(employee_id_list, f_name_list, l_name_list, email_list, salary_list)
            elif user_selection == 3:
                edit_salary(employee_id_list, f_name_list, l_name_list, salary_list)
            elif user_selection == 4:
                add_employee(employee_id_list, f_name_list, l_name_list, email_list, salary_list)
            elif user_selection == 5:
                delete_employee(employee_id_list, f_name_list, l_name_list, email_list, salary_list)
            elif user_selection == 6:
                give_bonus(employee_id_list, f_name_list, l_name_list, salary_list)
            elif user_selection == 7:
                gen_report(employee_id_list, f_name_list, l_name_list, salary_list)
            elif user_selection == 8:
                save_data(FILE, employee_id_list, f_name_list, l_name_list, email_list, salary_list)
                print("Good bye!")
                quit = True
        else:
            #If the input is not between the given options the loop will restart
            print("Invalid input, please select a valid option\n")
            time.sleep(.5)
    return employee_id_list, f_name_list, l_name_list, email_list, salary_list

def view_all_employee(employee_id_list, f_name_list, l_name_list, email_list, salary_list):
    print("ID\t\tF_name\tL_name\t\tEmail\t\tSalary\n")
    #This will loop through all every item in the list and print them out individually
    for i in range(0, len(employee_id_list)):
        print(employee_id_list[i], " ", f_name_list[i], " ", l_name_list[i], " ", email_list[i], " ", salary_list[i])
    #Will not return to menu until the users gives an input
    user_selection = int(input("\nSelect an input\n"
                               "1. Return to menu\n>>> "))

def view_one_employee(employee_id_list, f_name_list, l_name_list, email_list, salary_list):
    view_one_employee_loop = True
    while view_one_employee_loop == True:
        view_one_employee_loop = False
        id_selection = input("What is the employee's ID?\n>>> ")
        if id_selection in employee_id_list:
            #The index for the chosen employee is given by the index of the input ID
            employee_index = employee_id_list.index(id_selection)
            print("\nID\t\tF_name\tL_name\t\tEmail\t\tSalary\n")
            print(employee_id_list[employee_index], " ", f_name_list[employee_index], " ", l_name_list[employee_index], " ",
                  email_list[employee_index], " ", salary_list[employee_index] , "\n")
            #This loop allows the user to check for further employees before returning to the menu
            user_selection = int(input("\nSelect an input\n"
                                       "1. Run again\n"
                                       "2. Return to menu\n>>> "))
            if user_selection == 1:
                view_one_employee_loop = True
            else:
                view_one_employee_loop = False
        else:
            print("Invalid input, Employee ID not found, please try again\n")
            view_one_employee_loop = True

def edit_salary(employee_id_list, f_name_list, l_name_list, salary_list):
    print("Edit Salary\n")
    edit_salary_loop = True
    while edit_salary_loop == True:
        edit_salary_loop = False
        user_selection = input("What is the employee's ID?\n>>> ")
        # this checks if the given ID is a valid ID in the employee list, if not it restarts the loop
        if user_selection in employee_id_list:
            employee_index = employee_id_list.index(user_selection)
            print("\nID\t\tF_name\tL_name\t\tSalary\n")

            print(employee_id_list[employee_index], " ", f_name_list[employee_index], " ", l_name_list[employee_index], " ",
                  salary_list[employee_index] , "\n")
            new_salary = input("Change salary from " + str(salary_list[employee_index]) + " to: ")
            #this will set the employees salary to the new salary value
            salary_list[employee_index] = float(new_salary)
            user_selection = int(input("\nSelect an input\n"
                                       "1. Run again\n"
                                       "2. Return to menu\n>>> "))
            if user_selection == 1:
                edit_salary_loop = True
            else:
                edit_salary_loop = False
            return salary_list
        else:
            print("ID not found, please try agan\n")
            time.sleep(.5)
            edit_salary_loop = True

def add_employee(employee_id_list, f_name_list, l_name_list, email_list, salary_list):
    print("Add Employee\n")
    f_name_list.append(input("What is the new employees first name?: "))
    l_name_list.append(input("What is the new employees last name?: "))
    id_generator(employee_id_list)
    email_generator(f_name_list,l_name_list,email_list)
    salary_loop = True
    while salary_loop == True:
        salary_loop = False
        try:
            salary_list.append(float(input("What is the employees salary?: ")))
        except:
            print("Invalid input, please enter the employees salary")
            salary_loop = True
    print("\nID\t\tF_name\tL_name\t\tEmail\t\tSalary\n")
    print(employee_id_list[len(employee_id_list)-1], " ", f_name_list[len(employee_id_list)-1], " ", l_name_list[len(employee_id_list)-1], " ",email_list[len(employee_id_list)-1], " ",salary_list[len(employee_id_list)-1] , "\n")
    return employee_id_list, f_name_list, l_name_list, email_list, salary_list

def id_generator(employee_id_list):
    id_gen_loop = True
    while id_gen_loop == True:
        id_gen_loop = False
        temp_id = str(randint(10000,99999))
        if temp_id in employee_id_list:
            id_gen_loop = True
        elif temp_id not in employee_id_list:
            employee_id_list.append(temp_id)
            return employee_id_list

def email_generator(f_name_list, l_name_list, email_list):
    email = f_name_list[len(f_name_list) - 1] + "." + l_name_list[len(l_name_list) - 1]
    email_check_loop = True
    i = 0
    while email_check_loop == True:
        temp_email = email + "@cit.ie"
        email_check_loop = False
        i += 1
        if temp_email in email_list:
            email += str(i)
            email_check_loop = True
        else:
            email = temp_email
            email_list.append(email)
            return f_name_list, l_name_list, email_list

def delete_employee(employee_id_list, f_name_list, l_name_list, email_list, salary_list):
    print("Delete Employee")
    delete_employee_loop = True
    while delete_employee_loop == True:
        delete_employee_loop = False
        user_selection = input("What is the employee's ID?\n>>> ")
        if user_selection in employee_id_list:
            employee_index = employee_id_list.index(user_selection)
            #This removes the item located at the set index for the ID of the string 
            employee_id_list.remove(employee_id_list[employee_index])
            f_name_list.remove(f_name_list[employee_index])
            l_name_list.remove(l_name_list[employee_index])
            email_list.remove(email_list[employee_index])
            salary_list.remove(salary_list[employee_index])
        else:
            print("ID not found, please try agan\n")
            time.sleep(1)
            delete_employee_loop = True
        user_selection = int(input("\nSelect an input\n1. Run again\n2. Return to menu\n>>> "))
        if user_selection == 1:
            delete_employee_loop = True
        else:
            delete_employee_loop = False

def give_bonus(employee_id_list, f_name_list, l_name_list, salary_list):
    FILE = "Bonus"
    print("End of year bonus\n")
    give_bonus_loop = True
    while give_bonus_loop == True:
        give_bonus_loop = False
        try:
            #inputs the bonus as a float value
            raw_bonus = float(input("What is the end of year bonus?: \n"))
            #if the bonus is less that 1 (100), adds one in order to add the bonus of that percent to the sum
            if raw_bonus < 1:
                bonus = 1+raw_bonus
            else:
                bonus = 1+(raw_bonus/100)
            data_file =open(FILE +".txt","w")
            #adds bonus to each employee
            for i in range(0,len(salary_list)):
                salary_list[i] = str(float(salary_list[i]) * bonus)
                data_file.write("ID: "+employee_id_list[i]+" Name: "+f_name_list[i]+" "+l_name_list[i]+" New salary: "+str(salary_list[i]))
            data_file.close()
        except:
            print("Invalid input, Please put in a decimal value for the bonus")
            give_bonus_loop = True
        user_selection = int(input("\nSelect an input\n1. Run again\n2. Return to menu\n>>> "))
        if user_selection == 1:
            give_bonus_loop = True
        else:
            give_bonus_loop = False



def gen_report(employee_id_list, f_name_list, l_name_list, salary_list):
    print("Generate report for management")
    time.sleep(.5)
    FILE = "Report"
    #gets average salary and formats it to 2 decimal places
    avg_salary = format(sum(salary_list) / float(len(salary_list)), ".2f")
    #Finds the highest salary in the list
    highest_salary = max(salary_list)
    highest_salary_index = salary_list.index(highest_salary)
    #Finds the ID of the highest salary of the list
    highest_salary_ID = employee_id_list.index(employee_id_list[highest_salary_index])
    #Gets the name of the ID with highest salary
    highest_salary_name = f_name_list[highest_salary_index]+" "+l_name_list[highest_salary_index]
    data_file = open(FILE +".txt","w")
    output = "The avgerage salary is"+str(avg_salary)+"€\nThe highest salary was "+str(highest_salary)+" by "+ str(highest_salary_ID)+ " "+highest_salary_name
    data_file.write(output)
    data_file.close()

def save_data(FILE, employee_id_list, f_name_list, l_name_list, email_list, salary_list):
    final = ""
    # this function prints each item one after another into the set file, replacing the old data
    for i in range(0, len(employee_id_list)):
        final += employee_id_list[i] + "\n" + f_name_list[i] + "\n" + l_name_list[i] + "\n" + email_list[
            i] + "\n" + str(salary_list[i]) + "\n"
    data_file = open(FILE + ".txt", "w")
    data_file.write(final)
    data_file.close()

def main():
    FILE_NAME = "Data"
    employee_id_list, f_name_list, l_name_list, email_list, salary_list = load_data(FILE_NAME)
    main_menu(FILE_NAME, employee_id_list, f_name_list, l_name_list, email_list, salary_list)
main()