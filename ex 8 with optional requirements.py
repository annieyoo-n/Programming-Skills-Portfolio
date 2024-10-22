

#Exercise 8: Simple Search

# Initialize the list of names
names = ["aysa", "zyan", "ahmad", "raheel", "shaheer", "sara"]

# Search for the specific name "sara"
name_to_find = "sara"

# Check if the name is in the list
if name_to_find in names:
    print(f"{name_to_find} is in the list.")
else:
    print(f"{name_to_find} is not in the list.")
    
    
#Optional Requirements:
    
#Initialize the list of names
names = ["aysa", "zyan", "ahmad", "raheel", "shaheer", "sara"]   
     
# Enter the search term
search_term = input("Enter the name you are looking for: ")

# Check if the name is in the list
if search_term in names:
    print(f"{search_term} is in the list.")
else:
    print(f"{search_term} is not in the list.")
