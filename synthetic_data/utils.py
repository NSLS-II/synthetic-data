from bluesky import RunEngine


def RE_with_mds(mds):
    RE = RunEngine({})
    RE.subscribe('all', mds.insert)
    return RE
