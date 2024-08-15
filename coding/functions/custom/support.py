import re
from string import punctuation

import numpy as np
from unidecode import unidecode


def human_format(num, n_decimal=None):
    num = float('{:.3g}'.format(num))
    magnitude = 0
    fmt_text = '{:' + ("" if n_decimal is None else '.{}'.format(int(n_decimal))) + 'f}'
    while (abs(num) >= 1000) and (magnitude < 4):
        magnitude += 1
        num /= 1000.0
    return '{}{}'.format(fmt_text.format(num).rstrip('0').rstrip('.'), ['', 'K', 'M', 'B', 'T'][magnitude])


class text:
    """Chuẩn hóa dữ liệu text
    """

    def __init__(self):
        pass

    def remove_punctuation(str_data):
        """
        Xóa bỏ ký tự đặc biệt và đuôi float .0
        """
        str_data = re.sub(' +', ' ', str(str_data)).strip()
        for e in ['.0', '.00', ',0', ',00']:
            if str_data.endswith(e):
                str_data = str_data[:-len(e)]
                break
        str_data = str_data.translate(str.maketrans('', '', punctuation)).strip()
        return str_data

    def clean(value, space=True, end_dotzero=False, punc=False, nan=True, use_unidecode=False):
        """Convert nan/none value ở dạng string thành NaN

        Returns:
            _type_: _description_
        """

        def space_clean(value):
            return re.sub(' +', ' ', value).strip()

        def end_dotzero_clean(value):
            for e in ['.0', '.00', ',0', ',00']:
                if value.endswith(e):
                    value = value[:-len(e)]
                    break
            return value

        def punctuation_clean(value):
            return value.translate(str.maketrans('', '', punctuation))

        def nan_clean(value):
            value = str(value)
            nan_list = ['', '#n/a', '#n/a n/a', '#na',
                        '#ref!', '(null)', ',', '-1.#ind',
                        '-1.#qnan', '-nan', '.', '1.#ind',
                        '1.#qnan', '<na>', 'n/a', 'na',
                        'nan', 'none', 'null', ]
            condi = (value.lower() in nan_list)
            if condi:
                return np.nan
            else:
                return value

        if (value is np.nan) or (value is None) or (nan_clean(value) is np.nan):  # None or nan
            return np.nan
        if type(value) == str:
            if space: value = space_clean(value)
            if end_dotzero: value = end_dotzero_clean(value)
            if nan: value = nan_clean(value)
            if punc: value = punctuation_clean(value)
            if use_unidecode: value = unidecode(value)
        return value


class Phone(text):
    """Lấy thông tin từ 1 số điện thoại

    Args:
        text (_type_): _description_
    """

    def __init__(self, value=None, dialcode="84", error='ignore'):
        self.value = str(value)
        self.dialcode = dialcode
        self.error = error
        self.chuyendausodidong = [
            ['162', '32'], ['163', '33'], ['164', '34'], ['165', '35'], ['166', '36'], ['167', '37'], ['168', '38'],
            ['169', '39'],
            ['120', '70'], ['121', '79'], ['122', '77'], ['126', '76'], ['128', '78'], ['123', '83'], ['124', '84'],
            ['125', '85'],
            ['127', '81'], ['129', '82'], ['182', '52'], ['186', '56'], ['188', '58'], ['199', '59']
        ]
        self.chuyendausocodinh = [
            ['76', '296'], ['64', '254'], ['281', '209'], ['240', '204'], ['781', '291'], ['241', '222'], ['75', '275'],
            ['56', '256'], ['650', '274'], ['651', '271'], ['62', '252'], ['780', '290'], ['710', '292'], ['26', '206'],
            ['511', '236'], ['500', '262'], ['501', '261'], ['230', '215'], ['61', '251'], ['67', '277'], ['59', '269'],
            ['219', '219'], ['351', '226'], ['4', '24'], ['39', '239'], ['320', '220'], ['31', '225'], ['711', '293'],
            ['8', '28'], ['218', '218'], ['321', '221'], ['8', '258'], ['77', '297'], ['60', '260'], ['231', '213'],
            ['63', '263'], ['25', '205'], ['20', '214'], ['72', '272'], ['350', '228'], ['38', '238'], ['30', '229'],
            ['68', '259'], ['210', '210'], ['57', '257'], ['52', '232'], ['510', '235'], ['55', '255'], ['33', '203'],
            ['53', '233'], ['79', '299'], ['22', '212'], ['66', '276'], ['36', '227'], ['280', '208'], ['37', '237'],
            ['54', '234'], ['73', '273'], ['74', '294'], ['27', '207'], ['70', '270'], ['211', '211'], ['29', '216'],
        ]
        self.dausodidong = [i[1] for i in self.chuyendausodidong] + \
                           ['86', '96', '97', '98', '88', '91', '94', '89', '90', '93', '92', '56', '58', '99', '87']
        self.dausocodinh = [i[1] for i in self.chuyendausocodinh]
        # self.typephone = 'unknown'
        self.cleaned = self.standardize()

    def cleankey(self):
        """Hàm làm sạch input

        Raises:
            ValueError: _description_

        Returns:
            _type_: _description_
        """
        self.typephone = 'unknown'
        dialcode = self.dialcode

        def isAllNumber(text):
            for char in text:
                if not char.isnumeric():
                    return False
            return True

        cleaned = text.clean(self.value, True, True, True, True, False).replace(" ", "")
        assert isAllNumber(cleaned)

        runtime = 0

        while (len(cleaned) >= 9) and (runtime < 30) and (self.typephone == 'unknown'):

            cleaned = cleaned[5:] if bool(re.match('8400[0-9]{1,1}', cleaned[:5])) and (len(cleaned) >= 14) else cleaned
            cleaned = cleaned[1:] if cleaned[0] == '0' else cleaned
            if ((cleaned[:len(dialcode)] == dialcode) and len(cleaned) >= (9 + len(dialcode))):
                cleaned = cleaned[len(dialcode):]

            if (len(cleaned) == 9) and (self.typephone == 'unknown'):
                for i in self.dausodidong:
                    if cleaned.startswith(i):
                        self.typephone = 'so_di_dong'
                        break

            if (len(cleaned) in [9, 10]) and (self.typephone == 'unknown'):
                for i in self.dausocodinh:
                    if cleaned.startswith(i) and (
                            len(cleaned[len(i):]) in [7, 8]):  # ví du 0220 3736 596 (HD), 024 392 63087 (HN)
                        self.typephone = 'so_co_dinh'
                        break

            if (len(cleaned) == 10) and (self.typephone == 'unknown'):
                for pair in self.chuyendausodidong:
                    if cleaned.startswith(pair[0]):
                        cleaned = cleaned.replace(pair[0], pair[1], 1)
                        self.typephone = 'so_di_dong'
                        break

            if (len(cleaned) in [9, 10]) and (self.typephone == 'unknown'):
                for pair in self.chuyendausocodinh:
                    if cleaned.startswith(pair[0]) and (
                            len(cleaned[len(pair[0]):]) in [7, 8]):  # ví du 0220 3736 596 (HD), 024 392 63087 (HN)
                        cleaned = cleaned.replace(pair[0], pair[1], 1)
                        self.typephone = 'so_co_dinh'
                        break

            runtime += 1

        if runtime == 30:
            raise ValueError
        else:
            return cleaned

    def standardize(self):
        """Hàm chuẩn hóa SĐT

        Returns:
            _type_: _description_
        """
        try:
            res = self.dialcode + self.cleankey()
        except:
            if self.error == 'ignore':
                res = self.value
            if self.error == 'nan':
                res = np.nan

        return res

    def pay_type(paytype):
        """Hàm chuẩn hóa thông tin paytype

        Args:
            paytype (_type_): _description_

        Returns:
            _type_: _description_
        """
        if paytype != paytype:
            return np.nan
        paytype = text.clean(str(paytype), True, True, True, True, True).lower()
        if len([i for i in ['pre', 'truoc', 'tt'] if i in paytype]) > 0:
            return 'prepaid'
        elif len([i for i in ['post', 'sau', 'ts'] if i in paytype]) > 0:
            return 'postpaid'
        else:
            return np.nan
