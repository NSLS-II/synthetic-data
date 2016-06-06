import uuid
import pytest
from metadatastore.mds import MDS
from metadatastore.utils import create_test_database


@pytest.fixture(scope='function')
def mds(request):
    db_template = "mds_testing_disposable_{}".format(str(uuid.uuid4()))
    test_conf = create_test_database('localhost', db_template=db_template)
    mds = MDS(test_conf)

    def delete_dm():
        print("DROPPING DB")
        mds._connection.drop_database(test_conf['database'])

    request.addfinalizer(delete_dm)

    return mds
