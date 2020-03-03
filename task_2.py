from functools import total_ordering


class Version:

    def __init__(self, version):
        self.version = version

    def __str__(self):
        return self.version

    @staticmethod
    def shorten_line(object1, object2):
        found_line = ()
        elements_dict = list(zip(object1, object2))
        for item in elements_dict:
            if len(set(item)) > 1:
                found_line = item
                break
        if found_line is ():
            if object1 == object2:
                return '1', '1'
            elif len(object1) > len(object2):
                return '0', '1'
            elif len(object1) < len(object2):
                return '1', '0'
        else:
            return found_line

    @staticmethod
    def parse_digits(line):
        digits_list = []
        for item in line:
            if not item.isdigit():
                break
            else:
                digits_list.append(item)
        parsed_digit = ''.join(digits_list)
        return parsed_digit

    def find_values(self, other):
        version1 = str(self).replace('-', '')
        version2 = str(other).replace('-', '')
        elements_list_ver1 = [i for i in version1.split('.')]
        elements_list_ver2 = [i for i in version2.split('.')]
        found_line = self.shorten_line(elements_list_ver1, elements_list_ver2)
        if found_line[0].isdigit() and found_line[1].isdigit():
            return found_line[0], found_line[1]
        else:
            digits_new_version1 = self.parse_digits(found_line[0])
            digits_new_version2 = self.parse_digits(found_line[1])
            if digits_new_version1 != digits_new_version2:
                return digits_new_version1, digits_new_version2
            else:
                start = len(digits_new_version1)
                result_found_line = self.shorten_line(found_line[0][start:], found_line[1][start:])
                if result_found_line[0].isdigit() and result_found_line[1].isdigit():
                    return int(result_found_line[0]), int(result_found_line[1])
                else:
                    return ord(result_found_line[0]), ord(result_found_line[1])

    @total_ordering
    def __eq__(self, version_2):
        x = self.find_values(version_2)
        return x[0] == x[1]

    def __lt__(self, version_2):
        x = self.find_values(version_2)
        return x[0] < x[1]


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
