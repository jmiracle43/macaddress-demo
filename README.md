# MacAddress.io CLI tool
## Quick example
### Build the tool
Build the tool (UNIX/MAC Platforms)

`./build.sh`

Other platforms (e.g. Windows)

`docker build -t macaddress-io-tools:latest .`

Run the tool (UNIX/MAC Platforms)

`MAC_API_KEY=<your key here> ./run.sh -m <mac-address-to-search>`

Run the tool (Other platforms)

`docker run -it -e "MAC_API_KEY=<your key here>" macaddress-io-tools:latest -m <mac-address-to-search>`


## Example run
```bash
MAC_API_KEY=<hidden> ./run.sh -m E8:6A:64:F4:3E:F0
+ cd /usr/src/app
+ python macaddress.py -m E8:6A:64:F4:3E:F0
Found Valid Match for MAC: E8:6A:64:F4:3E:F0
Found Vendor: Lcfc(HeFei) Electronics Tech Co, Ltd
Found Virtual Machine Type: Not detected
```

## Security references

This tool assumes that the API key is always provided by an environment variable.
This is the standard/best practice for automated tooling (i.e. from a source such as Hashicorp Vault).
The API key is a privileged credential and should not be cached / stored in your environment / shell history.