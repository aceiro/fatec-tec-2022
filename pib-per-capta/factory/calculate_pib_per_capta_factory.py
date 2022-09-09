from singleton.calculate_pib_per_capta_singleton import CalculatePibPerCaptaSingleton

class CalculatePibPerCaptaFactory:
    @classmethod
    def create_instance(self):
        return CalculatePibPerCaptaSingleton.get_instance()
