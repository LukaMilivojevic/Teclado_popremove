# Remove

## The remove() function removes the first matching value from the list.

customers = [['John', 1],
             ['John', 1],
             ['Lisa', 2],
             ['Rolf', 3],
             ['John', 4]]

## use remove to delete a specific value from a list regardless of the index
## reminder that the remove function removes only the first matching value
customers.remove(['John', 1])

## use remove to basically delete an element from the nested list by index while actually using the value
customers.remove(customers[1])




# Pop

## The pop() function is used to remove an element from the list and return it.

customers = [['John', 1],
             ['Lisa', 2],
             ['Rolf', 3],
             ['John', 4]]

## delete the last element of the nested list and assign it to a variable
## used to explain how the pop returns the deleted element which might be needed to check if we removed the right customer
customer_1 = customers.pop()

## delete the second element of the nested list without assigning the return value
customers.pop(1)









# Showing how the two methods work with higher level of nesting
# A real life example would be grouping customers by towns, countries, etc.


## Remove 

customers = [[["John", 11],["Lisa", 12],["Rolf", 13]],
             [["Murilo", 21],["Joshua", 22]]] # added Murilo and Joshua as a little homage to the question and reply :)

### customers.remove(["John", 11]) example of an error with an explanation of why it doesn't work

### explain how to remove John from the db properly
customers[0].remove(["John", 11]) 

 ### explain how to remove a whole nested list
customers.remove([["Lisa", 12],["Rolf", 13]])

### removing a nested list using remove and index 
### a real life example is - remove all customers in one "batch" which could be a town or country, etc.
customers.remove(customers[0])




## Pop

customers = [[["John", 11],["Lisa", 12],["Rolf", 13]],
             [["Murilo", 21],["Joshua", 22]]]

### deleting the last element from the list (to show how the last element is the whole nested list and what pop does)
customers.pop() 

### deleting the element by index
### compare this to using the index with remove, where we actually use the value but we access it using index
customers[0].pop(0)
