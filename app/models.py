class News:
    '''
    News Class to define News Objects
    '''

    def __init__ (self, author,title, description,url,image, date):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.image = image

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
