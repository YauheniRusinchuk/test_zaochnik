
class DictCompare2:

    @staticmethod
    def compare(current_data:dict, second_data:dict) -> dict:
        result:dict = {}
        for key in current_data.keys():
            if key in second_data.keys():
                if current_data[key] != second_data[key]:
                    result[key] = second_data[key]
        return result
