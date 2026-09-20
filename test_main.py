import time
import unittest
from datetime import datetime, timedelta

from main import SHANGHAI_TZ, get_entry_dedup_key, is_recent_entry, parse_entry_datetime


class FeedEntryTests(unittest.TestCase):
    def test_parses_rfc822_time_into_shanghai_timezone(self):
        result = parse_entry_datetime("Sat, 19 Sep 2026 23:30:00 GMT")
        self.assertEqual(result.isoformat(), "2026-09-20T07:30:00+08:00")

    def test_falls_back_to_updated_struct_time(self):
        parsed = time.strptime("2026-09-19 23:30:00", "%Y-%m-%d %H:%M:%S")
        result = parse_entry_datetime(parsed_time=parsed)
        self.assertEqual(result.isoformat(), "2026-09-20T07:30:00+08:00")

    def test_missing_date_is_not_treated_as_now(self):
        self.assertIsNone(parse_entry_datetime(""))
        self.assertFalse(is_recent_entry({"published_at": ""}))

    def test_recent_window_crosses_midnight(self):
        now = datetime(2026, 9, 20, 8, 0, tzinfo=SHANGHAI_TZ)
        entry = {"published_at": (now - timedelta(hours=23, minutes=59)).isoformat()}
        self.assertTrue(is_recent_entry(entry, now))

    def test_old_entry_is_excluded(self):
        now = datetime(2026, 9, 20, 8, 0, tzinfo=SHANGHAI_TZ)
        entry = {"published_at": (now - timedelta(hours=24, seconds=1)).isoformat()}
        self.assertFalse(is_recent_entry(entry, now))

    def test_link_key_deduplicates_trailing_slash(self):
        first = get_entry_dedup_key({"link": "https://example.com/article/"})
        second = get_entry_dedup_key({"link": "https://example.com/article"})
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
