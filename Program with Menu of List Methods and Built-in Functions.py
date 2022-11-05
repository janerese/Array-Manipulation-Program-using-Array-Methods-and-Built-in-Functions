# Programmed by Erika Jane T. Reyes

# Write a python program that do the following:
# Display the initial content of the array
# Display a menu of options
# Allows user to select item in the menu (check if valid)
# Perform the selected option (you may prompt additional info to user when need)
# Display the resulting values of the array

array1 = [4, 21, 13, 1, 7, 75, 36, 17, 9, 17]

print("*" * 70)
print("             Welcome to this Special Array Program!")
print("    Here you can customize the array given in many different ways.")
print("          This is the array we are working with today: ")
print(f"              {array1}")

def print_menu():
    print("\n" + "*"* 31 + "  MENU  " + "*" * 31)
    print("\t\t\t1 -> Add an element")
    print("\t\t\t2 -> Insert an element")
    print("\t\t\t3 -> Modify an element")
    print("\t\t\t4 -> Delete an element")
    print("\t\t\t5 -> Arrange in ascending order")
    print("\t\t\t6 -> Arrange in descending order")
    print("\t\t\t7 -> Reverse the order")
    print("\t\t\t8 -> Find the smallest element")
    print("\t\t\t9 -> Find the largest element")
    print("\t\t\t10 -> Find an element")
    print("\t\t\t11 -> Sum of all the elements")
    print("\t\t\t12 -> End the program")
    print("*" * 70)

loop = True

def main():
    try:
        print_menu()
        print("\t\t\t\tThe array:")
        print(f"\t           {array1}")
        print("*" * 70)
        choice = int(input("\t\t     Enter your choice [1-12]: "))
        print("*" * 70)

    except ValueError:
        print("Invalid choice.")

    else:
        if choice == 1:
            try:
                print("Enter the element you want to add: ")
                add_element = int(input())
            except ValueError:
                print("\nInvalid. Integer only.")
            else:
                array1.append(add_element)
                print("\nSuccessfully added the element.\n\nThis is the new array.")
                print(array1)

        elif choice == 2:
            try:
                print("Enter the element you want to insert: ")
                insert_element = int(input())
                print("Enter the particular index you want it to be inserted at: ")
                insert_index = int(input())
            except ValueError:
                print("\nInvalid. Integer only.")
            else:
                array1.insert(insert_index,insert_element)
                print(f"\nSuccessfully inserted the element {insert_element} at index {insert_index}.\n\nThis is the new array.\n")
                print(array1)

        elif choice == 3:
            try:
                print("Enter the index of the element you want to modify: ")
                modify_index = int(input())
                print("Enter the new element: ")
                modify_element = int(input())
            except ValueError:
                print("\nInvalid. Integer only.")
            else:
                array1[modify_index] = modify_element
                print(f"\nSuccessfully modified element at index {modify_index}.\n\nThis is the new array.")
                print(array1)

        elif choice == 4:
            print("Mode of Deletion: "
                "\n1 -> By Index"
                "\n2 -> By Element")
            choice4 = int(input("\nEnter choice: "))
            if choice4 == 1:
                try:
                    print("Enter the index of the element you want to delete: ")
                    delete_index = int(input())
                except ValueError:
                    print("\nInvalid. Integer only.")
                else:
                    array1.pop(delete_index)
                    print(f"\nSuccessfully deleted element at index {delete_index}.\n\nThis is the new array.")
                    print(array1)
            elif choice4 == 2:
                try:
                    print("Enter the element you want to delete: ")
                    delete_element = int(input())
                except ValueError:
                    print("\nInvalid. Integer only.")
                else:
                    array1.remove(delete_element)
                    print(f"\nSuccessfully deleted the element {delete_element}.\n\nThis is the new array.")
                    print(array1)
            else:
                print("Invalid choice.")


        elif choice == 5:
            array1.sort()
            print(f"\nSuccessfully arranged the array in ascending order.\n\nThis is the new array.")
            print(array1)

        elif choice == 6:
            array1.sort(reverse=True)
            print(f"\nSuccessfully arranged the array in descending order.\n\nThis is the new array.")
            print(array1)

        elif choice == 7:
            array1.reverse()
            print(f"\nSuccessfully reversed the order of the array.\n\nThis is the new array.")
            print(array1)

        elif choice == 8:
            smallest = min(array1)
            print("\nSuccessfully found the smallest element in the array.")
            print(f"\nThe smallest element is {smallest}.")

        elif choice == 9:
            largest = max(array1)
            print("\nSuccessfully found the largest element in the array.")
            print(f"\nThe smallest element is {largest}.")

        elif choice == 10:
            try:
                print("Enter the element you want to find: ")
                find_element = int(input())
            except ValueError:
                    print("\nInvalid. Integer only.")
            else:
                find_index = array1.index(find_element)
                print(f"\nSuccessfully found the index of the first occurrence of the element {find_element}.")
                print(f"\nIt is found at the index {find_index}.")

        elif choice == 11:
            sum_elements = sum(array1)
            print(f"\nSuccessfully added all of the elements in the array.")
            print(f"\nThe sum of all the elements is {sum_elements}")

        elif choice == 12:
            print("\t\tThank you for using this program!!!")
            print("*" * 70)

        else:
            print("Invalid choice.")

main()
