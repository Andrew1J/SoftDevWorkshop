# K06 -- Random Occupation Picker
SoftDev </br>
The Best Team - Andrew Juang, Alif Abdullah, Joshua Kloepfer </br>
2021-09-29 </br>

## File Handling
- We used the Python CSV module's DictReader function to conver the CSV file into a dictionary. 
- We opened up the CSV file with the "with open" keywords.
- We stored the contents of the CSV file in the variable reader.
- We iterated through each row of the contents of reader using a variable called row.
- We then stored the contents of each Job Class column element as a key in our dictionary finaldict, and stored the corresponding Percentage column element as the corresponding value to the key.

## Dictionaries vs Lists 
- We used a dictionary because they allow you to have values correspond to a key which can be any datatype, rather than an index. This allows us to access the percentages from the job/class name. 
- Lists are useful because they associate a set of elements to a set of corresponding integers called indices. Unlike the dictionary, you only need one set of elements to create the list. To access any particular list value, you must know the index associated with the value. 

## Purpose of Markdown
- Markdown is a robust typing language that offers users the ability to style their text in a matter of seconds. It combines the structure of HTML with the aesthetic prowess of CSS in an easy to learn language.

## Weighted Randomized Selection
- 
