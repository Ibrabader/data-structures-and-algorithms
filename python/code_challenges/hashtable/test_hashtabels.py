import bytest
from hashtable import HashTable

def test_hash_function():
  hash_table = HashTable()
  assert hash_table.add('hello') == 523
  
def test_add_item():
  hash_table = HashTable()
  hash_table.add('hello',15)
  assert len(hash_table.arr[hash_table.get_hash('hello')]) == 1
  
def test_get_item():
  hash_table = HashTable()
  hash_table.add('hello',15)
  assert hash_table.get('hello') == 15

def test_contains_item():
  hash_table = HashTable()
  hash_table.add('hello',15)
  assert hash_table.contains('hello')

