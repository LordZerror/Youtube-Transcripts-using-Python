# Distributed Computing Module - 1

- Advancements in tech (fast, inexpensive processors) and communication tech (cost effective efficient, computer network) have lead to **Interconnected Multiple Processors**
    - Interconnected multiple processors :
        1. Tightly coupled systems :
            1. Single system wide memory (primary)
            2. Also called parallel processing system
        2. Loosely coupled systems :
            1. No sharing of memory.
            2. Each processors has its own local memory.
            3. Also called **DISTRIBUTED SYSTEM**
- **Distributed computing** is a field of computer science that studies distributed systems
    - A distributed system is one that appears to its users like an ordinary centralized system but runs on multiple , independent CPUs.
    - The key concept is TRANSPERANCY.
    - The use of multiple processors should be invisible (transparent) to the user.
    - The users view the system as a virtual uniprocessor and not a collection of distinct machines.
    - A distributed system is one that appears to its users like an ordinary centralized system but runs on multiple , independent CPUs.
    - This definition has 2 aspects :
        - The first one deals with software : the users think they are dealing with a single system.
        - The second one deals with hardware : runs on multiple independent  CPUs.
    - Eg of a distributed system –World wide web
- **Characteristics**
    - Consists of several computers that do not share memory.
    - Communication – Exchanging messages.
    - Each computer has its own memory and its own OS.
    - Resources owned and controlled by a computer are said to be local to it. While resources owned and controlled by other computers are said to be remote to it.
- **Example**
    - **SETI (Search for Extraterrestrial Intelligence) @Home project**
    - SETI@home is a scientific experiment that uses Internet-connected computers in the Search for Extraterrestrial Intelligence (SETI).
    - You can participate by running a free program that downloads and analyzes radio telescope data.
    - Data is recorded at the Arecibo Observatory in Puerto Rico.
    - The data is digitized, stored, and sent to the SETI@home serverat Berkeley. The data is then parsed into small chunks ,where it is processed into units of 107 seconds of data.

### Difference between a Computer Network and Distributed System

**Computer Network**

- User job is executed on the m/c where the user is currently logged.
- If a job has to be executed on a different m/c
    - either log onto that machine explicitly
    - or use remote login command.
- Thus, the user knows the machine on which the job is executed.
- User is required to know the location of a resource to access it.

**Distributed System**

- Jobs are automatically and dynamically allocated to the machines for processing.
- Thus, the user has no knowledge of the machine on which the job is executed.
- Users need not keep track of the location of various resources for accessing them.

---

## Cluster and Grid Computing

### **Cluster Computing**

- A Computer Cluster is a local network of two or more homogeneous computers.
- Computation on such a cluster is known as cluster computing

![Screenshot 2024-02-13 at 2.46.56 AM.png](Distributed%20Computing%20Module%20-%201%20acb1d860c38141298568053fdf69a861/Screenshot_2024-02-13_at_2.46.56_AM.png)

- It is used for parallel programming in which a single (compute intensive) program is run in parallel on multiple machines
- Well-known example of a cluster computer is formed by **Linux**-based Beowulf clusters, the general configuration of it is shown in
- Each cluster consists of a collection of compute nodes that are controlled and accessed by means of a single **master** node
- The master typically handles
    - the allocation of nodes to a   particular parallel program
    - maintains a batch queue of submitted jobs
    - provides an interface for the users of the system
- Master actually runs  middleware needed for  execution of programs and management of the cluster
- Important part of middleware is formed by the **libraries** for executing parallel programs

### **Grid Computing**

![Screenshot 2024-02-13 at 2.58.43 AM.png](Distributed%20Computing%20Module%20-%201%20acb1d860c38141298568053fdf69a861/Screenshot_2024-02-13_at_2.58.43_AM.png)

- A grid is a distributing computing architecture that connects a network of computers to form an on-demand robust network. A network of computers utilizes grid computing to solve complex problems.
- Grid Computing can be defined as a network of homogeneous or heterogeneous computers working together over a long distance to perform a task that would rather be difficult for a single machine.
- A characteristic feature of **cluster** computing is its **homogeneity.** In contrast, **grid computing** systems have a high degree of **heterogeneity**
- No assumptions are made concerning hardware, operating systems, networks, administrative domains, security policies, etc****
- An architecture of **grid system** proposed by Foster is shown as the architecture consists of four layers.
1. ***Fabric Layer***
    1. The lowest ***fabric layer*** provides interfaces to local resources at a specific site
    2. Interfaces will provide functions for querying the state and capabilities of a resource, along with functions for actual resource management
2. ***Connectivity Layer***
    1. The ***connectivity layer*** consists of communication protocols for  supporting grid transactions that span the usage of multiple resources For example, protocols are needed to transfer data between resources, or to simply access a resource from a remote location
    2. In addition, the connectivity layer will contain security protocols to authenticate users and resources
3. ***Resource Layer***
    1. The ***resource layer*** is responsible for managing a single resource
    2. It uses functions provided by  connectivity layer and calls directly the interfaces made available by the fabric layer
    3. For example, this layer will offer functions for obtaining configuration information on a specific resource, or, in general, to perform specific operations such as creating a process or reading data
    4. The resource layer is thus seen to be responsible for access control, and hence will rely on the authentication performed as part of the connectivity layer
4. ***Collective Layer***
    1. The ***collective layer*** deals with handling access to multiple resources and consists of services for resource discovery, allocation and scheduling of tasks onto multiple resources, data replication, and so on.
    2. Collective layer may consist of many different protocols for many different purposes
5. ***Application Layer***
    1. Finally, the ***application layer*** consists of the applications that operate within a virtual organization and which make use of the grid computing environment

| Cluster Computing | Grid Computing |
| --- | --- |
| Nodes are homogeneous i.e. they should have same type of hardware and operating system. | Nodes may have different Operating systems and hardware. Machines can be homogeneous or heterogeneous. |
| Same processes run on all computers over the cluster at the same time. | Job is divided into sub-jobs each is assigned to an idle CPU so they all run concurrently. |
| Computers are located close to each other. | Computers may be located at a huge distance from one another. |
| Computers are connected by a high speed LAN bus. | Computers are connected using a low speed bus or the internet. |
| Computers are connected in a centralized network topology | Computers are connected in a distributed or de-centralized network topology.
 |
| Eg : Sony PlayStation clusters | Dropbox, Gmail |

---

## Goals of Distributed System

- Important goals that should be met to make building a distributed system worth the effort.
- A distributed system
    - should make resources **easily accessible**;
    - it should reasonably **hide the fact** that resources are distributed across a network; **distribution transparency**
    - it should be **open**;
    - it should be **scalable**

### Easily Accessible

- The main goal of a distributed system is to make it easy for the users (and applications) to access remote resources, and to share them in a controlled and efficient way
- Resources can be just about anything, but typical examples include things like printers, computers, storage facilities, data, files, Web pages, and networks

### **Distribution transparency**

- An important goal of a distributed system is to hide the fact that its processes and resources are physically distributed across multiple computers
- A distributed system that is able to present itself to users and applications as if it were only a single computer system is said to be **transparent**
- **Types of Transparency**

![Untitled](Distributed%20Computing%20Module%20-%201%20acb1d860c38141298568053fdf69a861/Untitled.png)

### **Openness**

- An **open distributed** system is a system that offers services according to standard rules that describe the syntax and semantics of those services
- For example, in computer networks, standard rules govern the format, contents, and meaning of messages sent and received
- Such rules are formalized in protocols. In distributed systems services are generally specified through interfaces, which are often described in an **Interface Definition Language (IDL)**

### **Scalability**

- Scalability of a system can be measured along at least three different dimensions (Neuman, 1994)
1. First, a system can be scalable with respect to its size, meaning that we can easily add more users and resources to the system
2. Second, a geographically scalable system is one in which the users and resources may lie far apart
3. Third, a system can be administratively scalable, meaning that it can still be easy to manage even if it spans many independent administrative organizations

## Design Issues - TRFPSHS = TuRF Pe Sherlock HolmeS

### **Transparency: - CALF MiRRor**

1. **Concurrency Transparency:**
    1. It hides the fact that the resource may be shared by several competitive users
    2. Example, two independent users may each have stored their file on the same server and may be accessing the same table in a shared database
    3. In such cases, it is important that each user doesn’t notice that the others are making use of the same resource
2. **Access Transparency:**
    1. It hides differences in data representation and how a resource is accessed by a user
    2. Example, a distributed system may have a computer system that runs different operating systems, each having their own file naming conventions
    3. Differences in naming conventions as well as how files can be manipulated should be hidden from the users and applications
3. **Location Transparency:**
    1. Hides where exactly the resource is located physically
    2. Example, by assigning logical names to resources like **yahoo.com**, one cannot get an idea of the location of the web page’s main server
4. **Failure Transparency:**
    1. Hides failure and recovery of the resources
    2. It is the most difficult task of a distributed system and is even impossible when certain apparently realistic assumptions are made Example: A user cannot distinguish between a very slow or dead resource
    3. Same error message come when a server is down or when the network is overloaded of when the connection from the client side is lost
    4. So here, the user is unable to understand what has to be done, either the user should wait for the network to clear up, or try again later when the server is working again
5. **Migration Transparency:**
    1. Distributed system in which resources can be moved without affecting how the resource can be accessed are said to provide migration transparency
    2. It hides that the resource may move from one location to another
6. **Relocation Transparency:**
    1. This transparency deals with the fact that resources can be relocated while it is being accessed without the user who is using the application to know anything
    2. Example: using a Wi-Fi system on laptops while moving from place to place without getting disconnected
7. **Replication Transparency:**
    1. Hides the fact that multiple copies of a resource could exist simultaneously
    2. To hide replication, it is essential that the replicas have the same name

### **RELIABILITY**

- Distributed systems are expected to be more reliable than centralized systems due to the existence of multiple instances of resources
- However, the existence of multiple instances of the resources alone cannot increase the system’s reliability
- Distributed system, which manages these resources must be designed properly to increase the system’s reliability by taking full advantage of this characteristic feature of a distributed system
- For higher reliability, the fault-handling mechanisms of a distributed system must be designed properly to avoid faults, to tolerate faults, and to detect and recover form faults

### **FLEXIBILITY - EME**

- Flexibility is the most important features for distributed systems
- The design of a distributed operating system should be flexible due to the following reasons :
    1. **Ease of modification :**
        1. It has been found that some parts of the design often need to be replaced / modified either because some bug is detected in the design or because the design is no longer suitable for the changed system environment or new-user requirements
        2. Therefore, it should be easy to incorporate changes in the system in a user-transparent manner or with minimum interruption caused to the users
    2. **Ease of enhancement :**
        1. New functionalities have to be added from time to time it more powerful and easy to use. Therefore, it should be easy to add new services to the system
        2. If a group of users do not like the style in which a particular service is provided by the system, they should have the flexibility to add and use their own service that works in the style with which the users of that group are more familiar and feel more comfortable

### **PERFORMANCE - BC MMT**

- If a distributed system is to be used its performance must be at least as good as a centralized system
- Some design principles considered useful for better performance are as follows :
    - **Batch if possible**
        - Batching often helps in improving performance greatly
        - For example, transfer of data across the network in large chunks rather than as individual pages is much more efficient
    - **Cache whenever possible :**
        - Caching of data at clients’ sites frequently improves overall system performance because it makes data available wherever it is being currently used, thus saving a large amount of computing time and network bandwidth
    - **Minimize copying of data :**
        - Data copying overhead (e.g. moving data in and out of buffers) involves a substantial CPU cost of many operations
        - For example, while being transferred from its sender to its receiver, a message data may take the following path on the sending side :
            
            (a) From sender’s stack to its message buffer
            (b) From the message buffer in the sender’s address space to the message buffer in the kernel’s address space
            (c) Finally, from the kernel to the network interface board
            
        - On the receiving side, the data probably takes a similar path in the reverse direction
        - Therefore, for better performance, it is desirable to avoid copying of data
    - **Minimize network traffic :**
        - System performance may also be improved by reducing internode communication costs
        - For example, accesses to remote resources require communication, possibly through intermediate nodes
        - Therefore, migrating a process closer to the resources it is using most heavily may be helpful in reducing network traffic
        - Another way to reduce network traffic is to use the process migration facility to cluster two or more processes that frequently communicate with each other on the same node of the system
    - **Take advantage of fine-grain parallelism for multiprocessing:**
        - Performance can also be improved in this manner also
        - For example, threads are often used for structuring server processes  Servers structured as a group of threads can operate efficiently, because they can simultaneously service requests from several clients

### **SCALABILITY**

- Scalability refers to the capability of a system to adapt to increased service load
- Therefore, a distributed system should be designed to easily cope with the growth of nodes and users in the system
- That is, such growth should not cause serious disruption of service or significant loss of performance to users
- Guiding principles for designing  scalable distributed systems is :
    - **Avoid centralized entities :** In the design of a distributed system, use of centralized entities such as a single central file server or a single database for the entire system makes the distributed system non-scalable due to the security reasons

### **Heterogeneity**

- Heterogeneity refers to the ability for the system to operate on a variety of different hardware and software components
- This is achieved through the implementation of middle-ware in the software layer
- The issue  of the middle-ware is to abstract and interpret the programming procedural calls such that the distributed processing can be achieved on a variety of differing nodes

### **Security :**

- In order that the users can trust the system and rely on it, the various resources of a computer system must be protected against destruction and unauthorized access
- As compared to a centralized system, enforcement of security in a distributed system has the following additional requirements :
- It should be possible for
    - i.) the sender of a message to know that the message was received by the intended receiver
    - ii.) the receiver of a message to know that the message was sent by the genuine sender
    - iii.) both the sender and receiver of a message to be guaranteed that the contents of the message were not changed while it was in transfer.
- **Cryptography** is the only known practical method for dealing with these security aspects of a distributed system.

---

### Network Operating System (NOS)

- **NOS** is software that connects multiple devices and computers on the network and allows them to share resources on the network
- **Functions of the NOS :**
    - Creating and managing user accounts on the network
    - Controlling access to resources on the network
    - Providing communication services between the devices on the network
    - Monitoring and troubleshooting the network
    - Configuring and Managing the resources on the network
- **Types of Network operating systems :**
    - Peer to Peer
        - Peer-to-peer NOSs allow sharing resources and files with small-sized networks and having fewer resources
        - In general, peer-to-peer NOSs are used on LAN
    - Client/server
        - Client-server NOSs provide users access to resources through the central server
        - Client-server NOS is good for the big networks which provide many services

### Distributed Operating System (DOS)

- A distributed operating system is system software over a collection of independent software, networked, communicating and physically separate computational nodes

| Key | Network OS | Distributed OS |
| --- | --- | --- |
| Objective | It provides local services to remote clients. | It manages the hardware resources. |
| Communication | Communication is file-based, shared folder based. | Communication is message-based or shared memory-based. |
| Scalability | Network OS is highly scalable. A new machine can be added very easily. | Distributed OS is less scalable. The process to add new hardware is complex. |
| Fault tolerance | Less fault tolerance as compared to distributed OS. | It has very high fault tolerance. |
| Autonomy | Each machine can acts on its own thus autonomy is high. | It has a poor rate of autonomy |
| Implementation | Network OS-based systems are easy to build and maintain. | It is difficult to implement a Distributed OS. |
| Operating System | Network OS-based systems have their own copy of operating systems. | Distributed OS-based nodes have the same copy of the operating system. |

---

## Middleware

![Untitled](Distributed%20Computing%20Module%20-%201%20acb1d860c38141298568053fdf69a861/Untitled%201.png)

- Middleware is software that is used to bridge the gap between applications and operating systems.
- Middleware ****is a S/W that  acts as an intermediary between other applications or devices
    - For example, it is possible to turn existing custom applications into Software as a Service applications with all the complex software architecture handled by platform middleware
- To support heterogeneous computers and n/w while offering a single system view, distributed system are often organized by means of a layer of software that is placed between a user applications and OS. → **This is called as a middleware.**
- Goal of the middleware is to hide the heterogeneity of the underlying platforms.
    - All different types of transparencies are provided by the middleware.

### Services Provided by Middleware

- Middleware offers a range of services that facilitate communication, integration, and management of distributed systems and applications.
- A middleware has mainly 4 functions :
1. **Makes distribution as transparent as possible:**
    - Masks complexities of distributed system communication.
    - Manages data communication intricacies like network protocols, message passing, and serialization.
    - Allows developers to focus on application logic instead of network details.
2. **Provides homogenous view of the underlying heterogeneous hardware and software systems:**
    - Standardizes access across diverse systems (different OS, network technologies, programming languages).
    - Abstracts differences between operating systems, database systems, and communication protocols.
    - Enables seamless interoperability across different platforms and environments.
3. **Provides services of common use for the distributed system:**
    - Includes essential services like transaction management, security (authentication and authorization), message queuing, data replication, and load balancing.
    - Standardizes implementation of these functions, improving interoperability.
    - Reduces effort required to implement these features from scratch.
4. **Provides a high level interface or API for programming distributed applications:**
    - Offers high-level APIs for complex operations (e.g., remote procedure calls (RPCs), publish/subscribe messaging, distributed transactions).
    - Simplifies the development of distributed applications by abstracting low-level details.
    - Enables efficient writing of distributed applications, focusing on high-level functions rather than network communication specifics.

### Types of Middleware ⇒ MOR DT PEC - MORe DaTa PEC

1. **MESSAGE ORIENTED MIDDLEWARE**
    - It supports the receiving and sending of messages over distributed applications.
    - It enables applications to be disbursed over various platforms.
    - It makes the process of creating software applications spanning many OSs and network  protocols much less complicated.
    - It is one of the most widely used types of middleware.
2. **OBJECT MIDDLEWARE**
    - It is also called an object request broker
    - It gives applications the ability to send objects and request services via an object oriented system
    - In short, it manages the communication between objects.
3. **REMOTE PROCEDURE CALL (RPC) MIDDLEWARE**
    - It calls procedures on remote systems
    - It is used to perform synchronous or asynchronous interactions between applications or systems.
    - It is usually utilized within a software application
4. **DATABASE MIDDLEWARE**
    - It allows for direct access to databases, providing direct interaction with them
    - There are many database gateways and connectivity options
    - This is the most general and commonly known type of middleware
    - This includes SQL database software
5. **TRANSACTION MIDDLEWARE**
    - This includes applications like transaction processing monitors
    - It also encompasses web-application servers
    - These types of middleware are becoming more and more common today
6. **PORTALS**
    - This refers to enterprise portal server
    - It is considered middleware because portals facilitate front-end integration
    - They are used to create interactions between a user’s computer or device and back-end systems and services.
7. **EMBEDDED MIDDLEWARE**
    - It allows for communication and integration services with an interface of software or firmware
    - It acts as a liaison between embedded applications and the real-time operating system
8. **CONTENT-CENTRIC MIDDLEWARE**
    - It allows to abstract specific content without worrying how it is obtained
    - This is done through a simple provide / consume abstraction
    - It is similar to publish / subscribe middleware, which is another type of this software that is often used as a part of web-based applications