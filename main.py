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
        print("Data validation failed! Checksum mismatch.")
        print("Stopping!!!")
        return

    print("Requirement 2: Populate point data")
    coordinates = get_coordinates()
    print("Coordinates:", coordinates)
    points=[Point(x,y) for x,y in coordinates]
    print(f"Created {len(points)} Point objects") 

    print("Requirement 3: Find neighbors within distance <= 20")
    max_distance=20
    total_neighbors=0
    neighbors={}
    for point in points:
        neighbors[point]=[]
        for other_point in points:
            if point != other_point:
                distance=point.distance_to(other_point)
                if distance <= max_distance:
                    neighbors[point].append(other_point)
                    total_neighbors+=1

    print("Neighbors:")
    print(f"Total neighbors: {total_neighbors}")
    
    # for point, neighbor_list in neighbors.items():
    #     print(f"{point}: {neighbor_list}")



if __name__ == "__main__":
    main()