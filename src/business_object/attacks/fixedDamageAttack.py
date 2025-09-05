from business_object.attacks.abstractAttack import AbstractAttack


class FixedDamageAttack(AbstractAttack):
    """
    Attack that always inflicts a fixed amount of damage (its power).
    """

    def compute_damage(self, attacker, defender) -> int:
        return self._power
