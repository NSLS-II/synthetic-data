from bluesky.plans import count, scan, fly
from bluesky.examples import det, motor
from .utils import RE_with_mds


def simple_count(mds):
    RE = RE_with_mds(mds)
    RE(count([det]))


def multi_count(mds):
    RE = RE_with_mds(mds)
    RE(count([det], num=3))


def step_scan(mds):
    RE = RE_with_mds(mds)
    RE(scan([det], motor, 1, 5, 5))


def fly_scan(mds):
    RE = RE_with_mds(mds)
    RE(fly([flyer]))
