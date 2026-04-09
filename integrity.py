# integrity.py

data = input("Enter data packet: ")

if data == data[::-1]:
    print("Data Integrity Verified (Palindrome)")
else:
    print("Data Corrupted")
