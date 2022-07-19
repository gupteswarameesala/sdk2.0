package com.opsramp.gateway.{{res}}.cluster;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import com.opsramp.gateway.common.listener.LogProcessor;

import ch.qos.logback.classic.Level;

public class AppLogProcessor implements LogProcessor{
	private static final Logger LOG = LoggerFactory.getLogger(AppLogProcessor.class.getName());

	@Override
	public boolean changeLogLevel(String level) {
		try {
			LOG.debug("App Log level is changing started to :{} ", level);
			ch.qos.logback.classic.Logger rootLogger = (ch.qos.logback.classic.Logger) LoggerFactory
					.getLogger(ch.qos.logback.classic.Logger.ROOT_LOGGER_NAME);
			if (level.equals("INFO")) {
				rootLogger.setLevel(Level.toLevel("INFO"));
			} else if (level.equals("DEBUG")) {
				rootLogger.setLevel(Level.toLevel("DEBUG"));
			} else if (level.equals("ERROR")) {
				rootLogger.setLevel(Level.toLevel("ERROR"));
			}
			LOG.info("App Log level is changed to :{} ", level);
			LOG.debug("App Log level is changed to :{} ", level);
			LOG.error("App Log level is changed to :{} ", level);

			return true;
		} catch (Exception e) {
			LOG.debug("Failed to change App Log level to :{}", level);
			e.printStackTrace();
			return false;
		}
	}

}
