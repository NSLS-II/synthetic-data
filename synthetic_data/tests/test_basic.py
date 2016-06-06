import pytest
import synthetic_data.basic as sb

@pytest.mark.parametrize(
    'plan',
    [sb.simple_count,
     sb.multi_count,
     sb.step_scan,
     sb.step_scan_with_overlapping_baseline,
     sb.step_scan_with_distinct_baseline,
    ])
def test_data_generator(plan, mds):
    plan(mds)
