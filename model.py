import os, pickle

class ToDoItem:
    """Model class"""

    todo_items_list = [] #list of all ToDoItem instances

    def __init__(self, name:str, description:str, is_done:bool = False):
        """
        Constructor of ToDoItem
        :param name: str -> name of task
        :param description: str -> description of task
        :param is_done: bool -> status of task true equals to done and false to undone
        """
        ToDoItem.load_todo_items_from_file()
        ToDoItem.raise_exception_if_item_with_such_name_exists(name)
        self.set_name(name)
        self.set_description(description)
        self.set_is_done(is_done)
        ToDoItem.todo_items_list.append(self)
        ToDoItem.save_todo_items_to_file()

    @staticmethod
    def raise_exception_if_item_with_such_name_exists(name:str):
        """
        Function checks if there is a todo task with given name
        :param name: str -> name of task that may already exist
        :return: None
        """
        ToDoItem.load_todo_items_from_file()
        for todo_item in ToDoItem.todo_items_list:
            if todo_item.get_name().lower() == name.lower():
                raise Exception('Such TodoItem exists !')

    def set_name(self, name:str):
        """
        Setter of _name attribute
        :param name: str -> name of task
        :return: None
        """
        if not isinstance(name, str): raise Exception('Name should be string !')
        if len(name) > 20: raise Exception('Name should contain max 20 chars!')
        self._name = name

    def get_name(self):
        """
        Getter of _name attribute
        :return: str -> _name attribute
        """
        return self._name

    def set_description(self, description:str):
        """
        Setter of _description attribute
        :param description: str -> description of task
        :return: None
        """
        if not isinstance(description, str): raise Exception('Description should be string !')
        if len(description) > 150: raise Exception('Description should contain max 150 chars!')
        self._description = description

    def get_description(self):
        """
        Getter of _description attribute
        :return: _description: str -> description of task
        """
        return self._description

    def set_is_done(self, is_done:bool = False):
        """
        Setter of _is_done attribute
        :param is_done: bool -> status of task, by default False
        :return: None
        """
        self._is_done = is_done

    def get_is_done(self):
        """
        Getter of _is_done attribute
        :return: _is_done: bool -> status of task, by default False
        """
        return self._is_done

    @staticmethod
    def remove_todo_item(todo_item):
        """
        Remove ToDoItem from todo_items_list
        :param todo_item: ToDoItem -> ToDoItem instance to be removed
        :return: None
        """
        ToDoItem.load_todo_items_from_file()
        if ToDoItem.todo_items_list.__contains__(todo_item):
            ToDoItem.todo_items_list.remove(todo_item)
        else:
            raise Exception('Such item does not exist !')
        ToDoItem.save_todo_items_to_file()

    @staticmethod
    def get_todo_items_list():
        """
        Getter of todo_items_list
        :return:
        """
        ToDoItem.load_todo_items_from_file()
        #if not ToDoItem.todo_items_list: raise Exception('List of Todo items is empty !')
        return ToDoItem.todo_items_list

    @staticmethod
    def save_todo_items_to_file():
        """
        Method saves todo_items_list list to file as binary object
        :return: None
        """
        with open('todoitems.data', 'wb') as output:
            pickle.dump(ToDoItem.todo_items_list, output, pickle.HIGHEST_PROTOCOL) #saves object to file

    @staticmethod
    def load_todo_items_from_file():
        """
        Method loads todo_items_list list from file
        :return: None
        """
        if not os.path.exists('todoitems.data') or os.stat('todoitems.data').st_size == 0:
            return  # checks if the data file exists, if not it does not load it
        if ToDoItem.todo_items_list: return #checks if the list have been loaded before if so it does not load again
        with open('todoitems.data', 'rb') as input:
            ToDoItem.todo_items_list = pickle.load(input) #load object from file