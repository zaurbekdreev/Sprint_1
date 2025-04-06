from typing import Union


class TestCase:

    def __init__(self, steps: Union[None, dict] = None, result: Union[None, dict] = None):
        self.steps: dict = steps if steps else {}
        self.result: str = result

    def set_step(self, step_number: int, step_text: str) -> None:
        self.steps[step_number] = step_text

    def delete_step(self, step_number: int) -> None:
        del self.steps[step_number] 

    def set_result(self, result: str) -> None:
        self.result = result

    def get_test_case(self) -> None:

        result = {
            'Шаги': self.steps,
            'Ожидаемый результат': self.result
        }

        print(result)
