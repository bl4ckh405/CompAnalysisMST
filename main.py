# Main file

from test_data import get_coordinates, get_y_values, get_expected_checksum
from data_validator import validation_results
from points import Point


def main():
    print("Requirement 1: Validate data using SHA256 checksum")
    y_values = get_y_values()
    expected_checksum = get_expected_checksum()
    print("Y values:", y_values)
    print("Expected checksum:", expected_checksum)
    is_valid=validation_results(y_values, expected_checksum)

    if not is_valid:
        print("ERROR: Data validation failed! Checksum mismatch.")
        print("Aborting execution.")
        return

    print("Requirement 2: Populate point data")
    coordinates = get_coordinates()
    print("Coordinates:", coordinates)
    points=[Point(x,y) for x,y in coordinates]
    print(f"Created {len(points)} Point objects") 



if __name__ == "__main__":
    main()