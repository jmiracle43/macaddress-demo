import getopt
import os
import requests
import sys


def main(argv):
    mac, opts, args = '', [], []
    api_key = read_api_key()
    try:
        opts, args = getopt.getopt(argv[1:], "hm:", "mac=")
    except getopt.GetoptError:
        program_help()
        exit(1)
    for opt, arg in opts:
        if opt == '-h':
            program_help()
        elif opt in ('-m', '--mac'):
            mac = arg
    call_macaddress_io(mac, api_key)


def read_api_key():
    if os.environ["MAC_API_KEY"]:
        return os.environ["MAC_API_KEY"]
    else:
        program_help()
        exit(1)


def call_macaddress_io(mac_address, api_key):
    r = requests.get(f'https://api.macaddress.io/v1?apiKey={api_key}&output=json&search={mac_address}')
    if r.status_code == 200:
        j = r.json()
        print("Found Valid Match for MAC: %s" % j['macAddressDetails']['searchTerm'])
        print("Found Vendor: %s" % j['vendorDetails']['companyName'])
        print("Found Virtual Machine Type: %s" % j['macAddressDetails']['virtualMachine'])
    elif r.status_code == 400:
        print("Internal error: Invalid parameters submitted to MACAddress.io during query.")
        exit(1)
    elif r.status_code == 401:
        print("Invalid API Key detected during search.")
        program_help()
        exit(1)
    elif r.status_code == 402:
        print("Access Denied from MACAddress.io, API daily limit exceeded.")
        exit(1)
    elif r.status_code == 422:
        print("Invalid MAC address submitted during query.")
        program_help()
        exit(1)
    elif r.status_code == 429:
        print("MACAddress.io service is busy, attempt query later.")
        exit(1)
    elif r.status_code == 500:
        print("MACAddress.io encounted an internal error, attempt later or contact support.")
        exit(1)


def program_help():
    print("MAC_API_KEY=<api_key> ./run.sh -m <mac-address>")


if __name__ == '__main__':
    main(argv=sys.argv)
