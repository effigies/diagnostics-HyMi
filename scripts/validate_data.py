""" Python script to validate data

Run as:

    python3 scripts/validata_data.py data
"""


import os.path as op
import sys
import hashlib
import os

def file_hash(filename):
    """ Get byte contents of file `filename`, return SHA1 hash

    Parameters
    ----------
    filename : str
        Name of file to read

    Returns
    -------
    hash : str
        SHA1 hexadecimal hash string for contents of `filename`.
    """
    # Open the file, read contents as bytes.
    read_file = open(filename, 'rb')
    file = read_file.read()
    read_file.close()
    # Calculate, return SHA1 has on the bytes from the file.
    return hashlib.sha1(file).hexdigest()



def validate_data(data_directory):
    """ Read ``hash_list.txt`` file in ``data_directory``, check hashes

    An example file ``data_hashes.txt`` is found in the baseline version
    of the repository template for your reference.

    Parameters
    ----------
    data_directory : str
        Directory containing data and ``hash_list.txt`` file.

    Returns
    -------
    None

    Raises
    ------
    ValueError:
        If hash value for any file is different from hash value recorded in
        ``hash_list.txt`` file.
    """
    # Read lines from ``hash_list.txt`` file.
    file = open(op.join(data_directory, 'group-01', 'hash_list.txt'), 'rt')
    for i in file.readlines():
        # Split into SHA1 hash and filename
        hash, fname = i.strip().split()

        # Calculate actual hash for given filename.
        hash_calc = file_hash(op.join(data_directory, fname))

        # If hash for filename is not the same as the one in the file, raise
        # ValueError
        if hash != hash_calc:
            raise ValueError("Hash does not match".format(fname))


def main():
    # This function (main) called when this file run as a script.
    #
    # Get the data directory from the command line arguments
    if len(sys.argv) < 2:
        raise RuntimeError("Please give data directory on "
                           "command line")
    data_directory = sys.argv[1]
    # Call function to validate data in data directory
    validate_data(data_directory)


if __name__ == '__main__':
    # Python is running this file as a script, not importing it.
    main()
