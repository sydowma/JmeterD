
class FormErrors(object):
    """
    """

    def __init__(self):
        """
        :param form_errors  a dict
        """

    @staticmethod
    def errors_message(form):
        return ', '.join([v for k, v in form.errors.items() for v in v])

    @staticmethod
    def errors(form):
        return form.errors.items()
