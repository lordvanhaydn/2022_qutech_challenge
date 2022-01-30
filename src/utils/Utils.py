import typing


class Utils:

    @staticmethod
    def merge_keys(base_a: typing.List[int],
                   base_b: typing.List[int],
                   raw_key: typing.List[int]) -> typing.List[int]:
        assert len(base_a) == len(base_b) == len(raw_key)
        final_key = []
        for i, (a, b) in enumerate(list(zip(base_a, base_b))):
            if a == b:
                final_key.append(raw_key[i])
        return final_key
