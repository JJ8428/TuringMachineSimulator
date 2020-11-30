# TuringMachineSimulator

<p>This program is Turing Machine (TM) simulator. This program is a master TM that reads a transition table (in a specific format) and acts on a string (in a specific format). Each step, state change, and string change, will be shown on the console in a neatly organized pattern.</p>
<p>Within this directory, I have provided a few TM transitions tables with the exact format in the examples the project PDF displays (These are files with the naming convenction of <b>tm_*.py</b>). You may notices a few differences in terms of looks and naming convention of the states. I will explain the transition table files and expected input/arguments in later sections.</p>

## Dependencies/Requirements:
<p>The only requirement is having atleast Python 3.7. I have tested it on a Ubuntu platforms and Linux department computers and it successfully worked. Any python packages the program use (such as re) are already built into Python or the directory contains the corresponding pyscript for that module, so no need to worry about additional dependencies.</p>

## TM actions I attempted:

These are a list of files that contain transtion tables for TM actions I attempted for the project:

* <b>tm_COMPLEMENT.txt</b> | TM transition table that takes the user input of a binary string and complement it (0 -> 1 and 1 -> 0)
* <b>tm_INCREMENT.txt</b> | TM transition table that takes the user input of a binary string as an integer and adds 1 to it.
* <b>tm_DECREMENT.txt</b> | TM transition table that takes the user input of a binary string as an integer and adds 1 to it.
* <b>tm_PALINDROME.txt</b> | TM transition table that takes the user input of a binary string and accepts if format of (str w ++ str w reversed) is detected.
* <b>tm_ZEROSANDONES.txt</b> | TM transition table that takes the user input of a binary string and accepts if format of (0 occuring 2k times ++ 1 occuring k times, where k is integer >= 0) is detected.
* <b>tm_DIVBY3.txt</b> | TM transition table that takes the user input of a binary string as an integer and accepts if the integer is divisible by 3.

Please note that any transition table file that accepts a binary string as binary number read from left to right (as stated in the project instructions).

## How to run:

```python 
python3 main.py -b $1 -i $2
```
-b/--build is the argument for the path of the file containing the transition table of the action the user desires. Referring to the list of files containg transition tables above stated in the previous section, those are the exact inputs $1 accepts.

-i/--input is the string the user wishes to process. The first character in the input to process must be a blank since the TM will start with its head at the index of 1 in the string. If the program cannot detect a blank your input's first character, it will go ahead and add one itself. Likewise, you do not need to append blanks to the end of the string to ensure it is long enough for the TM to carry out its process. The TM will automatically buffer the string both before and after the string with blank characters if necessary. After all, any TM will make the assumption that the tape is infinite in length. 

# Examples of running the program

Here are 2 examples of commandlines the user can use. This section is to help clear any doubts in how to run the pyscripts.

Suppose the user has the string 'b0001110111000'. The user wants to figure out if the string is a palindrome. The first thing is to check if there exists a transition table that identifies if a string is a palindrome. Yes, we have one called: tm_PALINDROME.txt. All that is to do is to enter the command line. Note that the input string 'b0001110111000' has a blank (b) as its first character. If the input did not have the blank, the program will automatically add it.
```python
python3 main.py -b tm_PALINDROME.txt -i b0001110111000
```
This will print every step and state the TM took and whether the input is accepted/rejected at the bottom of the console text.

Suppose the user wants to complement the string '000111000111'. The first thing is to check if there exists a transition table that complements a string of 0's and 1's. Yes, we have one called tm_COMPLEMENT.txt. All that is to do is to enter the command line. Remember, since the input string does not begin with a blank (b) as its first character, the program will warn the user that the text has no blank (b) as its first character and automically will prepend one. 
```python 
python3 main.py -b tm_COMPLEMENT.txt -i 000111000111
```


