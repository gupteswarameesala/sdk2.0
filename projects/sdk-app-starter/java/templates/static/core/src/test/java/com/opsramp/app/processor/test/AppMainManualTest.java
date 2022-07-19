package com.opsramp.app.processor.test;

import com.google.gson.Gson;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.opsramp.app.processor.discovery.DiscoveryDataProcessor;
import com.opsramp.app.processor.monitor.MonitorDataProcessor;

public class AppMainManualTest {

	public static void main(String[] args) throws Exception {
		String monitorJson = "{\"templateId\":\"1c645551-f0ad-447e-b6bf-baf74910aea2\",\"template\":{\"messageId\":\"44178d4a-43fe-4005-bb1c-0bf400386d7f\",\"messageVerison\":\"2.0.0\",\"app\":\"virtualvcenter\",\"module\":\"Monitoring\",\"subtype\":\"Configuration\",\"action\":\"Update\",\"payload\":{\"templateId\":\"1c645551-f0ad-447e-b6bf-baf74910aea2\",\"nativeType\":\"vm\",\"monitors\":{\"Performance Monitor VIRTUALVCENTER host \":{\"name\":\"Performance Monitor VIRTUALVCENTER host \",\"uuid\":\"a23e64f9-3e2e-4d8d-8e04-411e37cfc42b\",\"frequency\":5,\"metrics\":{\"system_cpu_usage_utilization\":{\"availibityMetric\":false,\"units\":\"%\",\"graph\":{\"graphPoint\":\"HISTORICAL\",\"formatPlottedValue\":\"To be Filled\"},\"notification\":{\"alertOn\":\"Static\",\"raiseAlert\":false,\"formatAlertValue\":\"To be Filled\",\"limit\":\"To be Filled\",\"warn\":{\"operator\":\"GREATER_THAN\",\"value\":\"50\",\"repeat\":1},\"critical\":{\"operator\":\"GREATER_THAN\",\"value\":\"65\",\"repeat\":1}},\"dataPointConverisonOptions\":\"To be Filled\"}}}}},\"sha\":\"3356a049b8ca036207c96af0379074bab7ec68af644035f1f00717ebccb18671\"},\"monitorId\":\"a23e64f9-3e2e-4d8d-8e04-411e37cfc42b\",\"appConfig\":{\"messageId\":\"5a7c9326-ce6f-4cd4-ab26-062c8f107af1\",\"messageVerison\":\"2.0.0\",\"appIntegrationId\":\"INTG-c233a941-952a-4032-be7b-b2d63cecb60b\",\"managementProfileId\":\"babf783f-14bc-4cd9-867a-6b4deaca227c\",\"gateway\":\"babf783f-14bc-4cd9-867a-6b4deaca227c\",\"module\":\"Discovery\",\"subtype\":\"Configuration\",\"app\":\"virtualvcenter\",\"action\":\"Update\",\"configurationId\":\"ADAPTER-MANIFEST-475d5ff3-d1e9-4fd5-a4c6-e4182bf72390\",\"configurationName\":\"testing-app\",\"frequency\":30,\"payload\":{\"data\":{\"port\":\"45000\",\"ipAddress\":\"172.25.252.193\",\"vcenterName\":\"vcenter1\",\"protocol\":\"http\"},\"nativeTypes\":{\"vm\":{\"resourceType\":\"Server\"},\"host\":{\"resourceType\":\"Server\"}}},\"requireAck\":false,\"sha\":\"b45a8668db4be966c594fff40172d090c6cfa91b0864aae9bc5814dd35f797f5\"},\"nativeType\":{\"vm\":[\"system_cpu_usage_utilization\"]},\"resources\":[{\"messageId\":\"23c752a2-1ae3-4530-809e-dbe2952084a0\",\"messageVerison\":\"2.0.0\",\"module\":\"Monitoring\",\"subtype\":\"Resource\",\"action\":\"Update\",\"managementProfileId\":\"babf783f-14bc-4cd9-867a-6b4deaca227c\",\"payload\":{\"resources\":{\"resourceId\":\"9fe7e2c9-015a-43cd-8c7a-10b8092085f1\",\"moId\":\"vcenter1@host1@vm1\",\"appConfigId\":\"ADAPTER-MANIFEST-475d5ff3-d1e9-4fd5-a4c6-e4182bf72390\",\"signature\":\"to be filled\",\"templates\":[{\"templateId\":\"1c645551-f0ad-447e-b6bf-baf74910aea2\",\"app\":\"virtualvcenter\",\"nativeType\":\"vm\",\"templateCustomization\":\"to be filled\"}],\"credential\":[]}},\"sha\":\"a12c9eb873d53df29d23fc17153e005c9c4dc6391d3fbc589c39ec97051fd4f8\"}]}";
		String discJson = "  {\"messageId\":\"5e39a44b-6af2-42d6-8874-501d894fea67\",\"messageVerison\":\"2.0.0\",\"appIntegrationId\":\"INTG-269351df-6998-459f-9b5a-aae429cb87c6\",\"managementProfileId\":\"babf783f-14bc-4cd9-867a-6b4deaca227c\",\"gateway\":\"babf783f-14bc-4cd9-867a-6b4deaca227c\",\"module\":\"Discovery\",\"subtype\":\"Configuration\",\"app\":\"virtualvcenter\",\"action\":\"Update\",\"configurationId\":\"ADAPTER-MANIFEST-b85fb24c-6c07-4c17-bce8-92decbe9e010\",\"configurationName\":\"virtual-vcenter\",\"frequency\":30,\"payload\":{\"data\":{\"port\":\"45000\",\"ipAddress\":\"172.25.252.193\",\"vcenterName\":\"vcenter1\",\"protocol\":\"http\"},\"nativeTypes\":{\"vm\":{\"resourceType\":\"Server\"},\"host\":{\"resourceType\":\"Server\"}}},\"requireAck\":false,\"sha\":\"b45a8668db4be966c594fff40172d090c6cfa91b0864aae9bc5814dd35f797f5\"}";
		Gson gson = new Gson();
		var moniJsonObj = gson.fromJson(monitorJson, JsonElement.class);
		var discJsonObj = gson.fromJson(discJson, JsonElement.class);

		 JsonObject monitoringJsonObj = moniJsonObj.getAsJsonObject();
		 JsonObject discoveryJsonObjJsonObj = discJsonObj.getAsJsonObject();
        
         System.out.println("Monitoring Logs started============================\n\n");
		 MonitorDataProcessor monitor = new MonitorDataProcessor();
         monitor.processMonitoring("12345", monitoringJsonObj);
         System.out.println("Discovery Logs started============================\n\n");
		 DiscoveryDataProcessor discover = new DiscoveryDataProcessor();
         //discover.processDiscovery(discoveryJsonObjJsonObj);
	}

}
