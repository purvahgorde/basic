string_list = ["apple", "banana", "cherry"]
for item in string_list:
    print(f"Length of '{item}':", len(item))


try:
    print(len(10))  # This will raise an error
except TypeError:
    print("Error: len() does not work on integers.")