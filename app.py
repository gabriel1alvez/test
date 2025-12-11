class Man:
	def __init__(self, name: str, age: int, height: float, occupation: str):
		self.name = name
		self.age = age
		self.height = height
		self.occupation = occupation

	def __str__(self):
		return f"Man(name={self.name}, age={self.age}, height={self.height}, occupation={self.occupation})"


if __name__ == "__main__":
	# Example usage
	m = Man("John", 30, 1.8, "Engineer")
	print(m)
	print(f"Name: {m.name}, Age: {m.age}, Height: {m.height}m, Occupation: {m.occupation}")

