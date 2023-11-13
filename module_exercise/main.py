from dto.itemorigin import ItemOrigin
from dto.inventoryitem import InventoryItem

from pydantic import BaseModel, Field, validator

class itemorigin(BaseModel):
    country: str
    production_date: str

    @validator("country")
    def check_valid_country(cls, country: str):
        assert country == "ethiopia", "country name must be ethiopia"
        return country

class inventoryitem(BaseModel):
    name: str
    quantity: int
    serial_num: str
    origin: itemorigin

def main():
    item_origin = itemorigin(country="ethiopia", production_date="02/12/2023")
    my_item1 = inventoryitem(name="printer",
                             quantity=5,
                             serial_num="hdouhkjn",
                             origin=item_origin)
    my_serialized_object1 = my_item1.dict()
    print(my_serialized_object1)
    my_item2 = inventoryitem(**my_serialized_object1)
    print(my_item2.dict())

if __name__ == "__main__":
    main()



def main():
    item_origin = ItemOrigin(country = "Ethiopia", production_date = "02/12/2023")
    my_item1 = InventoryItem(name = "printer",
                             quantity = 5,
                             serial_num = "HDOUHKJN",
                             origin = item_origin)
    my_serialized_object1 = my_item1.__dict__
    print(my_serialized_object1)
    my_item2 = InventoryItem(**my_serialized_object1)
    print(my_item2.__dict__)

if __name__ == "__main__":
    main()