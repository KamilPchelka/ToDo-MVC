import abc
import os

MENU_OPTION_LIST = ['Add ToDo item', 'Modify item', 'Delete Item', 'Mark item as done', "Display item's list",
                    "Display specific todo item's details", 'Exit']

CONFIRM_MESSAGE = '\nType ENTER...'

class AbstractView:
    """Abstract class for all views."""
    def print_error_message(self, error_msg:str):
        """
        Method prints error message
        :param error_msg: str -> An error message.
        :return: None
        """
        os.system('clear')
        print('\033[91m' + error_msg + '\033[0m')
        input(CONFIRM_MESSAGE)

    @abc.abstractmethod
    def call_get_user_input_event(self):
        """
        Method calls get user input event
        :return: None
        """
        ...

    @abc.abstractmethod
    def print_result_output(self):
        """
        Method prints output controller's messages.
        :return: None
        """
        ...

    def print_todo_item_info(self, task_name:str, task_description:str, is_done:bool):
        """
        Method print detailed information about ceratin ToDo task
        :param task_name: str -> name of the task
        :param task_description: str -> description of the task
        :param is_done: bool -> status of task true equals to done and false to undone
        :return: None
        """
        os.system('clear')
        print('Task name: %s' % task_name)
        print('Task description: %s' % task_description)
        is_done = 'done' if is_done else 'undone'
        print('Task status: %s' % is_done)
        input(CONFIRM_MESSAGE)

    def print_tasks_list(self, tasks_list:[]):
        print('List of added tasks:')
        for index, task in enumerate(tasks_list):
            task_name = task.get_name()
            print('%d. Name: %s' % (index, task_name))
        print()

class RootView(AbstractView):


    def print_view_info(self):
        for index, option in enumerate(MENU_OPTION_LIST):
            print(str(index +1) + '. ' + option)

    def call_get_user_input_event(self):
        from controllers import Controller
        self.print_view_info()
        controller = Controller.get_instance()
        controller.root_view_listener(input("Type a number of option: "))

    def exit_program(self, msg:str):
        os.system('clear')
        exit(msg)

class AddTodoItemView(AbstractView):

    def call_get_user_input_event(self):
        from controllers import Controller
        os.system('clear')
        controller = Controller.get_instance()
        print('Type info about item in following syntax <name:str,description:str,is done:bool>')
        user_input = input("i.e: buy vegetables,tommorow go to shop,false: ")
        controller.add_todo_item_view_listener(user_input)

    def print_result_output(self, task_name:str, task_description:str, is_done:bool):
        os.system('clear')
        print('New item have been added successfully !')
        super().print_todo_item_info(task_name, task_description, is_done)


class ModifyItemView(AbstractView):

    def call_get_user_input_event(self, tasks_list:[]):
        from controllers import Controller
        os.system('clear')
        super().print_tasks_list(tasks_list)
        print('If you want to change the name type: name,index,<new_name>')
        print('If you want to change the desc type: desc,index,<new_desc>')
        user_input = input('Your choice: ')
        controller = Controller.get_instance()
        controller.modify_item_view_listener(user_input, tasks_list)

    def print_result_output(self):
        os.system('clear')
        print('The TODO item information have been updated successfully!')
        input(CONFIRM_MESSAGE)


class DeleteItemView(AbstractView):

    def call_get_user_input_event(self, tasks_list:[]):
        from controllers import Controller
        os.system('clear')
        super().print_tasks_list(tasks_list)
        user_input = input('Index of item to be deleted: ')
        controller = Controller.get_instance()
        controller.delete_item_view_listener(user_input, tasks_list)

    def print_result_output(self, item_name:str):
        os.system('clear')
        print('Item with name %s have been deleted successfully !' % item_name)
        input(CONFIRM_MESSAGE)

class MarkItemAsDoneView(AbstractView):

    def call_get_user_input_event(self, tasks_list:[], ):
        from controllers import Controller
        os.system('clear')
        super().print_tasks_list(tasks_list)
        user_input = input('Index of item to be marked as done: ')
        controller = Controller.get_instance()
        controller.mark_item_as_done_view_listener(user_input, tasks_list)

    def print_result_output(self, item_name:str):
        os.system('clear')
        print('Item with name %s have been marked as done successfully !' % item_name)
        input(CONFIRM_MESSAGE)

class DisplayItemListView(AbstractView):

    def print_result_output(self, tasks_list:[]):
        os.system('clear')
        super().print_tasks_list(tasks_list)
        input(CONFIRM_MESSAGE)

class DisplaySpecificItemView(AbstractView):

    def call_get_user_input_event(self, tasks_list:[]):
        from controllers import Controller
        os.system('clear')
        super().print_tasks_list(tasks_list)
        user_input = input('Index of item to view deatils: ')
        controller = Controller.get_instance()
        controller.display_specyfic_item_view_listener(user_input, tasks_list)

    def print_result_output(self, task_name:str, task_description:str, is_done:bool):
        super().print_todo_item_info(task_name, task_description, is_done)