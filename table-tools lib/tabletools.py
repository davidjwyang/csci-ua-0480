# tabletools.py
class LabeledList:
	def __init__(self, data = None, index = None):
		self.values = data
		self.index = index 
		if index == None:
			self.index = list(range( len(data)-1 ))
	
	def __str__(self):
		output = "";
		pairs = zip(self.index, self.values)
		for i,value in pairs:
			output += f'{i:>5}{value:>20}\n'
		return output;

	__repr__ = __str__		

	def __getitem__(self, key_list):
		if (isinstance(key_list, LabeledList)):
			key_list = key_list.values
		if (isinstance(key_list, list)):
			if all(isinstance(n, bool) for n in lst):
				return getBoolList(key_list)
			else:
				return getList(key_list)
		else:
			return getItem(key_list)

	def getBoolList(self, key_list):
		v_index = []
		values = []
		for i, key in enumerate(key_list):
			if key == True:
				v_index.append(self.index[i])
				values.append(self.values[i])
		return LabeledList(values, v_index)

	def getList(self, key_list):
		intIndex = []
		v_index = []
		for key in key_list:
			for i,index in enumerate(self.index):
				if index == key:
					intIndex.append(i)
					v_index.append(key)
		values = []
		for i in intIndex: 
			values.append(self.values[i])
		return LabeledList(values, v_index)

	def getItem(self, key_list):
		intIndex = []
		for i,index in enumerate(self.index):
			if index == key_list:
				intIndex.append(i)
		if len(intIndex) == 1:
			return self.values[intIndex.pop()];
		else:
			v_index = []
			values = []
			for i in intIndex: 
				values.append(self.values[i])
				v_index.append(key_list)
			return LabeledList(values, v_index)

	def __setitem__(self, key, value):
		intIndex = []
		for i, index in enumerate(self.index):
			if index == key:
				intIndex.append(i)
		for i in intIndex:
			self.data[i] = value

	def __iter__(self):
		return iter(self.values)

	def __eq__(self, scalar):
		is_eq = [ True if value==scalar else False for value in self.values ]
		return LabeledList(is_eq, self.index)

	def __ne__(self, scalar):
		is_ne = [ True if value!=scalar else False for value in self.values ]
		return LabeledList(is_ne, self.index)

	def __gt__(self, scalar):
		is_gt = [ True if value>scalar else False for value in self.values]
		return LabeledList(is_gt, self.index)

	def __lt__(self, scalar):
		is_lt = [ True if value<scalar else False for value in self.values]
		return LabeledList(is_lt, self.index)

	def map(self, f):
		values = [ f(value) for value in self.values ] 
		index = self.index.copy()
		return LabeledList(values, index)

class Table:
	def __init__(self, data, index = None, columns = None):
		self.values = data
		#Labels of axis-0
		self.index = index 
		#Labels of axis-1
		self.columns = columns 

		if self.index == None:
			self.index = list(range( len(self.values) ))
		if self.columns == None:
			self.columns = list(range( len(self.values[1]) ))

	def getColumnSpacing(self):
		space = []
		for c in self.columns:
			space.append(len(c)+2)
		for i,value in enumerate(self.values):
			for j,v in enumerate(value):
				if isinstance(v,str):
					space[j] = len(v)+2 if len(v)+2 > space[j] else space[j]
		return space

	def __str__(self):
		space = self.getColumnSpacing()
		output = '{:>4s}'.format("")
		for i,c in enumerate(self.columns):
			output += f'{c:>{space[i]}}'
		output += '\n'	
		pairs = zip(self.index, self.values)
		for j,values in pairs:
			output += f'{j:>4d}'
			for k,v in enumerate(values):
				if isinstance(v,float):
					output += f'{v:>{space[k]}}'
				else:
					output += f'{v:>{space[k]}}'
			output += '\n'
		return output

	__repr__ = __str__

	def __getitem__(self, col_list):
		if (isinstance(col_list, LabeledList)):
			col_list = tuple(col_list.values)
		if (isinstance(col_list, tuple) or isinstance(col_list,list)):
			if all(isinstance(n, bool) for n in col_list):
				return self.getBoolTable(col_list)
			else:
				return self.getTable(col_list)
		else:
			return self.getList(col_list)

	def getBoolTable(self, col_list):
		v_index = []
		values = []
		for i, key in enumerate(col_list):
			if key == True:
				v_index.append(self.index[i])
				values.append(self.values[i])
		columns = self.columns.copy()
		return Table(values, v_index, columns)
	
	def sliceCols(self, matrix, start, end=None):
		if end==None:
			end = len(matrix)
		slice = [None]*len(matrix)
		slice = [ [] for x in slice ]
		for i in range(len(matrix)):
			for j in range(start,end):
				slice[i].append(matrix[i][j])
		return slice

	def getTable(self, col_list):
		#Initilize empty array with len(self.values) entries.
		filtered_vals = [None]*len(self.values)
		filtered_vals = [ [] for val in filtered_vals]
		v_columns = []
		for key in col_list:
			for i,col in enumerate(self.columns):
				if col == key:
					for j,entry in enumerate(self.sliceCols(self.values,i,i+1)):
						filtered_vals[j].append(entry[0])
					v_columns.append(key)
		return Table(filtered_vals, None, v_columns)

	def getList(self, col_list):
		filtered_vals = [None]*len(self.values)
		filtered_vals = [ [] for value in filtered_vals ]
		v_columns = []
		for i,col in enumerate(self.columns):
			if col == col_list:
				for j,entry in enumerate(self.sliceCols(self.values,i,i+1)):
					filtered_vals[j].append(entry[0])
				v_columns.append(col_list)
		if len(filtered_vals[1]) == 1:
			filtered_vals = self.sliceCols(filtered_vals,0,1)
			filtered_vals = [val[0] for val in filtered_vals]	
			return LabeledList(filtered_vals, self.index);
		else:
			return Table(filtered_vals, self.index, v_columns)	

	def __eq__(self, other):
		f = lambda values : [ True if value==other else False for value in values]
		is_eq = [ f(row) for row in self.values ]
		return Table(is_eq, self.index, self.columns)

	def __ne__(self, other):
		f = lambda values : [ True if value==other else False for value in values]
		is_eq = [ f(row) for row in self.values ]
		return Table(is_eq, self.index, self.columns)

	def head(self, n):
		return Table(self.values[:n], self.index[:n], self.columns)

	def tail(self, n):
		return Table(self.values[-n:], self.index[-n:], self.columns)

	def shape(self):
		return (len(self.values),len(self.values[1]))

def read_csv(fn):
	with open(fn) as file:
		data = file.read()
	data = data.replace("\n", "\r\n")
	data = data.split("\r\n")
	table_data = [ [value.strip() for value in row.split(",")] for row in data ]
	if table_data[len(table_data)-1] == ['']:
		del table_data[len(table_data)-1]
	column = table_data[0]
	values = table_data[1:]
	#make it per element
	for i,row in enumerate(values):
		for j,value in enumerate(row):
			try: 
				values[i][j] = float(value)
			except ValueError:
				None
	return Table(values,None,column)

	# with open(fn) as file:
	# 	data = [",".split(line) for line in file]
	# 	table_data = [ [value.strip() for value in row] for row in data ]
	# 	column = table_data[0]
	# 	values = table_data[1:]
	# 	try: 
	# 		values = [ [float(value) for value in row] for row in values ]
	# 	except ValueError:
	# 		None
	# 	return Table(values,None,column)
		


if __name__ == '__main__':
	import tabletools as tt
	candy_table = tt.read_csv('candy-data.csv')
	print(candy_table.tail(4))

	table = candy_table[candy_table['chocolate'] == 1.0]['competitorname', 'chocolate', 'peanutyalmondy', 'winpercent']
	print(table)

	isPeanutyAlmondy = [ True if x==1.0 else False for x in table['peanutyalmondy'] ] 
	table = table[isPeanutyAlmondy]
	print(table)

	lost = [ True if x<.50 else False for x in table['winpercent'] ]
	print(table[lost])

	f = lambda string: True if string[:5]=="Reese" else False
	reese = [f(x) for x in table['competitorname'] ]
	print(table[reese])

	f = lambda string: True if len(string)<10 else False
	lessThan10 = [ f(x) for x in table['competitorname'] ]
	print(table[lessThan10])




