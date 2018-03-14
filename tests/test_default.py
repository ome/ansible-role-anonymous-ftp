import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_upload(Command, Sudo, File):
    with Sudo():
        out = Command('rm -f /srv/ftp-incoming/upload_test.sh')

    out = Command.check_output('/upload_test.sh')

    with Sudo():
        f = File('/srv/ftp-incoming/upload_test.sh')
        assert f.exists
        assert f.size > 1
        assert out == ''
