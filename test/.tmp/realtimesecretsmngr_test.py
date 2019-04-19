import sys,os,time
sys.path.append("./deps")
sys.path.append(".")

import logging
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger("realtime-aws-secretsmngr")

from realtimeawssecretsmngr import RealTimeAwsSecretsMngr

def test_subscribe():
    secretsmngr = RealTimeAwsSecretsMngr(region="us-east-2",secretId="spil-stp-service-prod",apiId="3h5qsweuu5ebvny3q5ibu77dyi")
    def callback(secret):
        print(secret)
    secretsmngr.subscribe(callback)
    time.sleep(100)
