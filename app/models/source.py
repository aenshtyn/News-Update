class Source:
    '''
    News Class to define News Source Objects
    '''

    def __init__ (self, id, name, description,url, category ):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.content = category
