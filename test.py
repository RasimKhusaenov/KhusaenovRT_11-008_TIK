from btw import BTW
from main import btw_plus_mtf_encode, ac_decode
from mtf import MoveToFront


def is_result_expected(expectation, reality):
    return expectation == reality


btw_right_answers = [
    [["ABACABA", True], ("BCABAAA", 3)]
]
mtf_right_answers = [
    [["рдакраааабб"], 43243200040],
]
btw_plus_mrf_right_answers = [
    [["абракадабра", "абдкр"], (43243200040, 2)],
    [["ааааббббеееееддддда", "абде"], (2100002002000300002, 1)]
]
ac_right_answers = [
    [
        [["_", "а", "т", "е", "м", "о", "ф", "д", "л", "н", "у", "х", "ч", "ш", "э"],
         [0.12, 0.12, 0.12, 0.08, 0.08, 0.08, 0.08, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04],
         0.97218816,
         4],
        "этот"
    ],
    [
        [["a", "b", "c", "d"], [3/4, 1/8, 1/16, 1/16], 0.908203125, 4], "caad"
    ]
]
for inp, out in btw_right_answers:
    assert is_result_expected(BTW(*inp).encode(), out)
for inp, out in mtf_right_answers:
    assert is_result_expected(MoveToFront(*inp).encode(), out)
for inp, out in btw_plus_mrf_right_answers:
    assert is_result_expected(btw_plus_mtf_encode(*inp), out)
for inp, out in ac_right_answers:
    assert is_result_expected(ac_decode(*inp), out)
