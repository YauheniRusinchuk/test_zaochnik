
class DictCompare1:

    @staticmethod
    def compare(current:dict, second:dict) -> dict:
        c_keys:set = set(current.keys())
        s_keys:set = set(second.keys())
        intersect_keys:set = c_keys.intersection(s_keys)
        res:dict = {i : second[i] for i in intersect_keys if current[i] != second[i]}
        return res
