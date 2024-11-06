import random


def count_exact(agents,target):
    counter=0
    for agent in agents:
        if agent == target:
            counter+=1
    return counter
def count_more_than(agents,target):
    counter=0
    for agent in agents:
        if agent > target:
            counter+=1
    return counter
def num_discarded(agents):
    counter = 0
    for agent in agents:
        if agent>1:
            counter+=agent-1
    return counter
num_agents = 100000
agents = [0]*num_agents
for i in range(num_agents):
    rand_message = random.randint(0,num_agents-1)
    while rand_message == i:
        rand_message = random.randint(0,num_agents-1)
    agents[rand_message]+=1
bored = count_exact(agents,0)
single = count_exact(agents,1)
swamped = count_more_than(agents,1)
discards = num_discarded(agents)
print("bored agents: "+str(bored))
print("one message: "+str(single))
print("swamped agents: "+str(swamped))
print("discarded: "+str(discards))