from API.DataAccess.TagDataAccess import TagDataAccess
from API.Models.Tag import Tag

class TagsUseCase:
    def __init__(self):
        self.dataAccess = TagDataAccess()

    def add_new_tag(self, tagName):
        if self.dataAccess.get_tag_by_name(tagName):
            return False, 'Tag already exists'

        tag = self.dataAccess.new_tag(Tag(tagName))
        if not tag:
            return False, 'Failed to create tag'
        return True, tag

    def get_all_tags(self):
        tags = self.dataAccess.get_all_tags()
        if tags is None:
            return False, 'Unable to get tags'
        return True, tags