[![Build Status](https://travis-ci.com/darkwizard242/ansible-role-atom.svg?branch=master)](https://travis-ci.com/darkwizard242/ansible-role-atom) ![Ansible Role](https://img.shields.io/ansible/role/43192?color=dark%20green%20) ![Ansible Role](https://img.shields.io/ansible/role/d/43192?label=role%20downloads) ![Ansible Quality Score](https://img.shields.io/ansible/quality/43192?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-atom&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-atom) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-atom?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-atom?color=orange&style=flat-square)

# Ansible Role: atom

Role to install (_by default_) `atom` package or uninstall (_if passed as var_) on **Ubuntu** and **CentOS** systems.

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

Variable                  | Value (default)                                                       | Description
------------------------- | --------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------
atom_app                  | `atom`                                                                | Defines the app to install i.e. **atom**
atom_desired_state        | `present`                                                             | Defined to dynamically set whether to install (i.e. either `present` or `latest`) or uninstall (i.e. `absent`) the package. Defaults to `present`
atom_gpg_key              | <https://dl.google.com/linux/linux_signing_key.pub>                   | GPG key for Atom
atom_repo_desired_state   | `present`                                                             | State for repo to download Atom from. Can either be 'present' or 'absent'.
atom_repo_debian          | `deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main` | Atom's repo link for Debian based systems.
atom_repo_debian_filename | `atom`                                                                | Name of file to save for atom's repo in `/etc/apt/sources.list.d/`
atom_repo_el              | <http://dl.google.com/linux/chrome/rpm/stable/x86_64>                 | Atom's repo link for EL based systems.
atom_repo_el_name         | `atom`                                                                | Atom repo name for EL based systems.
atom_repo_el_description  | `atom`                                                                | Description for Atom's repo for EL based systems.
atom_repo_el_gpgcheck     | **yes**                                                               | Boolean operation for performing gpg check against gpg key. Can either be **yes** or **no**.
atom_repo_el_repogpgcheck | **yes**                                                               | Boolean operation for performing gpg check against atom's repository gpg. Can either be **yes** or **no**.
atom_repo_el_enabled      | **yes**                                                               | Boolean operation for setting repository to enabled or disabled. Can either be **yes** or **no**.
atom_repo_el_filename     | `atom`                                                                | Name of file to save for atom's repo in `/etc/yum.repos.d/`

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **atom** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - role: darkwizard242.atom
```

For customizing behavior of role (i.e. installation of latest **atom** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - role: darkwizard242.atom
      vars:
        atom_desired_state: latest
```

For customizing behavior of role (i.e. un-installation of **atom** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - role: darkwizard242.atom
      vars:
        atom_desired_state: absent
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-atom/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.linkedin.com/in/ali-muhammad-759791130/).
