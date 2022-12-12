"""Iterable
__iter__ 가 구현된 걸 Iterable 객체
__next__가 구현된 걸 Iterator라고 한다.

파이썬은 반복할 수 있는지를 확인하기 위해 아래 2가지를 확인한다.
1. 객체가 __next__나 __iter__를 가지고 있는가?
2. 객체가 Sequence이면서 __len__과 __getitem__을 가지고 있는가?

파이썬은 객체를 반복하려고 하면 iter() 함수를 호출한다. 
iter() 함수는 __iter__가 있는지 확인하고, 있으면 __iter__를 싫행한다.
"""

## iterable
from datetime import timedelta, date


class DateRangeIterable:
    """자체적으로 __iter__를 가지고 있는 Iterable"""

    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self._present_day = start_date

    def __iter__(self):
        return self

    def __next__(self):
        if self._present_day >= self.end_date:
            raise StopIteration()

        today = self._present_day
        self._present_day += timedelta(days=1)
        return today


for day in DateRangeIterable(date(2022, 1, 1), date(2022, 1, 5)):
    print(day)
    # 2022-01-01
    # 2022-01-02
    # 2022-01-03
    # 2022-01-04


## Sequence
"""파이토치의 dataset은 이렇게 Custom Sequence를 만드는 것과 같다."""


class DateRangeSequence:
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self._range = self._create_range()

    def _create_range(self):
        days = []
        current_day = self.start_date
        while current_day < self.end_date:  ## 끝에 도달할 때까지 반복
            days.append(current_day)
            current_day += timedelta(days=1)
        return days  ## 그 범위 안에 있는 날들의 list를 반환해줌

    def __getitem__(self, day_no):  # 위에서 나온 list에서 day_no 번째 날짜를 가져옴
        return self._range[day_no]

    def __len__(self):
        return len(self._range)


s1 = DateRangeSequence(date(2022, 1, 1), date(2022, 1, 5))
for day in s1:
    print(day)

print(s1[0])
