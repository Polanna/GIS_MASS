import os, subprocess
import json

masterNode = True
containers = []
hermesCluster = False

print("This is a v2.0 script to help you generate nodes.xml for containerized MASS applications")
userInput = input("Please type 'n' if executing on one node (local machine or only one hermes node), or type 'y' for multiple nodes (multiple nodes on hermes cluster):")
if userInput == "y":
    hermesCluster = True
elif userInput == "n":
    pass
else:
    raise ValueError("Invalid input")

print("\nThe docker network name is usually in combination of your APP name with \"_default\" (e.g.: \"rangesearch_default\")")
print("If running in cluster mode, docker network name is usually in combination of your APP name with \"_cluster_default\" (e.g.: \"rangesearch_cluster_default\")")
print("\nHere is all the existing docker networks on this machine:")
docker_networks = subprocess.run(["docker network ls --format \"{{.Name}}\""], stdout=subprocess.PIPE, shell=True).stdout.decode("utf-8").split("\n")[:-1]
for i in range(len(docker_networks)):
    print("\t" + str(i) + ". " + docker_networks[i])
print("\nIf you can't find the docker network of you APP, maybe you have NOT launched containers prior to this script")

networkIndex = int(input("Please input the index number of docker network plans to use(e.g.: input 0 for " + docker_networks[0] + " ):"))
networkName = docker_networks[networkIndex]

# obtain containers' name for every agent
if hermesCluster:
    print("\nHere is all the existing docker services on this machine:")
    docker_services = subprocess.run(["docker service ls --format \"{{.Name}}\""], stdout=subprocess.PIPE, shell=True).stdout.decode("utf-8").split("\n")[:-1]
    for i in range(len(docker_services)):
        print("\t" + str(i) + ". " + docker_services[i])
    serviceIndex = int(input("Please input the the index number of docker service plans to use:"))
    serviceName = docker_services[serviceIndex]
    print("Setteing up environment on multiple nodes is slow, please wait......")
    result = subprocess.run(["docker network inspect " + networkName], stdout=subprocess.PIPE, shell=True).stdout
    output = json.loads(result)
    peers = list(output[0]["Peers"])
    IPs = [i["IP"] for i in peers]
    print(IPs)

    for ip in IPs:
        sub_result = subprocess.run(["ssh " + ip + " docker network inspect " + networkName], stdout=subprocess.PIPE, shell=True).stdout.decode("utf-8")
        output = json.loads(sub_result)
        containers += [i["Name"] for i in list(output[0]["Containers"].values())[:-1]]
else:
    result = subprocess.run(["docker network inspect " + networkName], stdout=subprocess.PIPE, shell=True)
    output = json.loads(result.stdout)
    containerNetwork = list(output[0]["Containers"].values())
    containers = [i["Name"] for i in containerNetwork]

containerNames = sorted(containers)
print(containerNames)

# create the nodes.xml
with open("resources/nodes.xml", "w") as writer:
    writer.write("<nodes>\n")
    for containerName in containerNames:
        writer.write("\t<node>\n")
        writer.write("\t\t<hostname>" + containerName + "." + networkName + "</hostname>\n")
        if masterNode:
            writer.write("\t\t<master>true</master>\n")
            masterNode = False
        writer.write("\t\t<masshome>/app/build/libs</masshome>\n")
        writer.write("\t\t<javahome>${JAVA_HOME}/bin</javahome>\n")
        writer.write("\t\t<username>root</username>\n")
        writer.write("\t\t<privatekey>/root/.ssh/id_rsa</privatekey>\n")
        writer.write("\t</node>\n")
    writer.write("</nodes>\n")
print("Generated resources/nodes.xml with " + str(len(containerNames)) + " nodes")



# print out helping instructions
if hermesCluster:
    # find out the node hosting the master agent
    result = str(subprocess.run(["docker service ps " + serviceName + " | grep " + serviceName + ".1"], stdout=subprocess.PIPE, shell=True).stdout.decode("utf-8"))
    startIndex = result.find("hermes")
    mainNode = result[startIndex:startIndex + len("hermes00")]
    print("First, please use command below to connect to the node that is hosting the master node")
    print("\tssh " + mainNode)
    print("Then, please use command below to attach to the master container")
else:
    print("Please use command below to attach to the master container")
print("\tdocker exec -it " + containerNames[0] + " bash")