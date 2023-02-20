# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02GetAllReactionsAPITestCase.test_case status_code'] = '400'

snapshots['TestCase02GetAllReactionsAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_LIMIT_LENGTH',
    'response': 'Limit should be greater than or equal to zero'
}
