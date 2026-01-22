def calculate_average(numbers):
    try:
        return sum(numbers) / len(numbers)
    except ZeroDivisionError:
        return 0

def get_list_element(my_list, index):
    try:
        return my_list[index]
    except IndexError:
        print("Error: Index out of bounds")
        return None
    except TypeError:
        print("Error: Provided input is not a list")
        return None

# Example usage
data1 = [10, 20, 30, 40, 50]
data2 = [5, 15]
data3 = []

print(f"Average of data1: {calculate_average(data1)}")
print(f"Average of data2: {calculate_average(data2)}")
print(f"Average of data3: {calculate_average(data3)}")

print(get_list_element([1,2,3], 1))
print(get_list_element([1,2,3], 5))
print(get_list_element("not a list", 0))
