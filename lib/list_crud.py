def create_an_empty_list():
    return []

def create_a_list():
    return list(range(4))

def add_element_to_end_of_list(l, element):
    l.append(element)
    return l

def add_element_to_start_of_list(l, element):
    l.insert(0, element)
    return l

def remove_element_from_end_of_list(l):
    l.pop()
    return l

def remove_element_from_start_of_list(l):
    l.pop(0)
    return l

def retrieve_first_element_from_list(l):
    i = l.pop(0)
    return i

def retrieve_element_from_index(l, index):
    i = l.pop(index)
    return i

def retrieve_last_element_from_list(l):
    i = l.pop(len(l) -1)
    return i