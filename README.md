# Power of Iota Calculator

This is a simple Python script that calculates the power of iota (i) based on user input using a graphical user interface (GUI) built with the Tkinter library.

## How to Use

1. Make sure you have Python installed on your system.
2. Open a terminal or command prompt.
3. Navigate to the directory where the script is located.
4. Run the script using the following command:
   ```
   python main.py
   ```
5. A GUI window titled "Power of Iota Calculator" will appear.
6. Enter the desired power of iota (i) in the input field.
7. Click the "Calculate" button to see the calculated result displayed below.
8. The result will be shown in the format "i^x = y", where "x" is the user input and "y" is the calculated value.

## Code Explanation

The code uses the Tkinter library to create a GUI window. Here's a breakdown of the main components of the code:

- Importing the necessary libraries:
   ```python
   import tkinter as tk
   ```

- Defining the calculation function `calculate_iota()`:
   ```python
   def calculate_iota():
       user_number_input = int(entry.get())
       result = ""

       if user_number_input % 4 == 0:
           result = "1"
       elif user_number_input % 4 == 1:
           result = "\u221A-1 or i"
       elif user_number_input % 4 == 2:
           result = "-1"
       elif user_number_input % 4 == 3:
           result = "-\u221A1 or -i"

       result_label.configure(text="i^{} = {}".format(user_number_input, result))
   ```

- Creating the main window:
   ```python
   window = tk.Tk()
   window.title("Power of Iota Calculator")
   ```

- Adding labels, input fields, and buttons to the window:
   ```python
   label = tk.Label(window, text="Power of Iota Calculator")
   label.pack(pady=10)

   input_frame = tk.Frame(window)
   input_frame.pack()

   input_label = tk.Label(input_frame, text="Enter the power of iota(i):")
   input_label.pack(side="left")

   entry = tk.Entry(input_frame)
   entry.pack(side="left")

   calculate_button = tk.Button(window, text="Calculate", command=calculate_iota)
   calculate_button.pack(pady=10)

   result_label = tk.Label(window, text="")
   result_label.pack()
   ```

- Running the main event loop:
   ```python
   window.mainloop()
   ```

Feel free to customize and modify the code to fit your needs.