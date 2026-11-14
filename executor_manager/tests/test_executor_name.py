# SPDX-FileCopyrightText: 2026 Weibo, Inc.
#
# SPDX-License-Identifier: Apache-2.0

from executor_manager.utils.executor_name import generate_executor_name


def test_executor_names_are_unique_per_subtask_and_stable():
    first = generate_executor_name(100, 200, "alice")
    second = generate_executor_name(100, 201, "alice")
    other_task = generate_executor_name(101, 200, "alice")

    assert first == generate_executor_name(100, 200, "alice")
    assert first != second
    assert first != other_task
    assert first.startswith("wegent-task-alice-")
