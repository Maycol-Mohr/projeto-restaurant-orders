from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingrediente_bacon = Ingredient('bacon')

    assert ingrediente_bacon.name == 'bacon'

    assert ingrediente_bacon.name != 'manteiga'

    assert Restriction.ANIMAL_MEAT in ingrediente_bacon.restrictions

    assert Restriction.ANIMAL_DERIVED in ingrediente_bacon.restrictions

    assert Restriction.GLUTEN not in ingrediente_bacon.restrictions

    assert Restriction.SEAFOOD not in ingrediente_bacon.restrictions

    assert ingrediente_bacon.restrictions == {
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED
    }

    assert ingrediente_bacon.restrictions != {
        Restriction.GLUTEN,
        Restriction.SEAFOOD
    }

    assert hash(ingrediente_bacon) == hash('bacon')

    assert hash(ingrediente_bacon) != hash('manteiga')

    assert repr(ingrediente_bacon) == "Ingredient('bacon')"

    assert repr(ingrediente_bacon) != "Ingredient('manteiga')"

    assert ingrediente_bacon == Ingredient('bacon')

    assert ingrediente_bacon != Ingredient('manteiga')
