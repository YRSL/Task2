from functools import total_ordering


class Version:

    def __init__(self, version: str):
        self.ver2 = str()
        self.version = version

    def __init__(self, version):
        self.version = version

    def __str__(self):
        return self.version

    def convert_into_ord(self, ver2):
        el1 = [i for i in self.version.split('.')]
        el2 = [i for i in self.ver2.split('.')]
        po = dict(zip(el1, el2))
        po = {k: v for k, v in po.items() if k != v}
        if len(po) != 0:
            so = list(po.items())[0]
            result_item1 = so[0]
            result_item2 = so[1]
            res_gen = [ord(i) for i in result_item1]
            res_gen1 = [ord(i) for i in result_item2]
            if len(res_gen) > len(res_gen1):
                res_gen = res_gen[:len(res_gen1) + 1]
                res_gen1.append(0)
            elif len(res_gen) < len(res_gen1):
                res_gen1 = res_gen1[:len(res_gen) + 1]
                res_gen.append(0)
            el1x = [i for i in res_gen]
            el2x = [i for i in res_gen1]
            zo = dict(zip(el1x, el2x))
            zo = {k: v for k, v in zo.items() if k != v}
            so = list(zo.items())[0]
            return so[0], so[1]

    @total_ordering
    def __eq__(self, version_2):
        so = self.convert_into_ord(version_2)
        if so is None:
            return int(so[0]) == int(so[1])

    def __lt__(self, version_2):
        so = self.convert_into_ord(version_2)
        return int(so[0]) < int(so[1])


def main():
    to_test = [
        ('1.0.0', '2.0.0'),
        ('1.0.0', '1.42.0'),
        ('1.2.0', '1.2.42'),
        ('1.1.0-alpha', '1.2.0-alpha.1'),
        ('1.0.1b', '1.0.10-alpha.beta'),
        ('1.0.0-rc.1', '1.0.0'),
    ]

    for version_1, version_2 in to_test:
        assert Version(version_1) < Version(version_2), 'le failed'
        assert Version(version_2) > Version(version_1), 'ge failed'
        assert Version(version_2) != Version(version_1), 'neq failed'


if __name__ == "__main__":
    main()
