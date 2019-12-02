import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_upload(host):
    with host.sudo():
        out = host.run('rm -f /srv/ftp-incoming/upload_test.sh')

    out = host.check_output('/upload_test.sh')

    with host.sudo():
        f = host.file('/srv/ftp-incoming/upload_test.sh')
        assert f.exists
        assert f.size > 1
        assert out == ''
