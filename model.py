import os, pickle

class ToDoItem:

    todo_items_list = []

    def __init__(self, name:str, description:str, is_done:bool = False):
        ToDoItem.load_todo_items_from_file()
        ToDoItem.raise_exception_if_item_with_such_name_exists(name)
        self.set_name(name)
        self.set_description(description)
        self.set_is_done(is_done)
        ToDoItem.todo_items_list.append(self)
        ToDoItem.save_todo_items_to_file()

    @staticmethod
    def raise_exception_if_item_with_such_name_exists(name:str):
        ToDoItem.load_todo_items_from_file()
        for todo_item in ToDoItem.todo_items_list:
            if todo_item.get_name().lower() == name.lower():
                raise Exception('Such TodoItem exists !')

    def set_name(self, name:str):

        if not isinstance(name, str): raise Exception('Name should be string !')
        if len(name) > 20: raise Exception('Name should contain max 20 chars!')
        self._name = name

    def get_name(self):

        return self._name

    def set_description(self, description:str):
        if not isinstance(description, str): raise Exception('Description should be string !')
        if len(description) > 150: raise Exception('Description should contain max 150 chars!')
        self._description = description

    def get_description(self):

        return self._description

    def set_is_done(self, is_done:bool = False):

        self._is_done = is_done

    def get_is_done(self):

        return self._is_done

    @staticmethod
    def remove_todo_item(todo_item):
        ToDoItem.load_todo_items_from_file()
        if ToDoItem.todo_items_list.__contains__(todo_item):
            ToDoItem.todo_items_list.remove(todo_item)
        else:
            return None

    @staticmethod
    def get_todo_items_list():
        ToDoItem.load_todo_items_from_file()
        if not ToDoItem.todo_items_list: raise Exception('List of Todo items is empty !')
        return ToDoItem.todo_items_list

    @staticmethod
    def get_item_by_id(id:int):
        ToDoItem.load_todo_items_from_file()
        return ToDoItem.todo_items_list

    @staticmethod
    def save_todo_items_to_file():
        if not ToDoItem.todo_items_list: return #if todoitems instance list is empty it does not save it to file
        with open('todoitems.data', 'wb') as output:
            pickle.dump(ToDoItem.todo_items_list, output, pickle.HIGHEST_PROTOCOL) #saves object to file

    @staticmethod
    def load_todo_items_from_file():
        if not os.path.exists('todoitems.data') or os.stat('todoitems.data').st_size == 0:
            return  # checks if the data file exists, if not it does not load it
        if ToDoItem.todo_items_list: return #checks if the list have been loaded before if so it does not load again
        with open('todoitems.data', 'rb') as input:
            ToDoItem.todo_items_list = pickle.load(input) #load object from file