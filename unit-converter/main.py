from tkinter import *

def miles_to_km():
    miles = miles_input.get()
    km = float(miles) * 1.609
    km_result_label.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=50, pady=50)

#Entry
miles_input = Entry(width=10)
print(miles_input.get())
miles_input.grid(column=1, row=0)

#Label
is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)


#Button
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)



# There is pack, place and grid for widget layout.
# Pack isn't very flexible and Place is too specific as it requires x and y coordinates.
# Grid is more useful since it takes the whole layout as rows and columns.
window.mainloop()
