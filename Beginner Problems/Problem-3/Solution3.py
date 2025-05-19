inputlist = ["ai", "ml", "python", "ml", "dl", "ai"]

def find_duplicates(lists):
    seen = set()
    duplicates = set()
    for item in lists:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
            
    return list(duplicates)

dups = find_duplicates(inputlist)
print(dups)