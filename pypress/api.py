import os


class Template():
    def __init__(self, template_name: str):
        """Access the template using other functions by adding the name here"""
        self.tmp = 'pypress/'+template_name

    def create(self):
        """Creates and returnes edit access to the template"""
        return open(self.tmp, 'r+')

    def edit(self):
        """Grants edit access to an already existing template"""
        if os.path.isfile(self.tmp):
            return open(self.tmp, 'r+')
        raise FileNotFoundError

    def delete(self):
        """Deletes the template""""
        os.remove('template')
