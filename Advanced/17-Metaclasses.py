# Define a metaclass
class AutoAddMeta(type):
    def __new__(cls, name, bases, dct):
        # Automatically add a class-level attribute
        dct['auto_added_attribute'] = 'This is an auto-added attribute'

        # Automatically add a class-level method
        def auto_added_method(cls):
            return f"Auto-added method called in {cls.__name__}"

        dct['auto_added_method'] = classmethod(auto_added_method)

        return super().__new__(cls, name, bases, dct)


# Define a class using the metaclass
class MyClass(metaclass=AutoAddMeta):
    def __init__(self, value):
        self.value = value


# Test the functionality
if __name__ == "__main__":
    # Create an instance of MyClass
    instance = MyClass(42)

    # Access the auto-added attribute
    print(MyClass.auto_added_attribute)  # Output: This is an auto-added attribute

    # Call the auto-added method
    print(MyClass.auto_added_method())  # Output: Auto-added method called in MyClass

    # Check the instance attribute
    print(instance.value)  # Output: 42
