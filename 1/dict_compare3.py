

class DictCompare3:

    @staticmethod
    def compare(current:dict, second:dict) -> dict:
        result:dict = {}
        for k2, v2 in second.items():
            if k2 in current:
                if v2 != current[k2]:
                    result.update({k2 : v2})
            else:
                result.update({k2 : v2})
        return result
