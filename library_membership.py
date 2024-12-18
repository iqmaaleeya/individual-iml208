class Member:
    """Class to represent a library member."""
    def __init__(self, member_id, name, email, age):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.age = age

class LibraryMembershipSystem:
    """Class to handle the library membership system."""
    def __init__(self):
        self.members = {}  # Dictionary to hold members indexed by member_id
        self.total_fee = 0  # To keep track of total membership fees
        self.total_members = 0  # Count of total members

    def create_member(self, member_id, name, email, age):
        """Create a new member and add to the system."""
        if member_id in self.members:
            print("Member ID already exists!")
            return False
        self.members[member_id] = Member(member_id, name, email, age)
        print("Member created successfully.")
        self.update_membership_fee(age)  # Update total fee after adding a member
        return True

    def update_membership_fee(self, age):
        """Update the total membership fee based on member's age."""
        if age < 18:
            self.total_fee += 10  # Student Membership
        elif 18 <= age <= 64:
            self.total_fee += 20  # Regular Membership
        else:
            self.total_fee += 15  # Senior Membership
        self.total_members += 1  # Increment member count

    def read_members(self):
        """Display all members."""
        if not self.members:
            print("No members found.")
            return
        for member in self.members.values():
            print(f"ID: {member.member_id}, Name: {member.name}, Email: {member.email}, Age: {member.age}")

    def update_member(self, member_id, name=None, email=None, age=None):
        """Update member information."""
        if member_id not in self.members:
            print("Member ID not found!")
            return False
        member = self.members[member_id]
        if name:
            member.name = name
        if email:
            member.email = email
        if age:
            # Adjust membership fee based on age change
            self.adjust_membership_fee(member.age, age)
            member.age = age
        print("Member updated successfully.")
        return True

    def adjust_membership_fee(self, old_age, new_age):
        """Adjust total membership fees based on age change."""
        self.total_fee -= self.calculate_fee(old_age)
        self.total_fee += self.calculate_fee(new_age)

    def calculate_fee(self, age):
        """Calculate membership fee."""
        if age < 18:
            return 10  # Student Membership
        elif 18 <= age <= 64:
            return 20  # Regular Membership
        else:
            return 15  # Senior Membership

    def delete_member(self, member_id):
        """Delete a member from the system."""
        if member_id not in self.members:
            print("Member ID not found!")
            return False
        # Adjust total fee before deletion
        member_age = self.members[member_id].age
        self.total_fee -= self.calculate_fee(member_age)
        del self.members[member_id]
        self.total_members -= 1  # Decrement member count
        print("Member deleted successfully.")
        return True

    def calculate_total_membership_fee(self):
        """Return the total membership fee."""
        return self.total_fee

    def calculate_average_membership_fee(self):
        """Calculate and return the average membership fee."""
        if self.total_members == 0:
            return 0  # Avoid division by zero
        return self.total_fee / self.total_members


def main():
    library_system = LibraryMembershipSystem()
    
    while True:
        print("\nLibrarian Interface for OPAC System")
        print("1. Create Member")
        print("2. Read Members")
        print("3. Update Member")
        print("4. Delete Member")
        print("5. Calculate Total Membership Fee")
        print("6. Calculate Average Membership Fee")
        print("7. Exit")
        
        choice = input("Choose an option (1-7): ")
        
        if choice == '1':
            member_id = input("Enter Member ID: ")
            name = input("Enter Member Name: ")
            email = input("Enter Member Email: ")
            age = int(input("Enter Member Age: "))
            library_system.create_member(member_id, name, email, age)
        
        elif choice == '2':
            library_system.read_members()
        
        elif choice == '3':
            member_id = input("Enter Member ID to update: ")
            name = input("Enter new Name (leave blank to keep current): ")
            email = input("Enter new Email (leave blank to keep current): ")
            age_input = input("Enter new Age (leave blank to keep current): ")
            age = int(age_input) if age_input else None
            library_system.update_member(member_id, name if name else None, email if email else None, age)
        
        elif choice == '4':
            member_id = input("Enter Member ID to delete: ")
            library_system.delete_member(member_id)

        elif choice == '5':
            total_fee = library_system.calculate_total_membership_fee()
            print(f"The total membership fee collected is: ${total_fee}")
        
        elif choice == '6':
            average_fee = library_system.calculate_average_membership_fee()
            print(f"The average membership fee per member is: ${average_fee:.2f}")
        
        elif choice == '7':
            print("Exiting the system.")
            break
        
        else:
            print("Invalid choice! Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
