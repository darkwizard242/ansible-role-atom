import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


ATOM_PACKAGE = 'atom'
ATOM_BINARY_PATH = '/usr/bin/atom'
ATOM_DEBIAN_REPO = '/etc/apt/sources.list.d/atom.list'
ATOM_EL_REPO = '/etc/yum.repos.d/atom.repo'


def test_atom_package_installed(host):
    host.package("ATOM_PACKAGE").is_installed


def test_atom_binary_exists(host):
    host.file('ATOM_BINARY_PATH').exists


def test_atom_binary_file(host):
    host.file('ATOM_BINARY_PATH').is_file


def test_atom_repo_exists(host):
    host.file('ATOM_DEBIAN_REPO').exists or \
      host.file('ATOM_EL_REPO').exists


def test_atom_repo_file(host):
    host.file('ATOM_DEBIAN_REPO').is_file or \
      host.file('ATOM_EL_REPO').is_file


def test_atom_binary_which(host):
    host.check_output('which atom') == ATOM_BINARY_PATH or \
      host.check_output('whereis atom') == ATOM_BINARY_PATH
