# Ansible
Is the command line tool which helps you interact with the servers in an Adhoc way

# Ansible Playbook
Is a set of yaml files contains a human readable tasks, handlers vars etc. 
It enables you to store these files in a source code managment system like 
github and to move to the concept of "infrastructure as a code".
Playbook yml file contains:
    
    - vars_files
    - pre_tasks
    - handlers
    - tasks
    - post_tasks

# Roles
Roles are a way to manage and group your tasks in a meaningful and more orgnized way.
Example you can have inside your playbook n number of roles and one of them can be
apache-role, postgres-role, nfs-role and nginx role etc..

To create an ansible role run this command:
`ansible-galaxy init role_name`

The structure of the role_name directory will be like below (example used is apache):

apache
├── defaults
│   └── main.yml
├── files
├── handlers
│   └── main.yml
├── meta
│   └── main.yml
├── README.md
├── tasks
│   └── main.yml
├── templates
├── tests
│   ├── inventory
│   └── test.yml
└── vars
    └── main.yml

                