import connexion
import six
import json

from swagger_server.models.problem_details import ProblemDetails  # noqa: E501
from swagger_server.models.sm_policy_context_data import SmPolicyContextData  # noqa: E501
from swagger_server.models.sm_policy_control import SmPolicyControl  # noqa: E501
from swagger_server.models.sm_policy_decision import SmPolicyDecision  # noqa: E501
from swagger_server.models.sm_policy_delete_data import SmPolicyDeleteData  # noqa: E501
from swagger_server.models.sm_policy_update_context_data import SmPolicyUpdateContextData  # noqa: E501
from swagger_server import util


def sm_policies_post(body):  # noqa: E501
    """sm_policies_post

     # noqa: E501

    :param body:
    :type body: dict | bytes

    :rtype: SmPolicyDecision
    """
    if connexion.request.is_json:
        body = SmPolicyContextData.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def sm_policies_sm_policy_id_delete_post(body, sm_policy_id):  # noqa: E501
    """sm_policies_sm_policy_id_delete_post

     # noqa: E501

    :param body:
    :type body: dict | bytes
    :param sm_policy_id: Identifier of a policy association
    :type sm_policy_id: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = SmPolicyDeleteData.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def sm_policies_sm_policy_id_get(sm_policy_id):  # noqa: E501
    """sm_policies_sm_policy_id_get

     # noqa: E501

    :param sm_policy_id: Identifier of a policy association
    :type sm_policy_id: str

    :rtype: SmPolicyControl
    """
    return {"context":{"accNetChId":{"accNetChaIdValue":0,"refPccRuleIds":["string"],"sessionChScope":True},"chargEntityAddr":{"anChargIpv4Addr":"198.51.100.1","anChargIpv6Addr":"2001:db8:85a3::8a2e:370:7334"},"gpsi":"string","supi":"string","interGrpIds":["string"],"pduSessionId":0,"chargingcharacteristics":"string","dnn":"string","notificationUri":"string","accessType":"3GPP_ACCESS","servingNetwork":{"mnc":"string","mcc":"string"},"userLocationInfo":{"eutraLocation":{"tai":{"plmnId":{"mcc":"string","mnc":"string"},"tac":"string"},"ecgi":{"plmnId":{"mcc":"string","mnc":"string"},"eutraCellId":"string"},"ageOfLocationInformation":0,"ueLocationTimestamp":"2019-07-23T17:08:08.481Z","geographicalInformation":"string","geodeticInformation":"string","globalNgenbId":{"plmnId":{"mcc":"string","mnc":"string"},"n3IwfId":"string","gNbId":{"bitLength":0,"gNBValue":"string"},"ngeNbId":"string"}},"nrLocation":{"tai":{"plmnId":{"mcc":"string","mnc":"string"},"tac":"string"},"ncgi":{"plmnId":{"mcc":"string","mnc":"string"},"nrCellId":"string"},"ageOfLocationInformation":0,"ueLocationTimestamp":"2019-07-23T17:08:08.481Z","geographicalInformation":"string","geodeticInformation":"string","globalGnbId":{"plmnId":{"mcc":"string","mnc":"string"},"n3IwfId":"string","gNbId":{"bitLength":0,"gNBValue":"string"},"ngeNbId":"string"}},"n3gaLocation":{"n3gppTai":{"plmnId":{"mcc":"string","mnc":"string"},"tac":"string"},"n3IwfId":"string","ueIpv4Addr":"198.51.100.1","ueIpv6Addr":"2001:db8:85a3::8a2e:370:7334","portNumber":0}},"ueTimeZone":"string","pei":"string","ipv4Address":"198.51.100.1","ipv6AddressPrefix":"2001:db8:abcd:12::0\/64","ipDomain":"string","subsSessAmbr":{"uplink":"string","downlink":"string"},"subsDefQos":{"5qi":0,"arp":{"priorityLevel":0},"priorityLevel":0},"numOfPackFilter":0,"online":True,"offline":True,"3gppPsDataOffStatus":True,"refQosIndication":True,"traceReq":{"traceRef":"string","neTypeList":"string","eventList":"string","collectionEntityIpv4Addr":"198.51.100.1","collectionEntityIpv6Addr":"2001:db8:85a3::8a2e:370:7334","interfaceList":"string"},"sliceInfo":{"sst":0,"sd":"string"},"servNfId":{"servNfInstId":"3fa85f64-5717-4562-b3fc-2c963f66afa6","guami":{"plmnId":{"mcc":"string","mnc":"string"},"amfId":"string"},"anGwAddr":{"anGwIpv4Addr":"198.51.100.1","anGwIpv6Addr":"2001:db8:85a3::8a2e:370:7334"}},"suppFeat":"string","smfId":"3fa85f64-5717-4562-b3fc-2c963f66afa6","recoveryTime":"2019-07-23T17:08:08.481Z"},"policy":{"sessRules":{"additionalProp1":{"authSessAmbr":{"uplink":"string","downlink":"string"},"authDefQos":{"5qi":0,"arp":{"priorityLevel":0},"priorityLevel":0,"averWindow":0,"maxDataBurstVol":0},"sessRuleId":"string","refUmData":"string","refCondData":"string"},"additionalProp2":{"authSessAmbr":{"uplink":"string","downlink":"string"},"authDefQos":{"5qi":0,"arp":{"priorityLevel":0},"priorityLevel":0,"averWindow":0,"maxDataBurstVol":0},"sessRuleId":"string","refUmData":"string","refCondData":"string"},"additionalProp3":{"authSessAmbr":{"uplink":"string","downlink":"string"},"authDefQos":{"5qi":0,"arp":{"priorityLevel":0},"priorityLevel":0,"averWindow":0,"maxDataBurstVol":0},"sessRuleId":"string","refUmData":"string","refCondData":"string"}},"pccRules":{"additionalProp1":{"flowInfos":[{"flowDescription":"string","ethFlowDescription":{"destMacAddr":"string","ethType":"string","fDesc":"string","sourceMacAddr":"string","vlanTags":["string"]},"packFiltId":"string","packetFilterUsage":True,"tosTrafficClass":"string","spi":"string","flowLabel":"string"}],"appId":"string","contVer":0,"pccRuleId":"string","precedence":0,"appReloc":True,"refQosData":["string"],"refTcData":["string"],"refChgData":["string"],"refUmData":["string"],"refCondData":"string"},"additionalProp2":{"flowInfos":[{"flowDescription":"string","ethFlowDescription":{"destMacAddr":"string","ethType":"string","fDesc":"string","sourceMacAddr":"string","vlanTags":["string"]},"packFiltId":"string","packetFilterUsage":True,"tosTrafficClass":"string","spi":"string","flowLabel":"string"}],"appId":"string","contVer":0,"pccRuleId":"string","precedence":0,"appReloc":True,"refQosData":["string"],"refTcData":["string"],"refChgData":["string"],"refUmData":["string"],"refCondData":"string"},"additionalProp3":{"flowInfos":[{"flowDescription":"string","ethFlowDescription":{"destMacAddr":"string","ethType":"string","fDesc":"string","sourceMacAddr":"string","vlanTags":["string"]},"packFiltId":"string","packetFilterUsage":True,"tosTrafficClass":"string","spi":"string","flowLabel":"string"}],"appId":"string","contVer":0,"pccRuleId":"string","precedence":0,"appReloc":True,"refQosData":["string"],"refTcData":["string"],"refChgData":["string"],"refUmData":["string"],"refCondData":"string"}},"pcscfRestIndication":True,"qosDecs":{"additionalProp1":{"qosId":"string","5qi":0,"maxbrUl":"string","maxbrDl":"string","gbrUl":"string","gbrDl":"string","arp":{"priorityLevel":0},"qnc":True,"priorityLevel":0,"averWindow":0,"maxDataBurstVol":0,"reflectiveQos":True,"sharingKeyDl":"string","sharingKeyUl":"string","maxPacketLossRateDl":0,"maxPacketLossRateUl":0,"defQosFlowIndication":True},"additionalProp2":{"qosId":"string","5qi":0,"maxbrUl":"string","maxbrDl":"string","gbrUl":"string","gbrDl":"string","arp":{"priorityLevel":0},"qnc":True,"priorityLevel":0,"averWindow":0,"maxDataBurstVol":0,"reflectiveQos":True,"sharingKeyDl":"string","sharingKeyUl":"string","maxPacketLossRateDl":0,"maxPacketLossRateUl":0,"defQosFlowIndication":True},"additionalProp3":{"qosId":"string","5qi":0,"maxbrUl":"string","maxbrDl":"string","gbrUl":"string","gbrDl":"string","arp":{"priorityLevel":0},"qnc":True,"priorityLevel":0,"averWindow":0,"maxDataBurstVol":0,"reflectiveQos":True,"sharingKeyDl":"string","sharingKeyUl":"string","maxPacketLossRateDl":0,"maxPacketLossRateUl":0,"defQosFlowIndication":True}},"chgDecs":{"additionalProp1":{"chgId":"string","offline":True,"online":True,"sdfHandl":True,"ratingGroup":0,"serviceId":0,"sponsorId":"string","appSvcProvId":"string","afChargingIdentifier":0},"additionalProp2":{"chgId":"string","offline":True,"online":True,"sdfHandl":True,"ratingGroup":0,"serviceId":0,"sponsorId":"string","appSvcProvId":"string","afChargingIdentifier":0},"additionalProp3":{"chgId":"string","offline":True,"online":True,"sdfHandl":True,"ratingGroup":0,"serviceId":0,"sponsorId":"string","appSvcProvId":"string","afChargingIdentifier":0}},"chargingInfo":{"primaryChfAddress":"string","secondaryChfAddress":"string"},"traffContDecs":{"additionalProp1":{"tcId":"string","redirectInfo":{"redirectEnabled":True,"redirectServerAddress":"string"},"muteNotif":True,"trafficSteeringPolIdDl":"string","trafficSteeringPolIdUl":"string","routeToLocs":[None,None],"upPathChgEvent":{"notificationUri":"string","notifCorreId":"string"}},"additionalProp2":{"tcId":"string","redirectInfo":{"redirectEnabled":True,"redirectServerAddress":"string"},"muteNotif":True,"trafficSteeringPolIdDl":"string","trafficSteeringPolIdUl":"string","routeToLocs":[None,None],"upPathChgEvent":{"notificationUri":"string","notifCorreId":"string"}},"additionalProp3":{"tcId":"string","redirectInfo":{"redirectEnabled":True,"redirectServerAddress":"string"},"muteNotif":True,"trafficSteeringPolIdDl":"string","trafficSteeringPolIdUl":"string","routeToLocs":[None,None],"upPathChgEvent":{"notificationUri":"string","notifCorreId":"string"}}},"umDecs":{"additionalProp1":{"umId":"string","volumeThreshold":0,"volumeThresholdUplink":0,"volumeThresholdDownlink":0,"timeThreshold":0,"monitoringTime":"2019-07-23T17:08:08.482Z","nextVolThreshold":0,"nextVolThresholdUplink":0,"nextVolThresholdDownlink":0,"nextTimeThreshold":0,"inactivityTime":0,"exUsagePccRuleIds":["string"]},"additionalProp2":{"umId":"string","volumeThreshold":0,"volumeThresholdUplink":0,"volumeThresholdDownlink":0,"timeThreshold":0,"monitoringTime":"2019-07-23T17:08:08.482Z","nextVolThreshold":0,"nextVolThresholdUplink":0,"nextVolThresholdDownlink":0,"nextTimeThreshold":0,"inactivityTime":0,"exUsagePccRuleIds":["string"]},"additionalProp3":{"umId":"string","volumeThreshold":0,"volumeThresholdUplink":0,"volumeThresholdDownlink":0,"timeThreshold":0,"monitoringTime":"2019-07-23T17:08:08.482Z","nextVolThreshold":0,"nextVolThresholdUplink":0,"nextVolThresholdDownlink":0,"nextTimeThreshold":0,"inactivityTime":0,"exUsagePccRuleIds":["string"]}},"qosChars":{"additionalProp1":{"5qi":0,"priorityLevel":0,"packetDelayBudget":0,"packetErrorRate":"string","averagingWindow":0,"maxDataBurstVol":0},"additionalProp2":{"5qi":0,"priorityLevel":0,"packetDelayBudget":0,"packetErrorRate":"string","averagingWindow":0,"maxDataBurstVol":0},"additionalProp3":{"5qi":0,"priorityLevel":0,"packetDelayBudget":0,"packetErrorRate":"string","averagingWindow":0,"maxDataBurstVol":0}},"reflectiveQoSTimer":0,"conds":{"additionalProp1":{"condId":"string","activationTime":"2019-07-23T17:08:08.482Z","deactivationTime":"2019-07-23T17:08:08.482Z"},"additionalProp2":{"condId":"string","activationTime":"2019-07-23T17:08:08.482Z","deactivationTime":"2019-07-23T17:08:08.482Z"},"additionalProp3":{"condId":"string","activationTime":"2019-07-23T17:08:08.482Z","deactivationTime":"2019-07-23T17:08:08.482Z"}},"revalidationTime":"2019-07-23T17:08:08.482Z","offline":True,"online":True,"policyCtrlReqTriggers":["PLMN_CH","string"],"lastReqRuleData":[{"refPccRuleIds":["string"],"reqData":["CH_ID","string"]}],"lastReqUsageData":{"refUmIds":["string"],"allUmIds":True},"praInfos":{"additionalProp1":{"praId":"string","trackingAreaList":[{"plmnId":{"mcc":"string","mnc":"string"},"tac":"string"}],"ecgiList":[{"plmnId":{"mcc":"string","mnc":"string"},"eutraCellId":"string"}],"ncgiList":[{"plmnId":{"mcc":"string","mnc":"string"},"nrCellId":"string"}],"globalRanNodeIdList":[None,None,None]},"additionalProp2":{"praId":"string","trackingAreaList":[{"plmnId":{"mcc":"string","mnc":"string"},"tac":"string"}],"ecgiList":[{"plmnId":{"mcc":"string","mnc":"string"},"eutraCellId":"string"}],"ncgiList":[{"plmnId":{"mcc":"string","mnc":"string"},"nrCellId":"string"}],"globalRanNodeIdList":[None,None,None]},"additionalProp3":{"praId":"string","trackingAreaList":[{"plmnId":{"mcc":"string","mnc":"string"},"tac":"string"}],"ecgiList":[{"plmnId":{"mcc":"string","mnc":"string"},"eutraCellId":"string"}],"ncgiList":[{"plmnId":{"mcc":"string","mnc":"string"},"nrCellId":"string"}],"globalRanNodeIdList":[None,None,None]}},"ipv4Index":0,"ipv6Index":0,"suppFeat":"string"}}


def sm_policies_sm_policy_id_update_post(body, sm_policy_id):  # noqa: E501
    """sm_policies_sm_policy_id_update_post

     # noqa: E501

    :param body:
    :type body: dict | bytes
    :param sm_policy_id: Identifier of a policy association
    :type sm_policy_id: str

    :rtype: SmPolicyDecision
    """
    if connexion.request.is_json:
        body = SmPolicyUpdateContextData.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
