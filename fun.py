# Importing a module for additional functionality
import random

# Function to generate a list of random numbers
def generate_random_list(size, min_value, max_value):
    """
    Generate a list of random integers.

    :param size: Number of elements in the list
    :param min_value: Minimum value for random numbers
    :param max_value: Maximum value for random numbers
    :return: List of random integers
    """
    return [random.randint(min_value, max_value) for _ in range(size)]

# Simple class to represent a person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        """
        Method to introduce the person with their name and age.
        """
        return f"Hi, I'm {self.name} and I am {self.age} years old."

# Main execution block
if __name__ == "__main__":
    # Generate a list of 5 random numbers between 1 and 100
    random_numbers = generate_random_list(5, 1, 100)
    print("Random numbers:", random_numbers)

    # Sorting the list in ascending order
    sorted_numbers = sorted(random_numbers)
    print("Sorted numbers:", sorted_numbers)

    # Creating instances of the Person class
    person1 = Person("Alice", 30)
    person2 = Person("Bob", 25)

    # Using the introduce method
    print(person1.introduce())
    print(person2.introduce())
