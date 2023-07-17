import tkinter as tk
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
window = tk.Tk()
window.title("Power of Iota Calculator")
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
window.mainloop()