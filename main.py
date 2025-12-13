# Main file

from test_data import get_coordinates, get_y_values, get_expected_checksum
from data_validator import validation_results
from points import Point
from graph import Graph
from mst import kruskal_mst, calculate_mst_weight, verify_mst
from visualizer import generate_svg, generate_detailed_svg



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


    print("Requirement 4: Building graph...")
    graph = Graph()
    graph.build_from_points(points, max_distance)
    print(f"Graph constructed")
    print(f"  Vertices: {graph.get_vertex_count()}")
    print(f"  Edges: {graph.get_edge_count()}")
    print()


    print("Requirement 5: Computing Minimum Spanning Tree (Kruskal's Algorithm)...")
    mst_edges = kruskal_mst(graph)
    mst_weight = calculate_mst_weight(mst_edges)
    is_valid_mst, validation_msg = verify_mst(mst_edges, graph.get_vertex_count())
    
    print(f"  MST computed successfully")
    print(f"  MST edges: {len(mst_edges)}")
    print(f"  Total MST weight: {mst_weight:.2f}")
    print(f"  Validation: {validation_msg}")
    print()


    print("Requirement 6: Generating SVG visualizations...")
    
    # Generate main MST visualization
    generate_svg(points, mst_edges, 'mst_output.svg')
    
    # Generate detailed comparison (all edges vs MST)
    generate_detailed_svg(points, graph.edges, mst_edges, 'mst_detailed.svg')
    
    print()


if __name__ == "__main__":
    main()