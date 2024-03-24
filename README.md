**1.calendar_module()**
* This Python script defines a function find_day() to determine the day of the week for a given input date.
* It prompts the user to input a date in the format 'month day year', converts it to a datetime.date object, calculates the day of the week using .weekday(), and returns the corresponding day in uppercase after logging it.

**2.collections_namedtuples()**

* This Python script defines a function calculate_average() to compute the average marks of students. 
* It first reads the number of students, their column names, and calculates the average of marks by summing up marks and dividing by the number of students. 
* The script then logs the result to two decimal places using the logging module.

**3.find_the_percentage_problem()**

* This Python script defines a function calc_average() in a module named util.py to calculate the average marks of a student.
* It first reads the number of students, their names, and their marks. 
* Then it computes the average marks for a queried student's name by extracting their marks from the dictionary, calculating the average, formatting it to two decimal places, and finally logs the result using the logging module.

**4.find_the_runner_up()**

* This Python script defines a function find_runner_up_score() to find the second highest score among a list of scores. 
* It prompts the user to input the number of scores and the scores themselves. 
* It then sorts the unique scores in descending order, returning the second element if it exists, else it logs a message indicating that there is no second maximum score. Finally, it logs the result using the logging module.

**5.floor_ceil_rint()**

* This Python script defines a function print_floor_ceil_rint() to perform floor, ceil, and round operations on an input array using NumPy. 
* It reads a space-separated input and converts it into a NumPy array of floats. 
* Then it calculates the floor, ceil, and rounded values of the array elements. Finally, it returns these arrays and logs each of them using the logging module, displaying the result of floor, ceil, and round operations respectively.

**6.iterables_iterators()**

* This Python script defines a function probability_of_letter() to calculate the probability of selecting at least one unique letter from a given list of letters for a specific number of selections. It reads an integer n, a list of letters, and another integer k. 
* Then, it computes the total number of combinations and the combinations that include at least one unique letter among the first k selections. 
* Finally, it calculates the probability by dividing the latter by the former, formats it to four decimal places, and logs the result using the logging module.

**7.linear_algebra()**
* This Python script defines a function calculate_determinant() to compute the determinant of a square matrix.
* It first reads an integer n representing the size of the square matrix and then reads the matrix itself row by row. It utilizes NumPy's np.linalg.det() function to compute the determinant of the matrix and logs the result formatted to two decimal places using the logging module.

**8.mean_var_std()**

* This Python script defines a function calculate_statistics() to compute statistics (mean, variance, and standard deviation) along rows for a 2D array. 
* It reads two integers X and Y representing the dimensions of the array. Then, it reads the array row by row.
* Using NumPy functions np.mean(), np.var(), and np.std(), it computes the mean, variance, and standard deviation along the rows respectively. Finally, it logs each statistic array and returns.

**9.merge_the_tools()**
* This Python script defines a function merge_the_tools() to split a string into substrings of length k, removing duplicate characters within each substring. 
* It reads the input string s and the integer k. Then, it iterates over s in steps of k, creating substrings. 
* Within each substring, it keeps track of unique characters and appends them to the result list. Finally, it joins the resulting substrings with newline characters and logs the output using the logging module.

**10.min_max_axis()**

* This Python script defines a function min_max() to find the maximum value among the minimum values of each row in a 2D array. It reads an integer X representing the number of rows, and then reads the array row by row. 
* Utilizing NumPy's np.min() function with axis=1, it computes the minimum values along the rows, then finds the maximum of these minimum values. 
* Finally, it logs and returns the maximum value using the logging module.

**11.mutate_srting()**

* This Python script defines a function mutate_string() to replace a character in a string at a specified position.
* It reads an input string s and a position-character pair.
* It then converts the position to an integer and replaces the character at that position in the string s with the specified character. Finally, it logs and returns the modified string using the logging module.

**12.no_idea_problem()**
	
* This Python script defines a function calculate_happiness() to compute happiness based on elements in an array that are liked or disliked. 
* It reads two integers n and m representing the size of the array and the number of elements in the like and dislike sets respectively.
* Then, it reads the array and the sets of liked and disliked elements.
* Iterating over the array, it increments the happiness if an element is in the liked set and decrements it if it's in the disliked set. Finally, it logs and returns the computed happiness using the logging module.

**13.piling_up()**
* This Python script defines a function can_stack_cubes() to determine if a given arrangement of cubes can be stacked. It reads an integer T representing the number of test cases. 
* For each test case, it reads an integer n indicating the number of cubes and a list of integers representing the sizes of the cubes. 
* Then, it iterates through the cubes from both ends, ensuring that each cube can be stacked on top of the previous one.
* If the condition is met for all cubes, it returns "Yes"; otherwise, it returns "No". Finally, it logs and returns the result using the logging module

**14.python_string_formatted()**
* This Python script defines a function print_formatted() in a module named util.py to print formatted representations of numbers up to a specified maximum value. 
* It reads an integer number representing the maximum value to print.
* Then, it calculates the width of the binary representation by finding the length of the binary string without the '0b' prefix. It iterates over numbers from 1 to the maximum, converting each number into decimal, octal, hexadecimal, and binary representations.
* Finally, it logs and prints each representation right-justified with width obtained earlier using the logging module.

**15.text_alignment()**
* This Python script defines a function print_hackerrank_logo() to print the HackerRank logo using a specified character and thickness. 
* It reads an integer thickness representing the thickness of the logo. 
* The function then iterates through different sections of the logo, including the top cone, top pillars, middle belt, bottom pillars, and bottom cone, printing each section accordingly.
* Finally, it logs and prints the generated logo using the logging module.

**16.time_delta()**
* This Python script defines a generator function get_time_difference() to compute the absolute time difference in seconds between two timestamps provided in a specific format. 
* It first reads the number of test cases and then iterates through each test case. 
* For each test case, it reads two timestamps as strings and converts them into datetime objects using a specified date format. It then calculates the absolute time difference in seconds and yields the result. Finally, it logs each time difference using the logging module.



**17.validate_email()**
* This Python script defines a function validating_email() to filter and validate a list of email addresses based on a specific regex pattern.
* It reads an integer n representing the number of email addresses. 
* It then reads n email addresses into a list, filters them using the filter_mail() function based on whether they match the defined email format, sorts the filtered list, logs the result, and returns the filtered and sorted email addresses.
* The regex pattern email_format defines a basic structure for valid email addresses, which include alphanumeric characters, hyphens, and underscores before the "@" symbol, followed by alphanumeric characters and a dot, and ending with 1 to 3 alphabetic characters for the domain extension.

**18.word_order()**
* This Python script defines a function count_word_occurrences() to count the occurrences of words in a list and determine the number of distinct words.

* It reads an integer n representing the number of words, followed by n words into a list. It then iterates through the list, counting the occurrences of each word using a dictionary. 

* Finally, it calculates the number of distinct words and the occurrences of each word, logs them using the logging module, and returns these values.

