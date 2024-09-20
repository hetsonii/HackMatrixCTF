import binascii
import zipfile
import io

# The hex string representing the ZIP file
hex_data = "485454502f312e3120323030204f4b0d0a436f6e74656e742d547970653a206170706c69636174696f6e2f7a69700d0a436f6e74656e742d4c656e6774683a203234350d0a0d0a504b0304140009000800286b305952164a773f0000004000000008001c00466c61672e7478745554090003fb69e866fb69e86675780b000104e803000004e803000035c1ac6b31632140892da21b27fe2804dad4951f6ddc66976579ff57ef5a99491bd9ea468e3a6e23fea944aaa391cb2ce28b65c9e6536e12b63bedca63de83504b070852164a773f00000040000000504b01021e03140009000800286b305952164a773f00000040000000080018000000000001000000b68100000000466c61672e7478745554050003fb69e86675780b000104e803000004e8030000504b050600000000010001004e000000910000000000"

# Convert hex string to bytes
zip_data = binascii.unhexlify(hex_data)

# Use an in-memory bytes buffer to treat the byte data as a zip file
zip_buffer = io.BytesIO(zip_data)

# Path to the file with passwords (each password on a new line)
password_file_path = 'wordlist1.txt'

# Open the zip file
with zipfile.ZipFile(zip_buffer, 'r') as zip_file:
    # List the contents of the zip file
    zip_file.printdir()

    # Open the file with passwords
    with open(password_file_path, 'r') as password_file:
        # Try each password from the file
        for pwd in password_file:
            pwd = pwd.strip()  # Remove any extra whitespace/newline characters
            try:
                # Attempt to extract the files with the current password
                print(f"Trying password: {pwd}")
                zip_file.extractall("extracted_files", pwd=pwd.encode())  # Password needs to be bytes
                print(f"Success! The correct password is: {pwd}")
                break
            except (RuntimeError, zipfile.BadZipFile):
                print(f"Failed to extract with password: {pwd}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

