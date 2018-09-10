"""
Contains custom widgets for input for budget v4.
Currently contains:
- Entry for dates
"""
import tkinter as tk
from datetime import date


class DateEntry(tk.Frame):
	"""
	Allows the user to enter a date
	"""
	def __init__(self, parent):
		tk.Frame.__init__(self, parent)

		# create variables for tracking entry
		self.day = tk.StringVar(self)
		self.month = tk.StringVar(self)
		self.year = tk.StringVar(self)

		# create entry boxes
		day_box = tk.Entry(self, textvariable=self.day)
		month_box = tk.Entry(self, textvariable=self.month)
		year_box = tk.Entry(self, textvariable=self.year)

		# trace variables to limit chars
		self.day.trace('w', lambda *args :DateEntry.limit_entry(self.day))
		self.month.trace('w', lambda *args :DateEntry.limit_entry(self.month))
		self.year.trace('w', lambda *args :DateEntry.limit_entry(self.year, limit=4))

		# pack
		day_box.grid()
		month_box.grid(row=0, column=1)
		year_box.grid(row=0, column=2)


	def limit_entry(var, limit=2):
		"""
		Used to limit entry boxes to a certain length
		limit defaults to 2
		"""
		var.set(var.get()[:limit])



root = tk.Tk()
date = DateEntry(root)
date.pack()

root.mainloop()
