from API.Services.databaseContext import *
from API.Models.Tag import Tag

class TagDataAccess:
    def new_tag(self, newTag: Tag):
        session = Session()
        try:
            session.add(newTag)
            session.commit()
            return session.query(Tag).filter_by(name=newTag.name).first()
        except Exception as e:
            print(e)
            return False
        finally: session.close()

    def tag_exists_by_id(self, tagId):
        session = Session()
        try:
            tag = session.query(Tag).filter_by(id=tagId).first()
            if tag is None:
                return False
            return True
        except Exception as e:
            print(e)
            return False
        finally:
            session.close()

    def get_tag_by_id(self, tagId):
        session = Session()
        try:
            return session.query(Tag).filter_by(id=tagId).first()
        except Exception as e:
            print(e)
            return None
        finally:
            session.close()

    def get_tag_by_name(self, tagName):
        session = Session()
        try:
            return session.query(Tag).filter_by(name=tagName).first()
        except Exception as e:
            print(e)
            return None
        finally:
            session.close()

    def get_all_tags(self):
        session = Session()
        try:
            return session.query(Tag).all()
        except Exception as e:
            print(e)
            return None
        finally:
            session.close()