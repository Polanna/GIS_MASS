package edu.uw.bothell.css.dsl.mass.apps.gisdatabase;

import edu.uw.bothell.css.dsl.MASS.MASS;
import edu.uw.bothell.css.dsl.MASS.Places;
import edu.uw.bothell.css.dsl.MASS.logging.LogLevel;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        MASS.init();
        MASS.setLoggingLevel(LogLevel.DEBUG);
        
        System.out.println("MASS initialized");
        
        System.out.println("Attempting to create places...");
        Places places = new Places(1, HelloWorldPlace.class.getName(), null, 10, 10);
        System.out.println("Created Places!");
        
        Object[] results = places.callAll(0, null);
        MASS.getLogger().debug("callAll");
        System.out.println("callAll:" + results.length);
        
        for (Object obj : results)
        {
        	System.out.println(obj);
        }
        
        MASS.finish();
    }
}
