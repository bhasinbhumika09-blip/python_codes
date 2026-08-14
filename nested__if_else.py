age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("Entry denied - ID required")
else:
    print("Entry denied - must be 18 or older")
