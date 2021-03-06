from bsn_sdk_py.client.config import Config
from bsn_sdk_py.client.fabric_client import FabricClient
import config
import json

c = Config(
    user_code=config.user_code,
    app_code=config.app_code,
    nodeApi=config.nodeApi,
    mspDir=config.mspDir,
    httpcert=config.httpcert,
    app_public_cert_path=config.app_public_cert_path,
    user_private_cert_path=config.user_private_cert_path,
)
client = FabricClient()
client.set_config(c)


def set(data):
    res = client.req_chain_code(
        chainCode=config.chaincode,
        funcName='set', name='',
        args=[data],
        transientData={})
    printRes(res)
    return res['body']['ccRes']


def update(data):
    res = client.req_chain_code(
        chainCode=config.chaincode,
        funcName='update', name='',
        args=[data],
        transientData={})
    printRes(res)
    return res['body']['ccRes']


def delete(id):
    res = client.req_chain_code(chainCode=config.chaincode, funcName='delete',
                                args=[id])
    printRes(res)
    return res['body']['ccRes']


def get(id):
    res = client.req_chain_code(chainCode=config.chaincode, funcName='get',
                                args=[id])
    printRes(res)
    return res['body']['ccRes']


def printRes(res):
    print(res['body']['ccRes'])

