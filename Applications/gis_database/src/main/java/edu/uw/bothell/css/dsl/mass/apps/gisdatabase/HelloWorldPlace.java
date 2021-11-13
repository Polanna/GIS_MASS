package edu.uw.bothell.css.dsl.mass.apps.gisdatabase;

import java.net.InetAddress;
import java.net.UnknownHostException;
import java.util.Arrays;

import edu.uw.bothell.css.dsl.MASS.Place;

public class HelloWorldPlace extends Place{

	@Override
	public Object callMethod(int functionId, Object argument) {
		// TODO Auto-generated method stub
		return hello (argument);
	}
	
	public Object hello (Object args) {
	    try {
			String hostname = InetAddress.getLocalHost().getHostName();
			return "Hello from " + Arrays.toString(this.getIndex()) + " on " + hostname;
		} catch (UnknownHostException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			return "Hello from " + Arrays.toString(this.getIndex());
		}		
	}

}
