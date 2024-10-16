#1. Lists: Creating, Accessing, and Modifying Lists
#list index start from 0
#create a list

fruits=['mango','apple','orange']
#accessing
print(fruits[2])

#modifying a list
fruits.insert(2,'pista')
print(fruits)
fruits[1] = 'blueberry'
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']
#append use to add at last
fruits.append('date')
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'date']

fruits.remove('apple')
print(fruits)  # Output: ['blueberry', 'cherry', 'date']


#2.Tupple
colors = ('red', 'green', 'blue')
#accessing items
print(colors[0])  # Output: red
print(colors[2])  # Output: blue
#Tuples are Immutable: You can’t modify items in a tuple.
# colors[1] = 'yellow'  # This will raise an error




#3. Dictionaries: Key-Value Pairs for Storing Data

#create dictionary
person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
print(person['name'])  # Output: Alice

person['age'] = 30
print(person)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}

person['email'] = 'alice@example.com'
print(person)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'email': 'alice@example.com'}

del person['city']
print(person)  # Output: {'name': 'Alice', 'age': 30, 'email': 'alice@example.com'}



#4.set
#Unique Elements: Sets automatically remove duplicates.


numbers = {1, 2, 3, 4}

 #add or remove items

numbers.add(5)
print(numbers)  # Output: {1, 2, 3, 4, 5}

numbers.remove(3)
print(numbers)  # Output: {1, 2, 4, 5}


#List Operations:

#Create a list of your favorite movies. Add a new movie to the list, remove one, and print the updated list.
# Create a list of your favorite movies
favorite_movies = ['Inception', 'The Matrix', 'Interstellar']

# Add a new movie to the list
favorite_movies.append('The Dark Knight')

# Remove one movie from the list
favorite_movies.remove('The Matrix')

# Print the updated list
print('Updated favorite movies:', favorite_movies)

#Tuple Operations:

#Create a tuple of your top 3 travel destinations. Try accessing the second item in the tuple.
# Create a tuple of your top 3 travel destinations
travel_destinations = ('Japan', 'Switzerland', 'New Zealand')

# Access the second item in the tuple
second_destination = travel_destinations[1]
print('Second travel destination:', second_destination)

#Dictionary Operations:

#Create a dictionary to store information about a book (title, author, year). Update the year, add a new key-value pair for genre, and delete the author key.
# Create a dictionary to store information about a book
book_info = {
    'title': 'To Kill a Mockingbird',
    'author': 'Harper Lee',
    'year': 1960
}

# Update the year
book_info['year'] = 1961

# Add a new key-value pair for genre
book_info['genre'] = 'Fiction'

# Delete the author key
del book_info['author']

# Print the updated dictionary
print('Updated book information:', book_info)

#Set Operations:

#Create a set of unique student IDs. Add a new ID and try adding a duplicate ID. Print the set to see the result.

# Create a set of unique student IDs
student_ids = {101, 102, 103}

# Add a new ID to the set
student_ids.add(104)

# Try adding a duplicate ID
student_ids.add(102)

# Print the set to see the result
print('Updated student IDs:', student_ids)








