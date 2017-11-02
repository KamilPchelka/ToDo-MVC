from views import *
import views
from model import ToDoItem

class Controller():
    """Singleton Controller class"""
    INSTANCE = None

    def __init__(self):
        if self.INSTANCE is not None:
            raise ValueError("An instantiation already exists!")
        self.root_view = RootView()
        self.add_todo_item_view = AddTodoItemView()
        self.modify_item_view = ModifyItemView()
        self.delete_item_view = DeleteItemView()
        self.mark_item_as_done_view = MarkItemAsDoneView()
        self.display_item_list_view = DisplayItemListView()
        self.display_specyfic_item_view = DisplaySpecificItemView()

    @classmethod
    def get_instance(cls):
        """
        Retruns the singleton instance of Controller
        :return:
        """
        if cls.INSTANCE is None:
            cls.INSTANCE = Controller()
        return cls.INSTANCE


    def start(self):
        """
        Method that runs main program loop
        :return: None
        """
        while True:
            os.system('clear')
            try:
                self.root_view.call_get_user_input_event()
            except IndexError:
                self.root_view.print_error_message(
                    'Please type required arguments in correct type and order !')
            except ValueError:
                self.root_view.print_error_message('Your input must contain only positive numbers !')
            except Exception as e:
                self.root_view.print_error_message(str(e))

    def root_view_listener(self, input:str):
        """
        Method handles and process input from root view
        :param input:
        :return:
        """
        tasks_list = ToDoItem.get_todo_items_list() #list of all avaible tasks
        if input not in [str(number) for number in range(1, len(views.MENU_OPTION_LIST) +1)]:
            self.root_view.print_error_message('Bad number of option !')
        elif input == '1':
            self.add_todo_item_view.call_get_user_input_event()
        elif input == '2':
            self.modify_item_view.call_get_user_input_event(tasks_list)
        elif input == '3':
            self.delete_item_view.call_get_user_input_event(tasks_list)
        elif input == '4':
            self.mark_item_as_done_view.call_get_user_input_event(tasks_list)
        elif input == '5':
            self.display_item_list_view.print_result_output(ToDoItem.get_todo_items_list())
        elif input == '6':
            self.display_specyfic_item_view.call_get_user_input_event(tasks_list)
        elif input == '7':
            self.root_view.exit_program('Thank you for using the program !')

    def add_todo_item_view_listener(self, user_input:str):
        """
        Method handles and process input from AddTodoItemView
        :param input: str-> user input as string
        :return:
        """
        splitted_user_input = user_input.split(',')
        task_name = splitted_user_input[0]
        task_desc = splitted_user_input[1]
        task_status = True if splitted_user_input[2].lower() == 'true' else False
        ToDoItem(task_name, task_desc, task_status)
        self.add_todo_item_view.print_result_output(task_name, task_desc, task_status)

    def modify_item_view_listener(self, user_input:str, tasks_list):
        """
        Method handles and process input from ModifyTodoItemView
        :param input: str-> user input as string
        :param tasks_list: list -> a list of all tasks
        :return:
        """
        splitted_user_input = user_input.split(',')
        cmd = splitted_user_input[0].lower() #one of the following: 'name' , 'desc' that changes TodoItem attributes
        index = int(splitted_user_input[1])
        new_value = splitted_user_input[2] # new name or new description of TodoItem
        if cmd == 'name':
            tasks_list[index].set_name(new_value)
        elif cmd == 'desc':
            tasks_list[index].set_description(new_value)
        else:
            raise Exception('Bad command !')
        self.modify_item_view.print_result_output()
        ToDoItem.save_todo_items_to_file()

    def delete_item_view_listener(self, user_input:str, tasks_list):
        """
        Method handles and process input from DeleteItemView
        :param input: str-> user input as string
        :param tasks_list: list -> a list of all tasks
        :return:
        """
        todo_item_to_be_removed = tasks_list[int(user_input)]
        ToDoItem.remove_todo_item(todo_item_to_be_removed)
        self.delete_item_view.print_result_output(todo_item_to_be_removed.get_name())

    def mark_item_as_done_view_listener(self, user_input:str, tasks_list):
        """
        Method handles and process input from MarkItemAsDoneView
        :param input: str-> user input as string
        :param tasks_list: list -> a list of all tasks
        :return:
        """
        todo_item_to_be_marked_as_done = tasks_list[int(user_input)]
        todo_item_to_be_marked_as_done.set_is_done(True)
        self.mark_item_as_done_view.print_result_output(todo_item_to_be_marked_as_done.get_name())

    def display_specyfic_item_view_listener(self, user_input:str, tasks_list):
        """
        Method handles and process input from DisplaySpecyficItemView
        :param input: str-> user input as string
        :param tasks_list: list -> a list of all tasks
        :return:
        """
        specyfic_todo_item = tasks_list[int(user_input)]
        name = specyfic_todo_item.get_name()
        desc = specyfic_todo_item.get_description()
        status = specyfic_todo_item.get_is_done()
        self.display_specyfic_item_view.print_result_output(name, desc, status)



