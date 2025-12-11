import hashlib

def get_checksum(y_data):

    #make all y data into a single string
    concat_data = ''.join(str(y) for y in y_data)

    sha256 = hashlib.sha256()
    sha256.update(concat_data.encode('utf-8'))
    return sha256.hexdigest()

def validate_data(y_data, expected_checksum):
    actual_checksum = get_checksum(y_data)
    if actual_checksum == expected_checksum:
        print("Actual checksum:", actual_checksum)
        return True

    return False

def validation_results(y_data, expected_checksum):
    if validate_data(y_data, expected_checksum):
        print("Data is valid.")
        return True
    else:
        print("Data is invalid.")
        return False