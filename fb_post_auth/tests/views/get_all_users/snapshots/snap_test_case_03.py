# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase03GetAllUsersAPITestCase.test_case status_code'] = '400'

snapshots['TestCase03GetAllUsersAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_OFFSET_LENGTH',
    'response': 'Offset should be greater than or equal to zero'
}
