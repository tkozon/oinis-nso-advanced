class DataStorage:
    def __init__(self, name: str, data: dict):
        self.name = name
        self.data = data

    def __repr__(self):
        return f"DataStorage(name={self.name}, data={self.data})"

    # You can add other methods to work with the data
    def add_entry(self, key: str, value: any):
        self.data[key] = value

    def get_entry(self, key: str):
        return self.data.get(key, None)

# Example usage
storage = DataStorage(name="Sample Data", data={"key1": "value1", "key2": "value2"})

# Displaying the object using __repr__
print(storage)

# Adding an entry
storage.add_entry("key3", "value3")

# Accessing the object data
print(storage.get_entry("key1"))

# Display updated object
print(storage)
