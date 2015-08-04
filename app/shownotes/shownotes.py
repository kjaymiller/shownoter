from datetime import date

class Shownotes:
    """ceates shownotes object to be saved in database"""
    def __init__(self, title):
    self.title = title
    self.created = date.today()
    self.description = description
    self.links = links
    
    def add_link(self, links):
        """adds a link to self.links"""
        pass
        
    def remove_link(self, links):
        """removes a link from self.links"""
        pass
        
    def reset_links(self):
        """removes all links in self.links""" 
        pass
        
        