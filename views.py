import abc


class AbstractView:
    def print_error_message(self, error_msg:str):
        print('\033[91m' + error_msg + '\033[0m')

    @abc.abstractmethod
    def print_view_info(self):
        ...

    @abc.abstractmethod
    def call_get_user_input_event(self):
        ...

    @abc.abstractmethod
    def print_result_output(self):
        ...

class RootView(AbstractView):
    menu_option_list = ['Add ToDo item', 'Modify item', 'Delete Item', 'Mark item as done', "Display item's list",
                        "Display specific todo item's details", 'Exit']

    def print_view_info(self):
        for index, option in enumerate(self.menu_option_list):
            print(str(index +1) + '. ' + option)

    def call_get_user_input_event(self):
        from controllers import Controller
        self.print_view_info()
        controller = Controller.get_instance()
        controller.root_view_listener(input("\n Type a number of option: "))

class AddTodoItemView(AbstractView):

    def print_view_info(self):
        print('Here you can add new TODO task.')

    def call_get_user_input_event(self):
        from controllers import Controller
        self.print_view_info()
        controller = Controller.get_instance()
        print('Type info about item in following syntax <name:str,description:str,is done:bool>')
        user_input = input("\ni.e buy vegetables,tommorow go to shop,false: ")
        controller.add_todo_item_view_listener(user_input)

    def print_result_output(self, task_name:str, task_description:str, is_done:bool):
        print('New item have been added successfully !')
        print('Task name: %s' % task_name)
        print('Task description: %s' % task_description)
        print('Task status: %s' % 'done' if is_done else 'undone')


class ModifyItemView(AbstractView):

    def print_view_info(self,):
        print('Here you can modify already added tasks!.')

    def call_get_user_input_event(self):
        self.print_view_info()
        from controllers import Controller
        print('If you want to change the name type: name,index,<new_name>')
        print('If you want to change the desc type: desc,index,<new_desc>')
        user_input = input('Your choice: ')
        controller = Controller.get_instance()
        controller.add_modify_item_view_listener(user_input)

    def print_result_output(self):
        print('The TODO item information have been updated successfully!')


class DeleteItemView(AbstractView):

    def print_view_info(self):
        print('Here you can delete already added tasks!.')

    def call_get_user_input_event(self,):
        from controllers import Controller
        user_input = input('Index of item to be deleted: ')
        controller = Controller.get_instance()
        controller.delete_item_view_listener(user_input)

    def print_result_output(self, item_name:str):
        print('Item with name %s have been deleted successfully !' % item_name)

class MarkItemAsDoneView(AbstractView):

    def print_view_info(self):
        print('Here you can mark as done already added tasks!.')

    def call_get_user_input_event(self,):
        from controllers import Controller
        user_input = input('Index of item to be marked as done: ')
        controller = Controller.get_instance()
        controller.delete_item_view_listener(user_input)

    def print_result_output(self, item_name:str):
        print('Item with name %s have been marked as done successfully !' % item_name)

class DisplayItemListView(AbstractView):

    def print_view_info(self, tasks_list:[]):
        print('List of added tasks:')
        for index, task in enumerate(tasks_list):
            task_name = task.get_name()
            print('%d. Name: %s,  Status: %s' % (index, task_name))

class DisplaySpecificItemView(AbstractView):

    def print_view_info(self):
        print('Here you can display information about TODO item with details!.')

    def call_get_user_input_event(self):
        from controllers import Controller
        user_input = input('Index of item to be marked as done: ')
        controller = Controller.get_instance()
        controller.delete_item_view_listener(user_input)

    def print_result_output(self, task_name:str, task_description:str, is_done:bool):
        print('Task name: %s' % task_name)
        print('Task description: %s' % task_description)
        print('Task status: %s' % 'done' if is_done else 'undone')