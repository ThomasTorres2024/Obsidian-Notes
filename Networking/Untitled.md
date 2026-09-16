# Overview 

### Network Protocols
A standard by which devices can send and receive messages over some standard. Protocols define a __format__ and __order__ of messages sent and received among network entities, and the __actions taken__ on message transmissions. Receiving a message from another machine will principally change the state of a state machine, hence the actions taken portion. 

### Infrastructure
Provides services to applications. 

### Programming Interface
* hooks which allow t

### Network Edge 
Hosts consist of servers, and clients consist of machines that make requests to servers. For instance, querying an LLM on the web from a laptop makes a request to the external machine on the server. Servers have to handle significant amounts of data processing and are thus typically hosted in data centers. 

### Access Networks, Physical Media
Consists of wired and wireless communication links. Contains host networks and local network. 

### Network Core 
Interconnected routers. Network of routers. 

Hosts need to connect to an access network. An access network then feeds into each access network since it connects to each router or network service and is thus a network of networks. 

### Hosts: Sends packets of data
A host takes some application message, consisting of $L$ bits and transmits it across the network. Packets are transmitted into the access network at transmission rate $R$. The link transmission rate, also __link capacity__/__link bandwidth__ is typically a constant for the total number of bits that can be sent across from a host into an access network. The transmission rate, $R$ the number of bits per second gives roughly the amount of delay:

$$\text{delay secs} = \frac{L \text{ (bits)} }{R \text{ (bits/sec)} }$$
### Wireless access networks
Wireless networks that connects hosts to 

### Links: 
* Bits propagate between transmitter and receiver pairs 
* Physical link, lies between transmitter and receiver
* Guided media: signals propagate in solid media
* unguided media signal propagate freely

## The Network Core -
* Mesh of interconnect routers
* Host break application layer message into packets
	* Forward packets from one router to the next across links on path from source to destination
	* Each packet transmitted at full link capacity 

* Transmission delay, $\frac{L}{R}$
	* Ex $L=10 kbits$,$R=100 Mbps$, $\frac{10 \cdot 10^3}{100 \cdot 10^6 } = 10^{-4}s$
* Store and forward, entire packet must at router before it can be transmitted on next link 
* End-end delay: $\frac{2L}{R}$ assuming zero propagation delay 

### Packet-switching queueing delay loss
- If arrival rate in bps to link exceeds bps of link for a period of time:
	- packets will queue waiting to be transmitted to an output link 
	- router has finite space, if router wills up packets are dropped (lost), otherwise there is just a queue we need to wait for, generally queueing delay doesn't have a good estimation 

### Two Key Network Core Functions
*  We are interested in finding the shortest route inbetween network devices in order to transmit packages 
* Forwarding: local action moving packets from input to approprisate output link
* Routing is a more global action, we try to determine a source-destination path taken by packets 

### Alternative to packet switchingm circuit switching
* 