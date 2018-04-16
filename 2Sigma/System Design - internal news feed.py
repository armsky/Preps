SQL:
1. Table based
    Schema should be carfully designed as it is not very horizontally scalable
2. Query language: good for complex logic, but maybe limited (need schema design)
3. Not good at sharding (MySQL can)
4. getting slower when data set becomes bigger and bigger

NoSQL:
1. Document based, key-value pair, graph, etc.
    horizontally scalable, good for every-chaning data set
2. Only simple queries
3. Easier for sharding
4. better performance with big data
