import pytest
import synthetic_data.basic as sb

@pytest.mark.parametrize(
    'plan',
    [sb.simple_count,
     sb.multi_count,
     sb.step_scan,
    ])
def test_data_generator(plan, mds):
    plan(mds)
