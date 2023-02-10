# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02CreatePostAPITestCase.test_case status_code'] = '400'

snapshots['TestCase02CreatePostAPITestCase.test_case body'] = {
    'content': [
        'This field may not be blank.'
    ]
}
