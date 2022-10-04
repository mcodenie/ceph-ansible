import pytest


class TestInfluxDB(object):

    @pytest.mark.dashboard
    def test_influxdb_service_enabled_and_running(self, node, host):
        s = host.service("influxdb")
        assert s.is_enabled
        assert s.is_running

    @pytest.mark.dashboard
    def test_influxdb_socket(self, node, host):
        assert host.socket('tcp://8086').is_listening
