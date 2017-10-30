import abc

@abc.abstractproperty
class AbstractView:

    def print_error_message(self, error_msg:str):
        print('\033[91m' + error_msg + '\033[0m')

    @abc.abstractmethod
    def print_view_info(self):
        ...

    def get_user_input(self, msg):

        return input(msg)

    @abc.abstractmethod
    def print_result_output(self):
        ...

class RootView(AbstractView):

    def print_view_info(self):
        ...

    def print_result_output(self):
        ...


class AddTodoItemView(AbstractView):

    def print_view_info(self):
        ...

    def get_user_input(self):
        ...

    def print_result_output(self):
        ...


class ModifyItemView(AbstractView):

    def print_view_info(self):
        ...

    def get_user_input(self):
        ...

    def print_result_output(self):
        ...


class DeleteItemView(AbstractView):

    def print_view_info(self):
        ...

    def get_user_input(self):
        ...

    def print_result_output(self):
        ...

class MarkItemAsDoneView(AbstractView):

    def print_view_info(self):
        ...

    def get_user_input(self):
        ...

    def print_result_output(self):
        ...

class DisplayItemListView(AbstractView):

    def print_view_info(self):
        ...


    def print_result_output(self):
        ...

class DisplaySpecificItemView(AbstractView):

    def print_view_info(self):
        ...

    def get_user_input(self):
        ...

    def print_result_output(self):
        ...