###
### config_remote.py - configuration for remote servers
###

NODES = ["hp036.utah.cloudlab.us", "hp004.utah.cloudlab.us", "hp030.utah.cloudlab.us","hp040.utah.cloudlab.us","hp003.utah.cloudlab.us"]

# Public domain or IP of server
SERVERS = NODES[0:1]
# Public domain or IP of intemediate
INTNODES = []
# Public domain or IP of client and agents
CLIENTS = NODES[1:]
# Public domain or IP of client
CLIENT = CLIENTS[0]
AGENTS = CLIENTS[1:]

# Public domain or IP of monitor
MONITOR = ""

# Username and SSH credential location to access
# the server, client, and agents via public IP
USERNAME = "csathe"
KEY_LOCATION = "/Users/chaitrasathe/.ssh/gt"

# Location of Shenango to be installed. With "", Shenango
# will be installed in the home direcotry
ARTIFACT_PARENT = ""

KERNEL_NAME = "caladan"

### End of config ###

ARTIFACT_PATH = ARTIFACT_PARENT
if ARTIFACT_PATH != "":
    ARTIFACT_PATH += "/"
ARTIFACT_PATH += "bw_caladan"
