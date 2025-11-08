class Address:
    def __init__(self, city: str, street: str, building: str, postal_code: str = ""):
        self.city = city
        self.street = street
        self.building = building
        self.postal_code = postal_code

    def full_address(self) -> str:
        return f"{self.city}, {self.street} {self.building}, {self.postal_code}"
