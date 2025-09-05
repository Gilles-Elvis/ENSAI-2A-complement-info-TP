import pytest

from business_object.attacks.fixedDamageAttack import FixedDamageAttack


class DummyPokemon:

    def __init__(self, name="Dummy"):
        self.name = name


class TestFixedDamageAttack:
    def test_damage_equals_power(self):
        # GIVEN
        attack = FixedDamageAttack(power=50, name="Explosion", description="Big boom")
        attacker = DummyPokemon("Attacker")
        defender = DummyPokemon("Defender")

        damage = attack.compute_damage(attacker, defender)

        assert damage == 50

    def test_damage_with_different_power(self):
        # GIVEN
        attack = FixedDamageAttack(power=120, name="Laser", description="Strong hit")
        attacker = DummyPokemon()
        defender = DummyPokemon()

        # WHEN
        damage = attack.compute_damage(attacker, defender)

        # THEN
        assert damage == 120

    def test_attack_attributes(self):
        # GIVEN
        attack = FixedDamageAttack(power=30, name="Punch", description="Simple punch")

        # THEN
        assert attack.power == 30
        assert attack.name == "Punch"
        assert attack.description == "Simple punch"


if __name__ == "__main__":
    pytest.main([__file__])
