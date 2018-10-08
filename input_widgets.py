"""
Contains custom widgets for input for budget v4.
Currently contains:
- Entry for dates
"""
import tkinter as tk
import datetime


class DateEntry(tk.Frame):
	"""
	Allows the user to enter a date
	"""
	def __init__(self, parent, today_button=True):
		tk.Frame.__init__(self, parent)
		self.parent = parent

		# register validation command
		id = self.parent.register(self.validate_date_entry)

		# create entry boxes
		self.day = tk.Entry(self, width=3, justify='center', validate='key', validatecommand=(id, '%P', 2, 31))
		self.month = tk.Entry(self, width=3, justify='center', validate='key', validatecommand=(id, '%P', 2, 12))
		self.year = tk.Entry(self, width=5, justify='center', validate='key', validatecommand=(id, '%P', 4, float('inf')))

		# create today button
		if today_button:
			self.today = tk.Button(self, text='Today', command=self.set_to_today)
			self.today.grid(row=0, column=5)

		# pack
		self.day.grid(row=0, column=0)
		tk.Label(self, text='.').grid(row=0, column=1)
		self.month.grid(row=0, column=2)
		tk.Label(self, text='.').grid(row=0, column=3)
		self.year.grid(row=0, column=4)


	def validate_date_entry(self, P, limit, top_value):
		"""
		Checks entered character is a number, and that entry is less
		than limit length and the top value
		"""
		# check for length
		if len(P) > int(limit):
			return False
		elif len(P) == 0:
			return True

		# check for type
		try:
			value = int(P)
		except ValueError:
			return False

		# check the entered number isn't higher than top_value
		if value <= int(top_value):
			return True
		else:
			return False


	def set_to_today(self):
		"""
		Changes the entry boxes to show today's date
		"""
		# setup variables
		boxes = [self.day, self.month, self.year]
		contents = datetime.date.today().strftime('%d %m %Y').split()
		# dynamically clear and enter contents
		for i in range(3):
			boxes[i].delete(0, 'end')
			boxes[i].insert(0, contents[i])


	def get_date(self):
		"""
		Retrieves date from entry boxes
		Returns tuple (True/False, datetime object/error message)
		"""
		try:
			date = datetime.date(year=int(self.year.get()),
								 month=int(self.month.get()),
								 day=int(self.day.get()))
			return True, date
		except ValueError as err:
			return False, err


class AmtEntry(tk.Frame):
	"""
	Custom widget for entering an amount of money
	"""
	def __init__(self, parent):
		tk.Frame.__init__(self, parent)
		self.parent = parent

		# create entry boxes
		self.pounds = tk.Entry(self)
		self.pence = tk.Entry(self)

		# grid
		tk.Label(self, text='£').grid(row=0, column=0)
		self.pounds.grid(row=0, column=1)
		tk.Label(self, text='.').grid(row=0, column=2)
		self.pence.grid(row=0, column=3)


# TESTING
if __name__ == "__main__":
	root = tk.Tk()

	test = AmtEntry(root)
	test.pack()

	root.mainloop()
