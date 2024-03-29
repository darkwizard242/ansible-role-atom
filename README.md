[![build-test](https://github.com/darkwizard242/ansible-role-atom/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-atom/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-atom/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-atom/actions?query=workflow%3Arelease) ![Ansible Role](https://img.shields.io/ansible/role/43192?color=dark%20green%20) ![Ansible Role](https://img.shields.io/ansible/role/d/43192?label=role%20downloads) ![Ansible Quality Score](https://img.shields.io/ansible/quality/43192?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-atom&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-atom) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-atom&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ansible-role-atom) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-atom&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-atom) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-atom&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-atom) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-atom?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-atom?color=orange&style=flat-square)

# Ansible Role: atom

Role to install (_by default_) [atom](https://atom.io/) package or uninstall (_if passed as var_) on **Ubuntu** and **CentOS** systems.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables list:

```yaml
atom_app: atom
atom_desired_state: present
atom_gpg_key: https://packagecloud.io/AtomEditor/atom/gpgkey
atom_repo_desired_state: present
atom_repo_debian: deb [arch=amd64] https://packagecloud.io/AtomEditor/atom/any/ any main
atom_repo_debian_filename: atom
atom_repo_el: https://packagecloud.io/AtomEditor/atom/el/7/$basearch
atom_repo_el_name: Atom
atom_repo_el_description: Atom Editor
atom_repo_el_gpgcheck: no
atom_repo_el_repogpgcheck: yes
atom_repo_el_enabled: yes
atom_repo_el_filename: atom
```

### Variables table:

Variable                  | Description
------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------
atom_app                  | Defines the app to install i.e. **atom**
atom_desired_state        | Defined to dynamically set whether to install (i.e. either `present` or `latest`) or uninstall (i.e. `absent`) the package. Defaults to `present`
atom_gpg_key              | GPG key for Atom
atom_repo_desired_state   | State for repo to download Atom from. Can either be 'present' or 'absent'.
atom_repo_debian          | Atom's repo link for Debian based systems.
atom_repo_debian_filename | Name of file to save for atom's repo in `/etc/apt/sources.list.d/`
atom_repo_el              | Atom's repo link for EL based systems.
atom_repo_el_name         | Atom repo name for EL based systems.
atom_repo_el_description  | Description for Atom's repo for EL based systems.
atom_repo_el_gpgcheck     | Boolean operation for performing gpg check against gpg key. Can either be **yes** or **no**.
atom_repo_el_repogpgcheck | Boolean operation for performing gpg check against atom's repository gpg. Can either be **yes** or **no**.
atom_repo_el_enabled      | Boolean operation for setting repository to enabled or disabled. Can either be **yes** or **no**.
atom_repo_el_filename     | Name of file to save for atom's repo in `/etc/yum.repos.d/`

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **atom** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.atom
```

For customizing behavior of role (i.e. installation of latest **atom** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.atom
  vars:
    atom_desired_state: latest
```

For customizing behavior of role (i.e. un-installation of **atom** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.atom
  vars:
    atom_desired_state: absent
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-atom/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.alimuhammad.dev/).
