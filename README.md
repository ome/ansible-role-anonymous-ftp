Anonymous FTP
=============

[![Build Status](https://travis-ci.org/openmicroscopy/ansible-role-anonymous-ftp.svg)](https://travis-ci.org/openmicroscopy/ansible-role-anonymous-ftp)
[![Ansible Role](https://img.shields.io/ansible/role/24437.svg)](https://galaxy.ansible.com/openmicroscopy/anonymous-ftp/)


Anonymous FTP using VSFTPD in Docker.

Note FTP is a very old protocol that does not follow modern patterns.
You should be familiar with this protocol before setting up this server, particularly if you need to configure firewalls, forwarding or monitoring.


Dependencies
------------

This requires Docker to be installed.
This is not handled by this role.


Variables
---------

Required:
- `anonymous_ftp_incoming_data_dir`: Directory for incoming files

Optional:
- `anonymous_ftp_image`: Docker image for the FTP server, default `openmicroscopy/vsftpd-anonymous-upload:0.1.0`
- `anonymous_ftp_incoming_group`: Group name/id for the uploads data directory, default `root`
- `anonymous_ftp_public_address`: Externally facing IP of the FTP server, will be guessed but it is strongly recommended that you set this
- `anonymous_ftp_emails`: List of emails for anonymous password, default empty
- `anonymous_ftp_port`: Published port for incoming FTP, default `21`
- `anonymous_ftp_pasv_min_port`: Passive port range (minimum, default `32022`)
- `anonymous_ftp_pasv_max_port`: Passive port range (maximum, default `32031`)
- `anonymous_ftp_banner_text`: Banner text


Example playbook
----------------
    - hosts: all
      roles:
        - role: openmicroscopy.docker
        - role: openmicroscopy.anonymous-ftp
          anonymous_ftp_incoming_data_dir: /srv/ftp-incoming
          anonymous_ftp_public_address: 10.0.0.1
          anonymous_ftp_emails:
          - allowed@example.org


Author Information
------------------

ome-devel@lists.openmicroscopy.org.uk
