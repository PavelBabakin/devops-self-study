import os
import subprocess

def create_user(username, password):
    """
    Create a new user on macOS.

    Args:
    - username (str): The username for the new user.
    - password (str): The password for the new user.
    """

    # Create a new user
    subprocess.run(["sudo", "sysadminctl", "-addUser", username, "-password", password])

    # Create a home directory for the user
    home_directory = f"/Users/{username}"
    if not os.path.exists(home_directory):
        os.makedirs(home_directory)
        print(f"Home directory created at {home_directory}")

    # Set permissions for the home directory
    subprocess.run(["sudo", "chown", username, home_directory])
    subprocess.run(["sudo", "chgrp", "staff", home_directory])
    print(f"Permissions set for {home_directory}")

def main():
    username = input("Enter the username for the new user: ")
    password = input("Enter the password for the new user: ")
    create_user(username, password)

if __name__ == "__main__":
    main()