# robogerctl

CLI tool for https://github.com/alttch/roboger

If installed on the same host with server, uses server configuration to
communicate.

Otherwise, create client configuration, put it to ~/.robogerctl.yml (default):

```yaml
uri: http://roboger-server:port
key: MANAGEMENT_KEY
#limits: true # set to manage server, where limits are enabled
```

## Installation

```
pip3 install robogerctl
```
