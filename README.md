![BrandHeader-STEM-BlackPrint.png](https://bitbucket.org/repo/b9GKML/images/1347427446-BrandHeader-STEM-BlackPrint.png)
# What is MASS? #

(Multi-Agent Spatial Simulation)

For more than the last two decades, multi-agent simulations have been highlighted to model mega-scale social or biological agents and to simulate their emergent collective behavior that may be difficult only with mathematical and macroscopic approaches. A successful key for simulating megascale agents is to speed up the execution with parallelization. Although many parallelization attempts have been made to multiagent simulations, most work has been done on shared-memory programming environments such as OpenMP, CUDA, and Global Array, or still has left several programming problems specific to distributed-memory systems, such as machine unawareness, ghost space management, and cross-processor agent management (including migration, propagation, and termination). To address these parallelization challenges, we have been developing MASS, a new parallel-computing library for multi-agent and spatial simulation over a cluster of computing nodes. MASS composes a user application of distributed arrays and multi-agents, each representing an individual simulation place or an active entity. All computation is enclosed in each array element or agent; all communication is scheduled as periodic data exchanges among those entities, using machine-independent identifiers; and agents migrate to a remote array element for rendezvousing with each other. Our unique agent-based approach takes advantage of these merits for parallelizing big data analysis using climate change and biological network motif searches as well as individual-based simulation such as neural network simulation and influenza epidemic simulation as practical application examples.

More information about MASS can be found out the University of Washington Distributed Systems Lab [Homepage](http://depts.washington.edu/dslab/MASS).

# Documentation #
You may find documentation regarding these applications in the [Wiki](https://bitbucket.org/mass_application_developers/mass_java_appl/wiki/Home). If you want to try out a version of the applications that are still in active development, clone the "develop" branch.

# Sample MASS Applications #

The projects within this repository represent several different ways that MASS can be used to solve problems. These projects are intended to be starting points for research into the use of MASS and the creation of new projects. Sub-projects (directories) within this repository contain
many applications categorized by demonstration purpose or major algorithm.

# Building The Applications #
## Overview ##
Each application is structured around [Maven](https://maven.apache.org). MASS applications take advantage of the dependency management and build functionality of Maven; Maven will need to be installed on your computer to build a properly functioning JAR. Maven is a popular tool for managing the development and maintenance lifecycle of Java applications; it is recommended that you visit the Maven home site and become familiar with its' use. In particular, check out the following topics:

* [What is Maven?](https://maven.apache.org/what-is-maven.html)
* [Build cycle overview](https://maven.apache.org/guides/introduction/introduction-to-the-lifecycle.html)
* [IDE Integration](https://maven.apache.org/ide.html)
* [POM Reference](https://maven.apache.org/pom.html) (further reading)

## Installing Maven ##
Some Java IDEs include Maven (such as [NetBeans](https://netbeans.org) and [IntelliJ IDEA](https://www.jetbrains.com/idea)), others such as [Eclipse](https://eclipse.org) require a [plugin](http://www.eclipse.org/m2e). If you decide to use an IDE plugin or native functionality, refer to IDE documentation. For Linux, check to see if there is a installation package available for your distribution. For Windows (and Linux), you may use the ZIP archive available on the Maven home site. If you plan to use Maven from the command line, test your installation using the command "mvn --version". If the installation is correct, you should see version and environment information returned by Maven. 
## Building the Applications ##
Projects are configured to build when Maven is instructed to execute the "package" build phase. If you are using an IDE plugin or built-in Maven support, refer to IDE instructions for starting the "package" phase. If you are using the command line, "mvn package" executed within the project directory will start building the application. Maven will automatically download any necessary dependencies, compile classes, and create the final JAR artifacts. JARs will be located in the "target" directory of each project; Maven will place the final JAR in this location regardless of the invocation method (IDE, plugin, or command-line).