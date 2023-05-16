from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    prato = Dish('risoto', 50.00)

    assert prato.name == 'risoto'

    assert prato.price == 50.00

    assert prato.recipe == {}

    with pytest.raises(TypeError):
        Dish('risoto', '50')

    with pytest.raises(ValueError):
        Dish('risoto', -50.00)

    assert hash(prato) == hash(prato)

    prato2 = Dish('churrasco', 90.00)

    assert hash(prato) != hash(prato2)

    prato2 == Dish('churrasco', 90.00)

    assert prato2.get_ingredients() == set()

    assert repr(prato) == "Dish('risoto', R$50.00)"

    assert repr(prato) != "Dish('lasanha', R$150.00)"

    assert prato == Dish('risoto', 50.00)

    assert prato != Dish('camarao', 200.00)

    ingrediente_farinha = Ingredient('farinha')

    prato.add_ingredient_dependency(ingrediente_farinha, 5)

    farinha_restrictions = {Restriction.GLUTEN}

    assert prato.get_restrictions() == farinha_restrictions

    assert prato.get_ingredients() == {ingrediente_farinha}
