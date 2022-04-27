"""(Maximum marks -15)
Q-1 ) Briefly describe CAP theorem (5 marks)
(Easy)
"""

"""
The CAP theorem is a belief from theoretical computer science about distributed data stores that claims, in the event of 
a network failure on a distributed database, it is possible to provide either consistency or availability—but not both.
The CAP Theorem is comprised of three components (hence its name) as they relate to distributed data stores:
Consistency. All reads receive the most recent write or an error.
Availability. All reads contain data, but it might not be the most recent.
Partition tolerance. The system continues to operate despite network failures (ie; dropped partitions, slow network 
connections, or unavailable network connections between nodes.)
In normal operations, your data store provides all three functions. But the CAP theorem maintains that when a
 distributed database experiences a network failure, you can provide either consistency or availability.
"""
