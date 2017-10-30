class ToDoItem:

    _todo_items_list = []

    def __init__(self, name:str, description:str, is_done:bool = False):
        self.set_name(name)
        self.set_description(description)
        self.set_is_done()
        ToDoItem._todo_items_list.append(self)
        ...


    def set_name(self, name:str):

        return self._name

    def get_name(self):
        ...

    def set_description(self, name:str):
        ...

    def get_desciption(self):

        return self._description

    def set_is_done(self, is_done:bool = False):

        self._is_done = is_done

    def get_is_done(self):

        self._is_done

    @staticmethod
    def remove_todo_item(todo_item):
        ...

    @staticmethod
    def get_todo_items_list():
        ...

    @staticmethod
    def _save_todo_items_to_file():
        ...

    @staticmethod
    def _load_todo_items_from_file():
        ...