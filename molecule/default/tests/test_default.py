import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_atom_package_installed(host):
    assert host.package("atom").is_installed


def test_atom_binary_exists(host):
    assert host.file('/usr/bin/atom').exists


def test_atom_binary_file(host):
    assert host.file('/usr/bin/atom').is_file


def test_atom_repo_exists(host):
    assert host.file('/etc/apt/sources.list.d/atom.list').exists or \
      host.file('/etc/yum.repos.d/atom.repo').exists


def test_atom_repo_file(host):
    assert host.file('/etc/apt/sources.list.d/atom.list').is_file or \
      host.file('/etc/yum.repos.d/atom.repo').is_file


def test_atom_binary_which(host):
    assert host.check_output('which atom') == '/usr/bin/atom' or \
      host.check_output('whereis atom') == '/usr/bin/atom'


def test_apm_binary_exists(host):
    assert host.file('/usr/bin/apm').exists


def test_apm_binary_file(host):
    assert host.file('/usr/bin/apm').is_symlink


def test_apm_binary_which(host):
    assert host.check_output('which apm') == '/usr/bin/apm' or \
      host.check_output('whereis apm') == '/usr/bin/apm'
