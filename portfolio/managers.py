from django.db.models import Manager


class PublicManager(Manager):
    """Returns only public projects."""
    
    def public(self):
        return self.get_query_set().filter(is_public=True)