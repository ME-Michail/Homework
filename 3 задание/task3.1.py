def count_letter(words,char):
    count= 0
    for word in words:
        for char1 in word:
            if char1.lower() in char.lower():
                count += 1
    return count
print(count_letter(['python', 'c++', 'c', 'scala', 'java'],"c"))