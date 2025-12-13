def normalize_coordinates(points, canvas_width=1200, canvas_height=800, padding=50):
    #Normalize point coordinates to fit within canvas dimensions.
    

    if not points:
        return {}
    
    # Find min and max coordinates
    min_x = min(p.x for p in points)
    max_x = max(p.x for p in points)
    min_y = min(p.y for p in points)
    max_y = max(p.y for p in points)
    
    # Calculate scaling factors
    x_range = max_x - min_x
    y_range = max_y - min_y
    
    # Avoid division by zero
    x_range = x_range if x_range > 0 else 1
    y_range = y_range if y_range > 0 else 1
    
    # Calculate scale to fit in canvas with padding
    x_scale = (canvas_width - 2 * padding) / x_range
    y_scale = (canvas_height - 2 * padding) / y_range
    
    # Normalize coordinates
    normalized = {}
    for point in points:
        norm_x = padding + (point.x - min_x) * x_scale
        # Flip y-axis (SVG y increases downward, but we want up to be positive)
        norm_y = canvas_height - (padding + (point.y - min_y) * y_scale)
        normalized[point] = (norm_x, norm_y)
    
    return normalized


def generate_svg(points, mst_edges, filename='mst_output.svg', 
                canvas_width=1200, canvas_height=800):
    #Generate SVG visualization of the MST.
    

    # Normalize coordinates
    normalized = normalize_coordinates(points, canvas_width, canvas_height)
    
    # Start SVG
    svg_lines = [
        f'<?xml version="1.0" encoding="UTF-8"?>',
        f'<svg width="{canvas_width}" height="{canvas_height}" xmlns="http://www.w3.org/2000/svg">',
        f'  <!-- Minimum Spanning Tree Visualization -->',
        f'  <!-- Total Points: {len(points)} | MST Edges: {len(mst_edges)} -->',
        '',
        f'  <!-- Background -->',
        f'  <rect width="{canvas_width}" height="{canvas_height}" fill="#f8f9fa"/>',
        '',
        f'  <!-- MST Edges -->',
        f'  <g id="mst-edges" stroke="#2563eb" stroke-width="2" opacity="0.7">',
    ]
    
    # Draw MST edges
    for point1, point2, weight in mst_edges:
        x1, y1 = normalized[point1]
        x2, y2 = normalized[point2]
        svg_lines.append(
            f'    <line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}"/>'
        )
    
    svg_lines.append('  </g>')
    svg_lines.append('')
    
    # Draw points
    svg_lines.append(f'  <!-- Points (Vertices) -->')
    svg_lines.append(f'  <g id="points">')
    
    for point in points:
        x, y = normalized[point]
        svg_lines.append(
            f'    <circle cx="{x:.2f}" cy="{y:.2f}" r="4" '
            f'fill="#dc2626" stroke="#fff" stroke-width="1"/>'
        )
    
    svg_lines.append('  </g>')
    svg_lines.append('')
    
    # Add title
    svg_lines.extend([
        f'  <!-- Title -->',
        f'  <text x="{canvas_width/2}" y="30" text-anchor="middle" '
        f'font-family="Arial, sans-serif" font-size="24" font-weight="bold" fill="#1f2937">',
        f'    Minimum Spanning Tree',
        f'  </text>',
        f'  <text x="{canvas_width/2}" y="55" text-anchor="middle" '
        f'font-family="Arial, sans-serif" font-size="14" fill="#6b7280">',
        f'    {len(points)} Points | {len(mst_edges)} Edges | '
        f'Total Weight: {sum(w for _, _, w in mst_edges):.2f}',
        f'  </text>',
        '',
    ])
    
    # Add legend
    svg_lines.extend([
        f'  <!-- Legend -->',
        f'  <g id="legend" transform="translate(20, {canvas_height - 60})">',
        f'    <rect width="200" height="50" fill="white" stroke="#d1d5db" rx="5"/>',
        f'    <line x1="15" y1="20" x2="45" y2="20" stroke="#2563eb" stroke-width="2"/>',
        f'    <text x="55" y="24" font-family="Arial" font-size="12" fill="#374151">MST Edge</text>',
        f'    <circle cx="30" cy="37" r="4" fill="#dc2626" stroke="#fff" stroke-width="1"/>',
        f'    <text x="55" y="41" font-family="Arial" font-size="12" fill="#374151">Point</text>',
        f'  </g>',
    ])
    
    # Close SVG
    svg_lines.append('</svg>')
    
    # Write to file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('\n'.join(svg_lines))
    
    print(f"[OK] SVG visualization saved to: {filename}")


def generate_detailed_svg(points, all_edges, mst_edges, filename='mst_detailed.svg',
                         canvas_width=1200, canvas_height=800):
    #Generate detailed SVG showing both all edges and MST edges.
    

    # Normalize coordinates
    normalized = normalize_coordinates(points, canvas_width, canvas_height)
    
    # Start SVG
    svg_lines = [
        f'<?xml version="1.0" encoding="UTF-8"?>',
        f'<svg width="{canvas_width}" height="{canvas_height}" xmlns="http://www.w3.org/2000/svg">',
        f'  <rect width="{canvas_width}" height="{canvas_height}" fill="#f8f9fa"/>',
        '',
        f'  <!-- All Edges (Gray) -->',
        f'  <g id="all-edges" stroke="#d1d5db" stroke-width="1" opacity="0.3">',
    ]
    
    # Draw all edges in gray
    for point1, point2, _ in all_edges:
        x1, y1 = normalized[point1]
        x2, y2 = normalized[point2]
        svg_lines.append(
            f'    <line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}"/>'
        )
    
    svg_lines.append('  </g>')
    svg_lines.append('')
    
    # Draw MST edges in blue
    svg_lines.append(f'  <!-- MST Edges (Blue) -->')
    svg_lines.append(f'  <g id="mst-edges" stroke="#2563eb" stroke-width="2.5" opacity="0.8">')
    
    for point1, point2, _ in mst_edges:
        x1, y1 = normalized[point1]
        x2, y2 = normalized[point2]
        svg_lines.append(
            f'    <line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}"/>'
        )
    
    svg_lines.append('  </g>')
    svg_lines.append('')
    
    # Draw points
    svg_lines.append(f'  <!-- Points -->')
    svg_lines.append(f'  <g id="points">')
    
    for point in points:
        x, y = normalized[point]
        svg_lines.append(
            f'    <circle cx="{x:.2f}" cy="{y:.2f}" r="4" '
            f'fill="#dc2626" stroke="#fff" stroke-width="1.5"/>'
        )
    
    svg_lines.append('  </g>')
    svg_lines.append('')
    
    # Add title
    svg_lines.extend([
        f'  <text x="{canvas_width/2}" y="30" text-anchor="middle" '
        f'font-family="Arial" font-size="24" font-weight="bold" fill="#1f2937">',
        f'    MST vs All Edges Comparison',
        f'  </text>',
        f'  <text x="{canvas_width/2}" y="55" text-anchor="middle" '
        f'font-family="Arial" font-size="14" fill="#6b7280">',
        f'    All Edges: {len(all_edges)} (gray) | MST Edges: {len(mst_edges)} (blue)',
        f'  </text>',
    ])
    
    svg_lines.append('</svg>')
    
    # Write to file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('\n'.join(svg_lines))
    
    print(f"[OK] Detailed SVG saved to: {filename}")
