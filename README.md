to-be-defined
=========

[Ansible][ansible] role for management of Huawei Server driver version.

With this role, you could:

- list current driver versions
- upgrade driver versions
- query upgrade driver task progress

Requirements
------------

- ansible >= 2.4
- Target Huawei Server with iBMC


Role Variables
--------------

- **command**: what command of the role expected to run.
- **drivers**: a list of name/version for the drivers to be upgraded (used when command is `upgrade-driver`).
- **repo_baseurl**: driver yum repo baseurl (used when command is `list-driver` or `upgrade-driver`).
- **repo_gpgcheck**: driver yum repo gpgcheck [yes|no] (used when command is `list-driver` or `upgrade-driver`).
- **taskid**: async task-id of the upgrade driver task (used when command is `upgrade-progress`)

Dependencies
------------

None.

Example Playbook
----------------

- list driver versions:

```
---

- hosts: servers
  roles:
    - { role: 'to-be-defined', command: 'list-driver',  repo_baseurl: 'http://houp.huawei.com/download/server/Linux/Driver/Redhat/Rhel$releasever/$basearch/current/' }
```

- upgrade driver versions:

```
---

- hosts: localhost
  remote_user: root
  roles:
    - role: 'huawei.server-manager'
      command: 'upgrade-driver'
      # optional, default upgrade all driver and firmware
      drivers: 
        - ['driver1', 'driver1-version']
        - ['driver2', 'driver2-version']
      # optional, default huawei houp repo
      repo_baseurl: http://houp.huawei.com/download/server/Linux/Driver/Redhat/Rhel$releasever/$basearch/current/
      # optional, default no
      repo_gpgcheck: yes
```


- upgrade driver progress:

```
---

- hosts: servers
  roles:
    - { role: 'to-be-defined', command: 'upgrade-progress', taskid: 'task-id' }
```

License
-------

Apache 2.0


[ansible]:  https://ansible.com/    "Ansible"