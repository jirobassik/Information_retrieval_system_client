from collections import namedtuple

price_game = namedtuple('Price', ('name', 'price',))


def convert_tuple(list_dicts: list[dict]) -> tuple:
    return [(dict_.get('id'), dict_.get('name'),) for dict_ in list_dicts]


def convert_tuple_price(list_dicts: list[dict]) -> tuple:
    return [(dict_.get('game'), price_game(dict_.get('name'), dict_.get('price'))) for dict_ in list_dicts]

def find_name(list_dicts: list[dict], name: str) -> bool:
    return True if name in (dict_.get('name') for dict_ in list_dicts) else False


def remove_dollar(price_dict: dict) -> list[dict]:
    price_dict['price'] = price_dict.get('price').amount
    return price_dict
