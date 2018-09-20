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

		# register validation command
		id = parent.register(self.validate_entry)

		# create entry boxes
		self.day = tk.Entry(self, width=3, justify='center', validate='key', validatecommand=(id, '%P', 2))
		self.month = tk.Entry(self, width=3, justify='center', validate='key', validatecommand=(id, '%P', 2))
		self.year = tk.Entry(self, width=5, justify='center', validate='key', validatecommand=(id, '%P', 4))

		# create today button
		if today_button:
			self.today = tk.Button(self, text='Today', command=self.set_to_today)
			self.today.grid(row=0, column=5)

		# pack
		self.day.grid()
		tk.Label(self, text='.').grid(row=0, column=1)
		self.month.grid(row=0, column=2)
		tk.Label(self, text='.').grid(row=0, column=3)
		self.year.grid(row=0, column=4)


	def validate_entry(self, P, limit):
		"""
		Checks entered character is a number, and that entry is less
		than limit length
		"""
		# check for length
		if len(P) > int(limit):
			return False
		elif len(P) == 0:
			return True

		# check for type
		try:
			int(P)
			return True
		except ValueError:
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


root = tk.Tk()
date = DateEntry(root)
date.pack()

# button to test retrieval
test = tk.Button(root, text='Get Date', command=date.get_date)
test.pack()


root.mainloop()
