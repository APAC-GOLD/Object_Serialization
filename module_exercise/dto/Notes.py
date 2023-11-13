from pydantic import BaseModel, field_validator


class ItemOrigin(BaseModel):
    country: str
    production_date: str

    @field_validator("country")
    @classmethod
    def check_valid_country(cls, country: str):
        assert country == "Ethiopia", "country name must be Ethiopia"
        return country

class InventoryItem(BaseModel):
    name: str
    quantity: int
    serial_num: str
    origin: ItemOrigin


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



OUTPUT
{'name': 'printer', 'quantity': 5, 'serial_num': 'hdouhkjn', 'origin': {'country': 'ethiopia', 'production_date': '02/12/2023'}}
{'name': 'printer', 'quantity': 5, 'serial_num': 'HDOUHKJN', 'origin': ItemOrigin(country='Ethiopia', production_date='02/12/2023')}
{'name': 'printer', 'quantity': 5, 'serial_num': 'HDOUHKJN', 'origin': ItemOrigin(country='Ethiopia', production_date='02/12/2023')}