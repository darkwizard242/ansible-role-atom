import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


PACKAGE = 'atom'
PACKAGE_BINARY = '/usr/bin/atom'
REPO_DEBIAN_FILE = '/etc/apt/sources.list.d/atom.list'
REPO_EL_FILE = '/etc/yum.repos.d/atom.repo'


def test_atom_package_installed(host):
    """
    Tests if atom package is installed.
    """
    assert host.package(PACKAGE).is_installed


def test_atom_binary_exists(host):
    """
    Tests if atom binary exists.
    """
    assert host.file(PACKAGE_BINARY).exists


def test_atom_binary_file(host):
    """
    Tests if atom binary is a file type.
    """
    assert host.file(PACKAGE_BINARY).is_file


def test_atom_repo_exists(host):
    """
    Tests if atom repo file exists.
    """
    assert host.file(REPO_DEBIAN_FILE).exists or \
        host.file(REPO_EL_FILE).exists


def test_atom_repo_file(host):
    """
    Tests if atom repo file is file type.
    """
    assert host.file(REPO_DEBIAN_FILE).is_file or \
        host.file(REPO_EL_FILE).is_file


def test_atom_binary_which(host):
    """
    Tests the output to confirm atom's binary location.
    """
    assert host.check_output('which atom') == PACKAGE_BINARY or \
        host.check_output('whereis atom') == PACKAGE_BINARY
