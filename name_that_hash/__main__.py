#! /usr/bin/env python3

"""
Name That Hash: Name the hash type.

"""


import sys

if __name__ == "__main__":
    minor = sys.version_info[1]

    major = sys.version_info[0]
    python_version = f"{str(sys.version_info[0])}.{str(sys.version_info[1])}.{str(sys.version_info[2])}"

    if major != 3 or minor < 6:
        print(
            f"Name That Hash requires Python 3.7+, you are using {python_version}. Please install a higher Python version."
        )
        sys.exit(1)

    from name_that_hash import runner

    runner.main()
