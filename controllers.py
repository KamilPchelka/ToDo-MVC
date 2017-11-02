from views import *
import views
from model import ToDoItem

class Controller():
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
        if cls.INSTANCE is None:
            cls.INSTANCE = Controller()
        return cls.INSTANCE


    def start(self):
        while True:
            os.system('clear')
            self.root_view.call_get_user_input_event()

    def root_view_listener(self, input:str):
        if input not in [str(number) for number in range(1, len(views.MENU_OPTION_LIST) +1)]:
            self.root_view.print_error_message('Bad number of option !')
        elif input == '1':
            self.add_todo_item_view.call_get_user_input_event()
        elif input == '2':
            self.modify_item_view.call_get_user_input_event()
        elif input == '3':
            self.delete_item_view.call_get_user_input_event()
        elif input == '4':
            self.mark_item_as_done_view.call_get_user_input_event()
        elif input == '5':
            self.display_item_list_view.print_result_output(ToDoItem.get_todo_items_list())
        elif input == '6':
            self.display_specyfic_item_view.call_get_user_input_event()
        elif input == '7':
            self.root_view.exit_program('Thank you for using the program !')

    def add_todo_item_view_listener(self, user_input:str):
        try:
            splitted_user_input = user_input.split(',')
            print(splitted_user_input)
            task_name = splitted_user_input[0]
            task_desc = splitted_user_input[1]
            task_status = True if splitted_user_input[2].lower() == 'true' else False
            ToDoItem(task_name, task_desc, task_status)
            self.add_todo_item_view.print_result_output(task_name, task_desc, task_status)
        except IndexError:
            self.add_todo_item_view.print_error_message('Please type required arguments in correct type and order !')
        except Exception as e:
            self.add_todo_item_view.print_error_message(str(e))


