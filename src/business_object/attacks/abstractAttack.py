from abc import ABC, abstractmethod

class AbstractAttack(ABC):
    """
    Abstract class for attacks
    """

    def __init__(self, power: int, name: str = None, description: str = None):
        self._power: int = power
        self._name: str = name
        self._description: str = description

    @abstractmethod
    def compute_damage(self, attacker, defender) -> int:
        """
        
        """
        pass

    @property
    def power(self):
        return self._power

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description