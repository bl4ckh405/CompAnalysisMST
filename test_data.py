#Contains test data

# X values: 1 to 100
X_VALUES = list(range(1, 101))

# Y values from the test data file init1
Y_VALUES = [
    20, 93, 72, 35, 54, 95, 25, 37, 29, 72,
    65, 66, 49, 43, 35, 61, 97, 66, 64, 22,
    83, 69, 19, 21, 69, 40, 35, 81, 15, 41,
    74, 12, 3, 65, 31, 12, 48, 68, 41, 40,
    99, 13, 70, 30, 20, 35, 84, 96, 1, 93,
    61, 83, 24, 27, 93, 86, 96, 43, 10, 51,
    27, 87, 40, 35, 83, 44, 15, 89, 71, 79,
    25, 84, 43, 49, 66, 0, 88, 80, 4, 3,
    74, 10, 41, 45, 75, 34, 41, 44, 50, 99,
    41, 37, 26, 6, 94, 94, 76, 48, 32, 42
]

# Expected SHA256 checksum for validation
EXPECTED_CHECKSUM = "5c14e4599f1d2a39abe6b487ac2a5415c894c6882f5fdd4a40e02c7dd628829a"

# Concatenated y values string (for reference)
Y_VALUES_STRING = '20937235549525372972656649433561976664228369192169403581154174123653112486841409913703020358496193618324279386964310512787403583441589717925844349660880437410414575344144509941372669494764832422'


def get_coordinates():
   # Returns a list of (x, y) coordinate tuples.
    
    if len(X_VALUES) != len(Y_VALUES):
        raise ValueError(f"X and Y value counts don't match: {len(X_VALUES)} vs {len(Y_VALUES)}")
    
    return list(zip(X_VALUES, Y_VALUES))


def get_y_values():
    # Returns the list of y values.
    return Y_VALUES.copy()


def get_expected_checksum():
    # Returns the expected SHA256 checksum.
    return EXPECTED_CHECKSUM
