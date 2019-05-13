import pytest  # type: ignore
from testlib.base import Scenario
import cmk_base.config as config
import cmk_base.check_api as check_api
import cmk_base.check_table as check_table


# TODO: This misses a lot of cases
# - different get_check_table arguments
@pytest.mark.parametrize(
    "hostname,expected_result",
    [
        ("empty-host", {}),
        # Skip the autochecks automatically for ping hosts
        ("ping-host", {}),
        ("no-autochecks", {
            ('smart.temp', '/dev/sda'): ({
                'levels': (35, 40)
            }, u'Temperature SMART /dev/sda', []),
        }),
        # Static checks overwrite the autocheck definitions
        ("autocheck-overwrite", {
            ('smart.temp', '/dev/sda'): ({
                'levels': (35, 40)
            }, u'Temperature SMART /dev/sda', []),
            ('smart.temp', '/dev/sdb'): ({
                'is_autocheck': True
            }, u'Temperature SMART /dev/sdb', []),
        }),
        ("ignore-not-existing-checks", {}),
        ("ignore-disabled-rules", {
            ('smart.temp', 'ITEM2'): ({
                'levels': (35, 40)
            }, u'Temperature SMART ITEM2', []),
        }),
        ("static-check-overwrite", {
            ('smart.temp', '/dev/sda'): ({
                'levels': (35, 40),
                'rule': 1
            }, u'Temperature SMART /dev/sda', [])
        }),
        ("node1", {
            ('smart.temp', 'auto-not-clustered'): ({}, u'Temperature SMART auto-not-clustered', []),
            ('smart.temp', 'static-node1'): ({
                'levels': (35, 40)
            }, u'Temperature SMART static-node1', []),
        }),
        ("cluster1", {
            ('smart.temp', 'static-cluster'): ({
                'levels': (35, 40)
            }, u'Temperature SMART static-cluster', []),
            ('smart.temp', 'auto-clustered'): ({
                'levels': (35, 40)
            }, u'Temperature SMART auto-clustered', []),
        }),
    ])
def test_get_check_table(monkeypatch, hostname, expected_result):
    autochecks = {
        "ping-host": [("smart.temp", "bla", {})],
        "autocheck-overwrite": [
            ('smart.temp', '/dev/sda', {
                "is_autocheck": True
            }),
            ('smart.temp', '/dev/sdb', {
                "is_autocheck": True
            }),
        ],
        "ignore-not-existing-checks": [("bla.blub", "ITEM", {}),],
        "node1": [("smart.temp", "auto-clustered", {}), ("smart.temp", "auto-not-clustered", {})],
    }

    ts = Scenario().add_host(hostname, tags={"criticality": "test"})
    ts.add_host("ping-host", tags={"agent": "no-agent"})
    ts.add_host("node1")
    ts.add_cluster("cluster1", nodes=["node1"])
    ts.set_option(
        "static_checks",
        {
            "temperature": [
                (('smart.temp', '/dev/sda', {}), [], ["no-autochecks", "autocheck-overwrite"]),
                (('blub.bla', 'ITEM', {}), [], ["ignore-not-existing-checks"]),
                (('smart.temp', 'ITEM1', {}), [], ["ignore-disabled-rules"], {
                    "disabled": True
                }),
                (('smart.temp', 'ITEM2', {}), [], ["ignore-disabled-rules"]),
                (('smart.temp', '/dev/sda', {
                    "rule": 1
                }), [], ["static-check-overwrite"]),
                (('smart.temp', '/dev/sda', {
                    "rule": 2
                }), [], ["static-check-overwrite"]),
                (('smart.temp', 'static-node1', {}), [], ["node1"]),
                (('smart.temp', 'static-cluster', {}), [], ["cluster1"]),
            ]
        },
    )
    ts.set_ruleset("clustered_services", [
        ([], ['node1'], [u'Temperature SMART auto-clustered$']),
    ])
    config_cache = ts.apply(monkeypatch)
    monkeypatch.setattr(config_cache, "get_autochecks_of", lambda h: autochecks.get(h, []))
    config.load_checks(check_api.get_check_api_context, ["checks/smart"])
    assert check_table.get_check_table(hostname) == expected_result
