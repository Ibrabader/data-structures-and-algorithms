from stack_queue_animal_shelter import AnimalShelter, Cat, Dog

def test_dog():
  ass = AnimalShelter()
  one = Dog("1")
  two = Dog("2")
  three = Dog("3")
  ass.enqueue(one)
  ass.enqueue(two)
  ass.enqueue(three)
  assert ass.dog == ['1','2','3']
  ass.dequeue("dog")
  assert ass.dog == ['1','2']

def test_cat():
  ass = AnimalShelter()
  one = Cat("1")
  two = Cat("2")
  three = Cat("3")
  ass.enqueue(one)
  ass.enqueue(two)
  ass.enqueue(three)
  assert ass.cat == ['1','2','3']

