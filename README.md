ansible-btsync
==============

Ansible playbooks for deploying and updating btsync nodes
All code is Ubuntu specific

Role variables
==============

There is only one  mandatory variable
`btsync_user`: The system user who runs the btsync daemon

All other variables are optional. Full list of optional variable are in `btsync/defaults/main.yml`

btsync daemon configuration follows the structure of the original JSON configuration
All variable are the same but in YAML format. 

Examples
==============

```yaml
    roles:
       - role: btsync
         btsync_user: btsync

         btsync_settings: 
             device_name: "{{ ansible_fqdn }}" 
             listening_port : 5999
             pid_file : "{{ btsync_home }}/.sync/btsync.pid"
             storage_path : "{{ btsync_home }}/.sync"
             use_upnp : false
             shared_folders : 
                - dir: "{{ btsync_home }}/Folder_one"
                  secret: PUTYOURLONGMAGICSECRETHERE
                - dir: "{{ btsync_home }}/Folder_Two"
                  secret: PUTYOURLONGMAGICSECRETHERE
```

```yaml
    roles:
       - role: btsync
         btsync_user: btsync
         btsync_settings: 
             device_name: "{{ ansible_fqdn }}" 
             pid_file : "{{ btsync_home }}/.sync/btsync.pid"
             storage_path : "{{ btsync_home }}/.sync"
             webui:
                 listen : "127.0.0.1:8888"
            
```
