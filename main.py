# Main file

from test_data import get_coordinates, get_y_values, get_expected_checksum

def main():
    print("Task 1: Validate data using SHA256 checksum")
    y_values = get_y_values()
    expected_checksum = get_expected_checksum()
    print("Y values:", y_values)
    print("Expected checksum:", expected_checksum)
    




if __name__ == "__main__":
    main()