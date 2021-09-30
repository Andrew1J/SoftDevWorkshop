# K06 -- Random Occupation Picker
SoftDev </br>
The Best Team - Alif Abdullah, Andrew Juang, Joshua Kloepfer </br>
2021-09-29 </br>

## File Handling
- We used the csv module's DictReader function to convert the csv file into a dictionary. 
- We opened up the csv file with the "with open" keywords. 
- We stored the contents of the csv file in the variable reader. 
- We iterated through each row of the contents of reader using a variable called row. 
- We then stored the contents of each Job Class column element as a key in our dictionary finalDict, and stored the corresponding Percentage column element as the corresponding value to the key.

## Dictionary vs. Lists
- Dictionaries are useful because they allow you to have values correspond to a key rather than an index, and thus have create connections between two sets of lists of elements. To access a particular value, you need to know the key associated with that value. 

- Lists are useful as they associate a set of elements to a set of corresponding integers called indices. Unlike the dictionary, you only need one set of elements to create the list. To access any particular list value, you must know the index associated with that value.

## Purpose of Markdown
- Markdown is a robust typing language that offers users the ability to style their text in a matter of seconds. It combines the structure of html with the aesthetic prowess of css in an easy to learn language.
- Here is a helpful guide : https://guides.github.com/features/mastering-markdown/

## Weighted Randomized Selection
- We randomly generated a number from 0 to 1000, and stored it into the variable x.
- We then iterated through the function parameter reader, a dictionary. 
- We then added each of the value elements, times 10 (this is done to accomodate the fact that a random number is chosen out of 1000), to the variable y, initialized to 0. 
- Whenever y is greater than x, the program will print out the key associated to the current value, and stop. 
- The program selection is weighted due to the intervals set by the percentages.
