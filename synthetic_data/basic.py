from bluesky.plans import count, scan, fly, baseline_wrapper
from bluesky.examples import det, det1, motor
from .utils import RE_with_mds


def simple_count(mds):
    RE = RE_with_mds(mds)
    return RE(count([det]))


def multi_count(mds):
    RE = RE_with_mds(mds)
    return RE(count([det], num=3))


def step_scan(mds):
    RE = RE_with_mds(mds)
    return RE(scan([det], motor, 1, 5, 5))


def step_scan_with_overlapping_baseline(mds):
    "same det in 'baseline' and in 'primary' event stream"
    RE = RE_with_mds(mds)
    return RE(baseline_wrapper(scan([det], motor, 1, 5, 5), [det]))


def step_scan_with_distinct_baseline(mds):
    "'baseline' and 'primary' event stream use different dets"
    RE = RE_with_mds(mds)
    return RE(baseline_wrapper(scan([det], motor, 1, 5, 5), [det1]))


def fly_scan(mds):
    RE = RE_with_mds(mds)
    return RE(fly([flyer]))
