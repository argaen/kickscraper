DEFAULT_BACKEND = 'backends.kickstarter'


class Project:

    def __init__(self, uid, backend=None):
        self.uid = uid
        self.connector = backend or DEFAULT_BACKEND

    def get_title():
        pass

    def get_author():
        pass
