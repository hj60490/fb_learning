# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase03GetPostsOfUserIdAPITestCase.test_case status_code'] = '400'

snapshots['TestCase03GetPostsOfUserIdAPITestCase.test_case body'] = {
    'limit': [
        'This field is required.'
    ]
}
