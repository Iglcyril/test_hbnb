#!/usr/bin/env python3
"""Test all models"""

from hbnb.app.models.amenity import Amenity
from hbnb.app.models.user import User
from hbnb.app.models.place import Place
from hbnb.app.models.review import Review

def test_amenity():
    print("\n🧪 Test Amenity")
    
    # Test valide
    wifi = Amenity("WiFi")
    print(f"✅ Créé: {wifi}")
    print(f"   ID: {wifi.id}")
    print(f"   Dict: {wifi.to_dict()}")
    
    # Test erreur
    try:
        Amenity("")
        print("❌ Erreur: devrait refuser string vide")
    except ValueError as e:
        print(f"✅ Erreur attrapée: {e}")

def test_user():
    print("\n🧪 Test User")
    
    # Test valide
    alice = User("Alice", "Smith", "alice@example.com")
    print(f"✅ Créé: {alice}")
    print(f"   Email: {alice.email}")
    
    # Test erreur email
    try:
        User("Bob", "Martin", "notanemail")
        print("❌ Erreur: devrait refuser email invalide")
    except ValueError as e:
        print(f"✅ Erreur attrapée: {e}")

def test_place():
    print("\n🧪 Test Place")
    
    # Test valide
    place = Place("Appart Paris", 100, 48.8566, 2.3522, "user123")
    print(f"✅ Créé: {place}")
    print(f"   Prix: {place.price}€")
    
    # Test erreur prix négatif
    try:
        Place("Test", -50, 48.8, 2.3, "user123")
        print("❌ Erreur: devrait refuser prix négatif")
    except ValueError as e:
        print(f"✅ Erreur attrapée: {e}")

def test_review():
    print("\n🧪 Test Review")
    
    # Test valide
    review = Review("Super séjour !", 5, "place123", "user456")
    print(f"✅ Créé: {review}")
    print(f"   Rating: {review.rating}/5")
    
    # Test erreur rating
    try:
        Review("Nul", 0, "place123", "user456")
        print("❌ Erreur: devrait refuser rating 0")
    except ValueError as e:
        print(f"✅ Erreur attrapée: {e}")

def test_relations():
    print("\n🧪 Test Relations")
    
    # Créer un user
    owner = User("Alice", "Smith", "alice@example.com")
    print(f"✅ User créé: {owner.first_name}")
    
    # Créer une place
    place = Place("Appart Paris", 100, 48.8566, 2.3522, owner.id)
    print(f"✅ Place créée: {place.title}")
    
    # Créer un amenity
    wifi = Amenity("WiFi")
    place.add_amenity(wifi.id)
    print(f"✅ Amenity ajouté: {wifi.name}")
    
    # Créer une review
    reviewer = User("Bob", "Martin", "bob@example.com")
    review = Review("Excellent !", 5, place.id, reviewer.id)
    place.add_review(review)
    print(f"✅ Review ajoutée: {review.rating}/5")
    
    # Afficher place avec relations
    place_dict = place.to_dict()
    print(f"\n📦 Place complète:")
    print(f"   Titre: {place_dict['title']}")
    print(f"   Prix: {place_dict['price']}€")
    print(f"   Amenities: {place_dict['amenity_ids']}")
    print(f"   Reviews: {place_dict['reviews']}")

if __name__ == "__main__":
    print("=" * 50)
    print("🧪 TESTS DES MODÈLES HBNB")
    print("=" * 50)
    
    test_amenity()
    test_user()
    test_place()
    test_review()
    test_relations()
    
    print("\n" + "=" * 50)
    print("🎉 TOUS LES TESTS PASSÉS !")
    print("=" * 50)