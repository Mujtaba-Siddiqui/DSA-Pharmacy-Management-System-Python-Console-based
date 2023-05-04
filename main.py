import datetime
import numpy as np
import os
import random

stack = []

# Double LinkedList
# Merge Sort
# Selection Sort
# Insertion Sort
# Bubble Sort
# Stack
# Queue
# LinearSearch
# Binary Search
# Array

def MergeSortAlgo(my_array):
    size = len(my_array)
    if size > 1:
        middle = int(size / 2)
        left_arr = my_array[:middle]
        right_arr = my_array[middle:]
        MergeSortAlgo(left_arr)
        MergeSortAlgo(right_arr)
        p = 0
        q = 0
        r = 0
        left_size = len(left_arr)
        right_size = len(right_arr)
        while p < left_size and q < right_size:
            if left_arr[p] < right_arr[q]:
                my_array[r] = left_arr[p]
                p += 1
            else:
                my_array[r] = right_arr[q]
                q += 1
            r += 1
        while p < left_size:
            my_array[r] = left_arr[p]
            p += 1
            r += 1
        while q < right_size:
            my_array[r] = right_arr[q]
            q += 1
            r += 1


def SelectionSortAlgo(my_array):
    for i in range(len(my_array) - 1):
        min_index = i
        for j in range(i + 1, len(my_array) - 1):
            if my_array[j] < my_array[min_index]:
                min_index = j
        swap = my_array[i]
        my_array[i] = my_array[min_index]
        my_array[min_index] = swap


def InsertionSortAlgo(my_array):
    for i in range(1, len(my_array)):
        key = my_array[i]
        j = i - 1
        while j >= 0 and key < my_array[j]:
            my_array[j + 1] = my_array[j]
            j -= 1
        my_array[j + 1] = key


def linearsearch(arr, x):
    for i in range(len(arr)):
        if str(arr[i]) == str(x):
            return i
        else:
            return -1


def binary_search(arr, low, high, x):
    if high >= low:
        mid = int((high + low) / 2)
        if int(arr[mid]) == int(x):
            return arr[mid]
        elif int(arr[mid]) > int(x):
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1


def BubbleSortAlgo(my_array):
    n = len(my_array)
    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            if my_array[j] < my_array[j + 1]:
                swap = my_array[j]
                my_array[j] = my_array[j + 1]
                my_array[j + 1] = swap
                already_sorted = False
        if (already_sorted):
            break
    return array


class Node:
    def __init__(self, particular, qty, unitprice):
        self.particular = particular
        self.qty = qty
        self.unitprice = unitprice
        self.amount = int(self.qty) * int(self.unitprice)
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.Name = None
        self.company = None
        self.date = None
        self.contact = None
        self.totalbill = 0
        self.start = None

    def insert(self, particular, qty, unitprice):
        if (self.start is None):
            self.start = Node(particular, qty, unitprice)
        else:
            ptr = self.start
            while (ptr.next != None):
                ptr = ptr.next
            ptr.next = Node(particular, qty, unitprice)

    def createinvoice(self):
        self.date = datetime.date.today()
        check = True
        while (check):
            x = str(input('Enter Medicine ID: '))
            qty = str(input('Enter Quantity: '))
            for line in open("medicines.txt", "r").readlines():
                data = line.split(',')
                if (data[0] == x):
                    particular = data[1]
                    unitprice = data[2]

            self.insert(particular, qty, unitprice)
            self.totalbill += int(qty) * int(unitprice)

            inpt = input("Press Enter to continue to add items or type NO to exit: ")
            if (inpt == "No" or inpt == "no" or inpt == "NO"):
                a = self.totalbill
                check = False

    def Print(self):
        self.billno = random.randint(0, 5)
        print("\n-------------------------------------------------------------")
        print("Bill:    " + str(self.billno) + "\t\t\t\t\t""Date:    " + str(self.date))
        print("-------------------------------------------------------------")
        print("S/no\tParticular \t\t Qty \t\t Rate  \t\t Amount\n")
        ptr = self.start
        i = 1
        while (ptr != None):
            print(str(i) + "\t\t " + ptr.particular + " \t\t\t " + ptr.qty + " \t\t " + ptr.unitprice + " \t\t " + str(
                ptr.amount))
            ptr = ptr.next
            i += 1
        print("-------------------------------------------------------------")
        print("\n\t\t\t\t\t\t\t\t\t\t" + "Total: " + str(self.totalbill))


class Medicines:
    medicines = np.array([])

    def __init__(self, medid, medicinename, price, quantity):
        self.medicineid = medid
        self.medicinename = medicinename
        self.price = price
        self.quantity = quantity

    def PurchaseMedicine(self):
        Bill = DoublyLinkedList()
        Bill.createinvoice()
        Bill.Print()

    def medicinedetails(self):
        file = "medicines.txt"
        if os.path.exists(file):
            for line in open(file, "r").readlines():
                data = line.split(',')
                self.medicines.append((data[0]))

    def FileDeletion(self, file, file2):
        with open(file, "r") as f:
            with open(file2, "w+") as f1:
                for line in f:
                    f1.write(line)
                f.close()
                f1.close()
        if os.path.exists(file):
            os.remove(file)
        else:
            print("The file does not exist")

    def DisplayAllMedicine(self):
        self.medicines = []
        self.medicinedetails()
        order = int(input("\t1.Ascending Order \n\t2.Descending Order"))
        if (order == 1):
            InsertionSortAlgo(self.medicines)
            if (os.path.exists("medicines.txt")):
                for i in range(len(self.medicines)):
                    for line in open("medicines.txt", "r").readlines():
                        data = line.split(',')
                        if (self.medicines[i] == data[0]):
                            print(str("\n\tMedicine #") + str(i + 1))
                            print("\tID: \t" + str(data[0]))
                            print("\tName: \t" + str(data[1]))
                            print("\tPrice: \t" + str(data[2]))
                            print("\tQuantity: \t" + str(data[3]))
            else:
                print("\tNo Medicines in Our Pharmacy")
        elif (order == 2):
            BubbleSortAlgo(self.medicines)
            if (os.path.exists("medicines.txt")):
                for i in range(len(self.medicines)):

                    for line in open("medicines.txt", "r").readlines():
                        data = line.split(',')
                        if (self.medicines[i] == data[0]):
                            print(str("\n\tMedicine #") + str(i + 1))
                            print("\tID: \t" + str(data[0]))
                            print("\tName: \t" + str(data[1]))
                            print("\tPrice: \t" + str(data[2]))
                            print("\tQuantity: \t" + str(data[3]))
            else:
                print("\tNo Medicines in Our Pharmacy")

    def DisplayAvailableMedicines(self):
        self.medicines = []
        self.medicinedetails()
        order = int(input("\t1. Descending Order\n\t2. Ascending Order"))

        if (order == 2):
            # Sort
            SelectionSortAlgo(self.medicines)
            if (os.path.exists("medicines.txt")):
                for i in range(len(self.medicines)):
                    # Queue
                    x = self.medicines.pop(0)
                    for line in open("medicines.txt", "r").readlines():
                        data = line.split(',')
                        if ((x == data[0]) and (int(data[3]) > 0)):
                            print()
                            print(str("\tMedicine #") + str(i + 1))
                            print("\tID: \t" + str(data[0]))
                            print("\tName: \t" + str(data[1]))
                            print("\tPrice: \t" + str(data[2]))
                            print("\tQuantity: \t" + str(data[3]))
            else:
                print("\tNo Medicines in Our Pharmacy")

        elif (order == 1):
            MergeSortAlgo(self.medicines)
            if (os.path.exists("medicines.txt")):
                for i in range(len(self.medicines)):
                    # Stack
                    x = self.medicines.pop()
                    for line in open("medicines.txt", "r").readlines():
                        data = line.split(',')
                        if ((x == data[0]) and (int(data[3]) > 0)):
                            print()
                            print(str("\tMedicine #") + str(i + 1))
                            print("\tID: \t" + str(data[0]))
                            print("\tName: \t" + str(data[1]))
                            print("\tPrice: \t" + str(data[2]))
                            print("\tQuantity: \t" + str(data[3]))
            else:
                print("\tNo Medicines in Our Pharmacy")

    def DisplayOutofStockMedicines(self):
        if (os.path.exists("medicines.txt")):
            medno = 0
            for line in open("medicines.txt", "r").readlines():
                data = line.split(',')
                if (int(data[3]) == 0):
                    medno += 1
                    print()
                    print(str("\tMedicine #") + str(medno + 1))
                    print("\tID: \t" + str(data[0]))
                    print("\tName: \t" + str(data[1]))
                    print("\tPrice: \t" + str(data[2]))
                    print("\tQuantity: \t" + str(data[3]))

        else:
            print("\tNo Medicines in Our Pharmacy")

    def SearchMedicine(self):
        var = True
        for line in open("medicines.txt", "r").readlines():
            data = line.split(',')

            # Linear Search
            if (self.medicineid == data[0]):

                print("\tID: " + str(data[0]))
                print("\tName: " + str(data[1]))
                print("\tPrice: " + str(data[2]))
                print("\tQuantity: " + str(data[3]))

                var = True
            else:
                var = False
        if (var == False):
            print("\tNo Medicine Found")

    def ismedalreadytaken(self):
        self.medicines = []
        self.medicinedetails()
        if (binary_search(self.medicines, 0, len(self.medicines) - 1, self.medicineid) == -1):
            return False
        else:
            return True

    def AddMedicine(self):
        if (self.ismedalreadytaken() == False):
            if (int(self.quantity) > 0):
                f = open("medicines.txt", "a+")
                f.write(str(self.medicineid) + ","
                        + str(self.medicinename) + ","
                        + str(self.price) + ","
                        + str(self.quantity) + ","
                        + "\n")
                print('\n\tMedicine Successfully Added')

            else:
                print("\tPlease enter Quantity greater thn zero")
        else:
            print("\tMedicine ID is Already Taken")

    def EditMedicine(self):
        file = "medicines.txt"
        file2 = "tempmedicines.txt"
        x = open(file2, "w")
        for line in open(file, "r").readlines():
            data = line.split(',')
            print()
            print()
            if (str(self.medicineid) == str(data[0])):
                x.write(str(input('\tEnter New ID: ')) + ","
                        + str(input('\tEnter New Name: ')) + ","
                        + str(input('\tEnter New Price: ')) + ","
                        + str(input('\tEnter Your New Quantity: '))
                        + ",\n")
            else:
                x.write(str(data[0]) + "," +
                        str(data[1]) + "," +
                        str(data[2]) + "," +
                        str(data[3]) + ",\n")

        x.close()
        print("Successfully Edited")
        self.FileDeletion(file2, file)

    def DeleteMedicine(self):
        file = "medicines.txt"
        file2 = "tempmedicines.txt"
        f = open(file, "r")
        f2 = open(file2, "w")
        for line in f.readlines():
            data = line.split(',')
            # Linear Search
            if (str(self.medicineid) == str(data[0])):
                continue
            else:
                f2.write(
                    str(data[0]) + "," +
                    str(data[1]) + "," +
                    str(data[2]) + "," +
                    str(data[3]) + ",\n")

        f.close()
        f2.close()
        print("Successfully Deleted")
        self.FileDeletion(file2, file)

    def DeleteAllMedicines(self):
        confirmation = str(input("Are You Sure You Want To Delete All Contacts Y/N"))
        if (os.path.exists("medicines.txt")) and (confirmation == 'Y'):
            os.remove("medicines.txt")


class Admin:
    users = []

    def __init__(self, name, email, password):

        self.name = name.lower()
        self.email = email
        self.password = password

    def getuserids(self):

        file = "Admins.txt"
        if os.path.exists(file):
            for line in open(file, "r").readlines():
                data = line.split(',')
                self.users.append(data[1])

    #def isUserAlreadyRegistered(self):
    #    self.users =[]
    #    self.getuserids()
    #    if(linearsearch(self.users,self.email)==-1):
    #        return False
    #    else:
    #        return True

    def Register(self):
        if (True):
            f = open("Admins.txt", "a+")
            f.write(str(self.name)
                    + "," + str(self.email) + ","
                    + str(self.password)
                    + ",\n")
            print("\tSuccessFully Registered")
        else:
            print("\tEmail already Taken")

    def Login(self):
        x = ''
        if (os.path.exists("Admins.txt")):
            for line in open("Admins.txt", "r").readlines():
                data = line.split(',')
                if (self.email == data[1] and self.password == data[2]):
                    self.name = data[0]
                    self.email = data[1]
                    self.password = data[2]
                    self.WelcomeAdmin()
                else:
                    x = 'notfound'

            if (x == 'notfound'):
                print("\tInvalid Email or Password")
        else:
            print("\n\tNo User Registered")

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    class LinkedList:
        def __init__(self):
            self.head = None

        def push(self, new_data):
            new_node = Node(new_data)
            new_node.next = self.head
            self.head = new_node

        def insertAfter(self, prev_node, new_data):
            if prev_node is None:
                print("The given previous node must inLinkedList.")
                return
            new_node = Node(new_data)
            new_node.next = prev_node.next
            prev_node.next = new_node

        def append(self, new_data):
            new_node = Node(new_data)
            if self.head is None:
                self.head = new_node
                return
            last = self.head
            while (last.next):
                last = last.next
            last.next = new_node

        def printList(self):
            temp = self.head
            while (temp):
                print(temp.data, end=" ")
                temp = temp.next

    def WelcomeAdmin(self):
        while (True):
            print(
                "\n\t1.Insert Medicine   \n\t2.Buy Medicine \n\t3.Update Medicine \n\t4.Search Medicine \n\t5.Delete Medicine \n\t6.Clear All Medicines\n\t7.Medicines Availability \n\t8.Medicines List \n\t9.Log Out")
            print()
            select = input("\tEnter Your Choice :: ")
            if select == '2':

                medicines = Medicines('none', 'none', 'none', 'none')
                medicines.PurchaseMedicine()
            elif select == '1':

                medicine = Medicines(input("\tEnter ID Number ::"),
                                     input("\tEnter Name:"),
                                     input("\tEnter Price:"),
                                     input("\tEnter Quantity:"),
                                     )
                medicine.AddMedicine()

            elif select == '3':
                medicines = Medicines(input("\tEnter ID ::"), 'none', 'none', 'none')
                medicines.EditMedicine()

            elif select == '4':
                medicines = Medicines(input("\tEnter ID:"), 'none', 'none', 'none')
                medicines.SearchMedicine()


            elif select == '5':
                medicines = Medicines(input("\tEnter Medicine ID:"), 'none', 'none', 'none')
                medicines.DeleteMedicine()

            elif select == '6':
                medicines = Medicines('none', 'none', 'none', 'none')
                medicines.DeleteAllMedicines()
            elif select == '8':
                medicines = Medicines('none', 'none', 'none', 'none')
                medicines.DisplayAllMedicine()

            elif select == '7':
                medicines = Medicines('none', 'none', 'none', 'none')
                medicines.DisplayAvailableMedicines()

            elif select == "9":
                break

            else:
                print("\tWrong Input")


print(" ---------------------------------------------------")
print(" |            Welcome To Medical Store             | ")
print(" ---------------------------------------------------")


def MainMenu() -> object:
    while (True):
        print("\t1. Sign Up  \n\t2. Login \n\t3. Shop Location\n\t4. About US\n\t5. Exit")
        print()
        select = input("Enter Your Choice ")
        if select == '2':
            admin = Admin('none', input("\tEnter Your Email:"), input("\tEnter Your Password:"), )
            admin.Login()
        elif select == '1':
            admin = Admin(
                input("\tEnter Your Name:"), input("\tEnter Your Email:"), input("\tEnter Your Password:"))
            admin.Register()
        elif select == '5':
            break
        elif select == "3":
            print("We have three shops")
            print("First Is Located In Block 19 , Al Noor Society , F.B Area, Karachi")
            print("Second is Located In Soldier Bazar near Gurumandir ")
            print("Third is located In Block D, North Nazimabad, Near Dolmen Mall")
        elif select == "4":
            print(
                "-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print(
                " HealthDirect’s pharmacy management solutions include the latest  prescription  technology \n services and friendly, expert pharmacy professionals to help you optimize your \n facility’s operations. Accuracy in our pharmacy process is designed with you in mind.\n It’s about making your job easier and community safer and more efficient. So, you can focus on \n providing better resident care and higher quality outcomes.")
            print(
                "-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        else:
            print('Invalid Input')
MainMenu()