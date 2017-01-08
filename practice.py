"""List Practice

Edit the functions until all of the doctests pass when
you run this file.
"""


def print_list(items):
    """Print each item in the input list.

    For example::

        >>> print_list([1, 2, 6, 3, 9])
        1
        2
        6
        3
        9
    """

    for item in items:          # Simple traversal of the list. Printing each time we pass.
        print item


def long_words(words):
    """Return words in input list that longer than 4 characters.

    For example::

        >>> long_words(["hello", "a", "b", "hi", "bacon", "bacon"])
        ['hello', 'bacon', 'bacon']

    (If there are duplicates, show both --- notice "bacon" appears
    twice in output)

    If no words are longer than 4 characters, return an empty list::

        >>> long_words(["all", "are", "tiny"])
        []
    """

    #return filter(lambda word: len(word)>4, words)         # Playing with filters. It works too.
    return [word for word in words if len(word) > 4]        # Using comprehension to select the word that are longer than 4. Autogenerating a list.


def n_long_words(words, n):
    """Return words in list longer than `n` characters.

    For example::

        >>> n_long_words(
        ...     ["hello", "hey", "spam", "spam", "bacon", "bacon"],
        ...     3
        ... )
        ['hello', 'spam', 'spam', 'bacon', 'bacon']

        >>> n_long_words(["I", "like", "apples", "bananas", "you"], 5)
        ['apples', 'bananas']
    """

    return [word for word in words if len(word) > n]  # Using comprehension to select the word that are longer than "n". Autogenerating a list.


def smallest_int(numbers):
    """Find the smallest integer in a list of integers and return it.

    **DO NOT USE** the built-in function `min()`!

    For example::

        >>> smallest_int([-5, 2, -5, 7])
        -5

        >>> smallest_int([3, 7, 2, 8, 4])
        2

    If the input list is empty, return `None`::

        >>> smallest_int([]) is None
        True
    """
    min_number = None
    if len(numbers) != 0 :              # Check it is not an empty list. If it is I am returning None
        min_number = numbers[0]         # Will be comparing two numbers. Initialize my minimun number with the 1st element
        for number in numbers[1:]:      # traverse list from the second element until the end
            if number < min_number:     # compare if my current minimun value is bigger than the current item in the list
                min_number = number     # if it is the case. I update my min number
            
    return min_number


def largest_int(numbers):
    """Find the largest integer in a list of integers and return it.

    **DO NOT USE** the built-in function `max()`!

    For example::

        >>> largest_int([-5, 2, -5, 7])
        7

        >>> largest_int([3, 7, 2, 8, 4])
        8

    If the input list is empty, return None::

        >>> largest_int([]) is None
        True
    """

    max_number = None
    if len(numbers) != 0 :              # Check it is not an empty list. If it is I am returning the original "None"
        max_number = numbers[0]         # Will be comparing two numbers. Initialize my max number with the 1st element
        for number in numbers[1:]:      # traverse list from the second element until the end
            if number > max_number:     # compare if my current max value is bigger than the current item in the list
                max_number = number     # if it is the case. I update my max number

    return max_number


def halvesies(numbers):
    """Return list of numbers from input list, each divided by two.

    For example::

        >>> halvesies([2, 6, -2])
        [1.0, 3.0, -1.0]

    If any of the numbers are odd, make sure you don't round off
    the half::

        >>> halvesies([1, 5])
        [0.5, 2.5]
    """

    return [num/2.0 for num in numbers]         # Traverse list dividing by float 2 to get floating number.


def word_lengths(words):
    """Return the length of words in the input list.

    For example::

        >>> word_lengths(["hello", "hey", "hello", "spam"])
        [5, 3, 5, 4]
    """

    return [len(word) for word in words]        # Traverse list using comprehension using len() for each item


def sum_numbers(numbers):
    """Return the sum of all of the numbers in the list.

    Python has a built-in function, `sum()`, which already does
    this --- but for this exercise, you should not use it.

    For example::

        >>> sum_numbers([1, 2, 3, 10])
        16

    Any empty list should return the sum of zero::

        >>> sum_numbers([])
        0
    """

    return reduce(lambda x, y: x + y, numbers, 0)       # Reduce function to add all the numbers initialized with zero in case is an empty list.


def mult_numbers(numbers):
    """Return product (result of multiplication) of numbers in list.

    For example::

        >>> mult_numbers([1, 2, 3])
        6

    Obviously, if there is a zero in input, the product is zero::

        >>> mult_numbers([10, 20, 0, 50])
        0

    As explained at http://en.wikipedia.org/wiki/Empty_product,
    if the list is empty, the product should be 1::

        >>> mult_numbers([])
        1
    """

    return reduce(lambda x, y: x * y, numbers, 1)       # Reduce function to multiply all the numbers initialized with zero in case is an empty list. 


def join_strings(words):
    """Return a string of all input strings joined together.

    Python has a built-in method, `list.join()` --- but for
    this exercise, **you should not use it**.

    For example::

        >>> join_strings(["spam", "spam", "bacon", "balloonicorn"])
        'spamspambaconballoonicorn'

    For an empty list, you should return an empty string::

        >>> join_strings([])
        ''
    """

    return reduce(lambda x, y: x + y, words, '')       # Reduce function to add all the strings. Initialized with "" in case is an empty list. 


def average(numbers):
    """Return the average (mean) of the list of numbers given.

    For example::

        >>> average([2, 4])
        3.0

    This should handle cases where the result isn't an integer::

        >>> average([2, 12, 3])
        5.666666666666667

    There is no defined answer if the list given is empty;
    it's fine if this raises an error when given an empty list.

    (Think of the best way to handle an empty input list, though,
    a feel free to provide a good solution here.)
    """

    total_sum = reduce(lambda x, y: x+y, numbers, 0)        # Accumulate all the integers. Initialize with Zero in case I get an empty list
    qty_numbers = len(numbers)
    if qty_numbers  == 0:
        average_total= None                                 # Return a None, so that the user can handle the return.
    else:
        average_total = float(total_sum) / qty_numbers         # COnvert to float to be able to handle float numbers or results. Divide by total numbers.

    return average_total


def join_strings_with_comma(words):
    """Return ['list', 'of', 'words'] like "list, of, words".

    For example::

        >>> join_strings_with_comma(
        ...     ["Labrador", "Poodle", "French Bulldog"]
        ...     )
        'Labrador, Poodle, French Bulldog'

    If there's only one thing in the list, it should return just that
    thing, of course::

        >>> join_strings_with_comma(["Pretzel"])
        'Pretzel'
    """

    comma_words = reduce(lambda x, y: x + y + ', ', words, '')       # Reduce function to add all the strings initialized with "" in case is an empty list. 

    return  comma_words[:-2]                      # the last concatenation will have and extra comma and an space. Cut before returning.

def reverse_list(items):
    """Return the input list, reversed.

    **Do not use** the python function `reversed()` or the method
    `list.reverse()`.

    For example::

        >>> reverse_list([1, 2, 3])
        [3, 2, 1]

        >>> reverse_list(["cookies", "love", "I"])
        ['I', 'love', 'cookies']

    You should do this without changing the original list::

        >>> orig = ["apple", "berry", "cherry"]
        >>> reverse_list(orig)
        ['cherry', 'berry', 'apple']
        >>> orig
        ['apple', 'berry', 'cherry']
    """
    
    # In case -1 is not allowed, this is the for solution. I tested it, it works. Generates a lot of garbage in memory
    #new_list = []
    #for item in items:
    #    new_list = [item] + new_list
    #return new_list

    return items[::-1]          # slice entire string backwards. My other solution is commented right above this, in case slicing is not permitted.


def reverse_list_in_place(items):
    """Reverse the input list `in place`.

    Reverse the input list given, but do it "in place" --- that is,
    do not create a new list and return it, but modify the original
    list.

    **Do not use** the python function `reversed()` or the method
    `list.reverse()`.

    For example::

        >>> orig = [1, 2, 3]
        >>> reverse_list_in_place(orig)
        >>> orig
        [3, 2, 1]

        >>> orig = ["cookies", "love", "I"]
        >>> reverse_list_in_place(orig)
        >>> orig
        ['I', 'love', 'cookies']
    """

    for i in range(len(items)):             # Traverse the entire list
        items.insert(i, items.pop())        # Inserting from the beggining and in sequence what we popped at the end of the list.

    return None                        # Return nothing since list was midified In Place.


def duplicates(items):
    """Return list of words from input list which were duplicates.

    Return a list of words which are duplicated in the input list.
    The returned list should be in ascending order.

    For example::

        >>> duplicates(
        ...     ["apple", "banana", "banana", "cherry", "apple"]
        ... )
        ['apple', 'banana']

        >>> duplicates([1, 2, 2, 4, 4, 4, 7])
        [2, 4]

    You should do this without changing the original list::

        >>> orig = ["apple", "apple", "berry"]
        >>> duplicates(orig)
        ['apple']

        >>> orig
        ['apple', 'apple', 'berry']
    """
    duplicate_items = []
    for i in range(len(items)):
        item = items[i]
        if item in items[i+1:] and item not in duplicate_items: # Look for duplicates in the remainder of the list and if is not listed as duplixate already
            duplicate_items.append(items[i])                    # Add to the list of deplicates
   
    return sorted(duplicate_items)                              # Return a newly created sorted list


def find_letter_indices(words, letter):
    """Return list of indices where letter appears in each word.

    Given a list of words and a letter, return a list of integers
    that correspond to the index of the first occurrence of the letter
    in that word.

    **DO NOT** use the `list.index()` method.

    For example::

        >>> find_letter_indices(['odd', 'dog', 'who'], 'o')
        [0, 1, 2]

    ("o" is at index 0 in "odd", is at index 1 in "dog", and at
    index 2 in "who")

    If the letter doesn't occur in one of the words, use `None` for
    that word in the output list. For example::

        >>> find_letter_indices(['odd', 'dog', 'who', 'jumps'], 'o')
        [0, 1, 2, None]

    ("o" does not appear in "jumps", so the result for that input is
    `None`.)
    """

    special_list = []
    
    for word in words:                      # Traverse the words in the list
        for i in range(len(word)):          # Traverse each word by character
            if(letter == word[i]):          # If a character match the target original letter
                special_list.append(i)      # Add the index where it was found in the results list
                break                       # Since we found a match, we don't need to keep looking (we only need the first finding)
        else:                               # If the loop fell through without finding a match. Break was never called if this line is reached.
            special_list.append(None)       # "None" is added instead of index (Practice with continue statement instead of break)
        
    
    return special_list                     # Return the list

#####################################################################
# END OF PRACTICE: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
