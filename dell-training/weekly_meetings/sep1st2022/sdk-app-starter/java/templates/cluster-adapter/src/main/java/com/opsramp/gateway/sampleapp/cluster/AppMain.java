package com.opsramp.gateway.{{res}}.cluster;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import com.opsramp.gateway.common.configuration.AppConfiguration;
import com.opsramp.gateway.common.core.ApplicationInitiator;



public class AppMain extends ApplicationInitiator {
	private static final Logger LOG = LoggerFactory.getLogger(AppMain.class.getName());

	public static void main(String[] args) throws Exception {
		LOG.trace("App Main method started.");

		try {
			AppConfiguration appConfiguration = AppMainUtil.appBuilderProcess();
			LOG.trace("Registration of App  started...");
			register(appConfiguration);
		} catch (Exception e) {
			LOG.error("Failed to register App", e);
			System.exit(1);
		}
	}
}