from app.persistence.repository import InMemoryRepository
from test_hbnb.part2.hbnb.app.models.user import User

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    # Placeholder method for creating a user
    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.create(user)
        return user

    # Placeholder method for fetching a place by ID
    def get_place(self, place_id):
        return self.place_repo.get(place_id)
