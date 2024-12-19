# python-Electric-Current-Calculator
Electric Current Calculator Using Ohm's Law in Python
Objective:
The purpose of this project is to create a Python program that calculates the electric current in a circuit based on user inputs for voltage and resistance. The program will use Ohm's Law to perform the calculation, making it an essential tool for students and professionals in electrical engineering, physics, and related fields.

Overview:
Ohm’s Law defines the relationship between voltage, current, and resistance in an electrical circuit. The formula is:

𝐼
=
𝑉
𝑅
I= 
R
V
​
 
Where:

𝐼
I is the current (measured in amperes, A),
𝑉
V is the voltage (measured in volts, V),
𝑅
R is the resistance (measured in ohms, Ω).
By rearranging this formula, we can calculate the electric current (
𝐼
I) when given the values for voltage and resistance. This calculator will take user input for voltage and resistance, calculate the current, and display the result.

Key Features:
Ohm's Law Calculation: The program calculates the current using the formula 
𝐼
=
𝑉
/
𝑅
I=V/R, based on the voltage and resistance values provided by the user.

Error Handling:

It checks if the user inputs valid numeric values for voltage and resistance.
Prevents division by zero if the resistance entered is zero (since division by zero is undefined in mathematics).
User Interaction:

The program provides clear prompts to the user for input, ensuring ease of use.
It also gives a friendly error message in case of invalid input or mathematical errors (like zero resistance).
Extendability: The code is modular, meaning it can be easily modified or expanded to handle additional electrical calculations, such as calculating voltage or resistance if the other parameters are provided.

Interactive: The calculator operates in the command-line interface (CLI), making it accessible on any machine without the need for a graphical user interface (GUI).

Target Audience:
Students: Those learning basic principles of electrical circuits and Ohm’s Law in physics or electrical engineering courses.
Professionals: Electrical engineers or technicians who need quick and easy calculations for basic circuit design or troubleshooting.
Hobbyists: Individuals working on electrical projects or experiments who need a simple tool for electric current calculation.
Technology Stack:
Programming Language: Python
Libraries:
Standard Python libraries (no external dependencies)
IDE: Any Python-supported IDE (e.g., VS Code, PyCharm) or text editor (e.g., Sublime Text, Notepad++)
Inputs:
Voltage (V): The electric potential difference in the circuit, entered by the user in volts (V).
Resistance (R): The opposition to the flow of electric current in the circuit, entered by the user in ohms (Ω).
Outputs:
Current (I): The result of the calculation, which is the electric current (in amperes, A), displayed to the user.
Error Messages: If invalid data (non-numeric or zero resistance) is entered, the program provides an appropriate error message.
Program Flow:
Start: Display an introduction to the user about the calculator and the formula used (Ohm's Law).
Input: Prompt the user to enter the voltage and resistance values.
Validation: Check that the inputs are valid numbers and handle any edge cases like zero resistance.
Calculation: Apply the Ohm's Law formula to compute the current.
Output: Display the calculated current to the user or an error message if something goes wrong.
End: Allow the user to exit or restart the program.
