---
created: 2024-10-14 12:49
updated: 2024-10-16 09:40
---

# [Prometheus](https://prometheus.io/)
- Prometheus is 100% open source and community-driven.
- What is Prometheus?[](https://prometheus.io/docs/introduction/faq/#what-is-prometheus)

Prometheus is an open-source systems monitoring and alerting toolkit with an active ecosystem. It is the only system directly supported by [Kubernetes](https://kubernetes.io/) and the de facto standard across the [cloud native ecosystem](https://landscape.cncf.io/).
### [Features](https://prometheus.io/docs/introduction/overview/#features)

Prometheus's main features are:

- a multi-dimensional [data model](https://prometheus.io/docs/concepts/data_model/) with time series data identified by metric name and key/value pairs
- PromQL, a [flexible query language](https://prometheus.io/docs/prometheus/latest/querying/basics/) to leverage this dimensionality
- no reliance on distributed storage; single server nodes are autonomous
- time series collection happens via a pull model over HTTP
- [pushing time series](https://prometheus.io/docs/instrumenting/pushing/) is supported via an intermediary gateway
- targets are discovered via service discovery or static configuration
- multiple modes of graphing and dashboarding support
### [components](https://prometheus.io/docs/introduction/overview/#components)

The Prometheus ecosystem consists of multiple components, many of which are optional:

- the main [Prometheus server](https://github.com/prometheus/prometheus) which scrapes and stores time series data
- [client libraries](https://prometheus.io/docs/instrumenting/clientlibs/) for instrumenting application code
- a [push gateway](https://github.com/prometheus/pushgateway) for supporting short-lived jobs
- special-purpose [exporters](https://prometheus.io/docs/instrumenting/exporters/) for services like HAProxy, StatsD, Graphite, etc.
- an [alertmanager](https://github.com/prometheus/alertmanager) to handle alerts
- various support tools

Most Prometheus components are written in [Go](https://golang.org/), making them easy to build and deploy as static binaries. 
![[architecture.png]]
Prometheus scrapes metrics from instrumented jobs, either directly or via an intermediary push gateway for short-lived jobs. It stores all scraped samples locally and runs rules over this data to either aggregate and record new time series from existing data or generate alerts. [Grafana](https://grafana.com/) or other API consumers can be used to visualize the collected data.

# [Comparison to alternatives](https://prometheus.io/docs/introduction/comparison/#comparison-to-alternatives)
## Prometheus vs. Graphite[](https://prometheus.io/docs/introduction/comparison/#prometheus-vs-graphite)

### Scope[](https://prometheus.io/docs/introduction/comparison/#scope)

[Graphite](http://graphite.readthedocs.org/en/latest/) focuses on being a passive time series database with a query language and graphing features. Any other concerns are addressed by external components.

Prometheus is a full monitoring and trending system that includes built-in and active scraping, storing, querying, graphing, and alerting based on time series data. It has knowledge about what the world should look like (which endpoints should exist, what time series patterns mean trouble, etc.), and actively tries to find faults.

### Data model[](https://prometheus.io/docs/introduction/comparison/#data-model)

Graphite stores numeric samples for named time series, much like Prometheus does. However, Prometheus's metadata model is richer: while Graphite metric names consist of dot-separated components which implicitly encode dimensions, Prometheus encodes dimensions explicitly as key-value pairs, called labels, attached to a metric name. This allows easy filtering, grouping, and matching by these labels via the query language.

Further, especially when Graphite is used in combination with [StatsD](https://github.com/etsy/statsd/), it is common to store only aggregated data over all monitored instances, rather than preserving the instance as a dimension and being able to drill down into individual problematic instances.

For example, storing the number of HTTP requests to API servers with the response code `500` and the method `POST` to the `/tracks` endpoint would commonly be encoded like this in Graphite/StatsD:

```
stats.api-server.tracks.post.500 -> 93
```

In Prometheus the same data could be encoded like this (assuming three api-server instances):

```
api_server_http_requests_total{method="POST",handler="/tracks",status="500",instance="<sample1>"} -> 34
api_server_http_requests_total{method="POST",handler="/tracks",status="500",instance="<sample2>"} -> 28
api_server_http_requests_total{method="POST",handler="/tracks",status="500",instance="<sample3>"} -> 31
```

### Storage[](https://prometheus.io/docs/introduction/comparison/#storage)

Graphite stores time series data on local disk in the [Whisper](http://graphite.readthedocs.org/en/latest/whisper.html) format, an RRD-style database that expects samples to arrive at regular intervals. Every time series is stored in a separate file, and new samples overwrite old ones after a certain amount of time.

Prometheus also creates one local file per time series, but allows storing samples at arbitrary intervals as scrapes or rule evaluations occur. Since new samples are simply appended, old data may be kept arbitrarily long. Prometheus also works well for many short-lived, frequently changing sets of time series.

### Summary[](https://prometheus.io/docs/introduction/comparison/#summary)

Prometheus offers a richer data model and query language, in addition to being easier to run and integrate into your environment. If you want a clustered solution that can hold historical data long term, Graphite may be a better choice.

## Prometheus vs. InfluxDB[](https://prometheus.io/docs/introduction/comparison/#prometheus-vs-influxdb)

[InfluxDB](https://influxdata.com/) is an open-source time series database, with a commercial option for scaling and clustering. The InfluxDB project was released almost a year after Prometheus development began, so we were unable to consider it as an alternative at the time. Still, there are significant differences between Prometheus and InfluxDB, and both systems are geared towards slightly different use cases.

### Scope[](https://prometheus.io/docs/introduction/comparison/#scope-0)

For a fair comparison, we must also consider [Kapacitor](https://github.com/influxdata/kapacitor) together with InfluxDB, as in combination they address the same problem space as Prometheus and the Alertmanager.

The same scope differences as in the case of [Graphite](https://prometheus.io/docs/introduction/comparison/#prometheus-vs-graphite) apply here for InfluxDB itself. In addition InfluxDB offers continuous queries, which are equivalent to Prometheus recording rules.

Kapacitor’s scope is a combination of Prometheus recording rules, alerting rules, and the Alertmanager's notification functionality. Prometheus offers [a more powerful query language for graphing and alerting](https://www.robustperception.io/translating-between-monitoring-languages/). The Prometheus Alertmanager additionally offers grouping, deduplication and silencing functionality.

### Data model / storage[](https://prometheus.io/docs/introduction/comparison/#data-model-storage)

Like Prometheus, the InfluxDB data model has key-value pairs as labels, which are called tags. In addition, InfluxDB has a second level of labels called fields, which are more limited in use. InfluxDB supports timestamps with up to nanosecond resolution, and float64, int64, bool, and string data types. Prometheus, by contrast, supports the float64 data type with limited support for strings, and millisecond resolution timestamps.

InfluxDB uses a variant of a [log-structured merge tree for storage with a write ahead log](https://docs.influxdata.com/influxdb/v1.7/concepts/storage_engine/), sharded by time. This is much more suitable to event logging than Prometheus's append-only file per time series approach.

[Logs and Metrics and Graphs, Oh My!](https://grafana.com/blog/2016/01/05/logs-and-metrics-and-graphs-oh-my/) describes the differences between event logging and metrics recording.

### Architecture[](https://prometheus.io/docs/introduction/comparison/#architecture)

Prometheus servers run independently of each other and only rely on their local storage for their core functionality: scraping, rule processing, and alerting. The open source version of InfluxDB is similar.

The commercial InfluxDB offering is, by design, a distributed storage cluster with storage and queries being handled by many nodes at once.

This means that the commercial InfluxDB will be easier to scale horizontally, but it also means that you have to manage the complexity of a distributed storage system from the beginning. Prometheus will be simpler to run, but at some point you will need to shard servers explicitly along scalability boundaries like products, services, datacenters, or similar aspects. Independent servers (which can be run redundantly in parallel) may also give you better reliability and failure isolation.

Kapacitor's open-source release has no built-in distributed/redundant options for rules, alerting, or notifications. The open-source release of Kapacitor can be scaled via manual sharding by the user, similar to Prometheus itself. Influx offers [Enterprise Kapacitor](https://docs.influxdata.com/enterprise_kapacitor), which supports an HA/redundant alerting system.

Prometheus and the Alertmanager by contrast offer a fully open-source redundant option via running redundant replicas of Prometheus and using the Alertmanager's [High Availability](https://github.com/prometheus/alertmanager#high-availability) mode.

### Summary[](https://prometheus.io/docs/introduction/comparison/#summary-0)

There are many similarities between the systems. Both have labels (called tags in InfluxDB) to efficiently support multi-dimensional metrics. Both use basically the same data compression algorithms. Both have extensive integrations, including with each other. Both have hooks allowing you to extend them further, such as analyzing data in statistical tools or performing automated actions.

Where InfluxDB is better:

- If you're doing event logging.
- Commercial option offers clustering for InfluxDB, which is also better for long term data storage.
- Eventually consistent view of data between replicas.

Where Prometheus is better:

- If you're primarily doing metrics.
- More powerful query language, alerting, and notification functionality.
- Higher availability and uptime for graphing and alerting.

InfluxDB is maintained by a single commercial company following the open-core model, offering premium features like closed-source clustering, hosting and support. Prometheus is a [fully open source and independent project](https://prometheus.io/community/), maintained by a number of companies and individuals, some of whom also offer commercial services and support.

## Prometheus vs. OpenTSDB[](https://prometheus.io/docs/introduction/comparison/#prometheus-vs-opentsdb)

[OpenTSDB](http://opentsdb.net/) is a distributed time series database based on [Hadoop](http://hadoop.apache.org/) and [HBase](http://hbase.apache.org/).

### Scope[](https://prometheus.io/docs/introduction/comparison/#scope-1)

The same scope differences as in the case of [Graphite](https://prometheus.io/docs/introduction/comparison/#prometheus-vs-graphite) apply here.

### Data model[](https://prometheus.io/docs/introduction/comparison/#data-model-0)

OpenTSDB's data model is almost identical to Prometheus's: time series are identified by a set of arbitrary key-value pairs (OpenTSDB tags are Prometheus labels). All data for a metric is [stored together](http://opentsdb.net/docs/build/html/user_guide/writing/index.html#time-series-cardinality), limiting the cardinality of metrics. There are minor differences though: Prometheus allows arbitrary characters in label values, while OpenTSDB is more restrictive. OpenTSDB also lacks a full query language, only allowing simple aggregation and math via its API.

### Storage[](https://prometheus.io/docs/introduction/comparison/#storage-0)

[OpenTSDB](http://opentsdb.net/)'s storage is implemented on top of [Hadoop](http://hadoop.apache.org/) and [HBase](http://hbase.apache.org/). This means that it is easy to scale OpenTSDB horizontally, but you have to accept the overall complexity of running a Hadoop/HBase cluster from the beginning.

Prometheus will be simpler to run initially, but will require explicit sharding once the capacity of a single node is exceeded.

### Summary[](https://prometheus.io/docs/introduction/comparison/#summary-1)

Prometheus offers a much richer query language, can handle higher cardinality metrics, and forms part of a complete monitoring system. If you're already running Hadoop and value long term storage over these benefits, OpenTSDB is a good choice.

## Prometheus vs. Nagios[](https://prometheus.io/docs/introduction/comparison/#prometheus-vs-nagios)

[Nagios](https://www.nagios.org/) is a monitoring system that originated in the 1990s as NetSaint.

### Scope[](https://prometheus.io/docs/introduction/comparison/#scope-2)

Nagios is primarily about alerting based on the exit codes of scripts. These are called “checks”. There is silencing of individual alerts, however no grouping, routing or deduplication.

There are a variety of plugins. For example, piping the few kilobytes of perfData plugins are allowed to return [to a time series database such as Graphite](https://github.com/shawn-sterling/graphios) or using NRPE to [run checks on remote machines](https://exchange.nagios.org/directory/Addons/Monitoring-Agents/NRPE--2D-Nagios-Remote-Plugin-Executor/details).

### Data model[](https://prometheus.io/docs/introduction/comparison/#data-model-1)

Nagios is host-based. Each host can have one or more services and each service can perform one check.

There is no notion of labels or a query language.

### Storage[](https://prometheus.io/docs/introduction/comparison/#storage-1)

Nagios has no storage per-se, beyond the current check state. There are plugins which can store data such as [for visualisation](https://docs.pnp4nagios.org/).

### Architecture[](https://prometheus.io/docs/introduction/comparison/#architecture-0)

Nagios servers are standalone. All configuration of checks is via file.

### Summary[](https://prometheus.io/docs/introduction/comparison/#summary-2)

Nagios is suitable for basic monitoring of small and/or static systems where blackbox probing is sufficient.

If you want to do whitebox monitoring, or have a dynamic or cloud based environment, then Prometheus is a good choice.

## Prometheus vs. Sensu[](https://prometheus.io/docs/introduction/comparison/#prometheus-vs-sensu)

[Sensu](https://sensu.io) is an open source monitoring and observability pipeline with a commercial distribution which offers additional features for scalability. It can reuse existing Nagios plugins.

### Scope[](https://prometheus.io/docs/introduction/comparison/#scope-3)

Sensu is an observability pipeline that focuses on processing and alerting of observability data as a stream of [Events](https://docs.sensu.io/sensu-go/latest/observability-pipeline/observe-events/events/). It provides an extensible framework for event [filtering](https://docs.sensu.io/sensu-go/latest/observability-pipeline/observe-filter/), aggregation, [transformation](https://docs.sensu.io/sensu-go/latest/observability-pipeline/observe-transform/), and [processing](https://docs.sensu.io/sensu-go/latest/observability-pipeline/observe-process/) – including sending alerts to other systems and storing events in third-party systems. Sensu's event processing capabilities are similar in scope to Prometheus alerting rules and Alertmanager.

### Data model[](https://prometheus.io/docs/introduction/comparison/#data-model-2)

Sensu [Events](https://docs.sensu.io/sensu-go/latest/observability-pipeline/observe-events/events/) represent service health and/or [metrics](https://docs.sensu.io/sensu-go/latest/observability-pipeline/observe-events/events/#metric-attributes) in a structured data format identified by an [entity](https://docs.sensu.io/sensu-go/latest/observability-pipeline/observe-entities/entities/) name (e.g. server, cloud compute instance, container, or service), an event name, and optional [key-value metadata](https://docs.sensu.io/sensu-go/latest/observability-pipeline/observe-events/events/#metadata-attributes) called "labels" or "annotations". The Sensu Event payload may include one or more metric [`points`](https://docs.sensu.io/sensu-go/latest/observability-pipeline/observe-events/events/#points-attributes), represented as a JSON object containing a `name`, `tags` (key/value pairs), `timestamp`, and `value` (always a float).

### Storage[](https://prometheus.io/docs/introduction/comparison/#storage-2)

Sensu stores current and recent event status information and real-time inventory data in an embedded database (etcd) or an external RDBMS (PostgreSQL).

### Architecture[](https://prometheus.io/docs/introduction/comparison/#architecture-1)

All components of a Sensu deployment can be clustered for high availability and improved event-processing throughput.

### Summary[](https://prometheus.io/docs/introduction/comparison/#summary-3)

Sensu and Prometheus have a few capabilities in common, but they take very different approaches to monitoring. Both offer extensible discovery mechanisms for dynamic cloud-based environments and ephemeral compute platforms, though the underlying mechanisms are quite different. Both provide support for collecting multi-dimensional metrics via labels and annotations. Both have extensive integrations, and Sensu natively supports collecting metrics from all Prometheus exporters. Both are capable of forwarding observability data to third-party data platforms (e.g. event stores or TSDBs). Where Sensu and Prometheus differ the most is in their use cases.

Where Sensu is better:

- If you're collecting and processing hybrid observability data (including metrics _and/or_ events)
- If you're consolidating multiple monitoring tools and need support for metrics _and_ Nagios-style plugins or check scripts
- More powerful event-processing platform

Where Prometheus is better:

- If you're primarily collecting and evaluating metrics
- If you're monitoring homogeneous Kubernetes infrastructure (if 100% of the workloads you're monitoring are in K8s, Prometheus offers better K8s integration)
- More powerful query language, and built-in support for historical data analysis

Sensu is maintained by a single commercial company following the open-core business model, offering premium features like closed-source event correlation and aggregation, federation, and support. Prometheus is a fully open source and independent project, maintained by a number of companies and individuals, some of whom also offer commercial services and support.

- Prometheus fundamentally stores all data as [_time series_](https://en.wikipedia.org/wiki/Time_series): streams of timestamped values belonging to the same metric and the same set of labeled dimensions. Besides stored time series, Prometheus may generate temporary derived time series as the result of queries.

# Querying Prometheus
Prometheus provides a functional query language called PromQL (Prometheus Query Language) that lets the user select and aggregate time series data in real time. The result of an expression can either be shown as a graph, viewed as tabular data in Prometheus's expression browser, or consumed by external systems via the [HTTP API](https://prometheus.io/docs/prometheus/latest/querying/api/).

# Installation[](https://prometheus.io/docs/prometheus/latest/installation/#installation)

- [Using pre-compiled binaries](https://prometheus.io/docs/prometheus/latest/installation/#using-pre-compiled-binaries)
- [From source](https://prometheus.io/docs/prometheus/latest/installation/#from-source)
- [Using Docker](https://prometheus.io/docs/prometheus/latest/installation/#using-docker)

- [Setting command line parameters](https://prometheus.io/docs/prometheus/latest/installation/#setting-command-line-parameters)
- [Volumes & bind-mount](https://prometheus.io/docs/prometheus/latest/installation/#volumes-bind-mount)
- [Save your Prometheus data](https://prometheus.io/docs/prometheus/latest/installation/#save-your-prometheus-data)
- [Custom image](https://prometheus.io/docs/prometheus/latest/installation/#custom-image)

- [Using configuration management systems](https://prometheus.io/docs/prometheus/latest/installation/#using-configuration-management-systems)

- [Ansible](https://prometheus.io/docs/prometheus/latest/installation/#ansible)
- [Chef](https://prometheus.io/docs/prometheus/latest/installation/#chef)
- [Puppet](https://prometheus.io/docs/prometheus/latest/installation/#puppet)
- [SaltStack](https://prometheus.io/docs/prometheus/latest/installation/#saltstack)

## Using pre-compiled binaries[](https://prometheus.io/docs/prometheus/latest/installation/#using-pre-compiled-binaries)

We provide precompiled binaries for most official Prometheus components. Check out the [download section](https://prometheus.io/download) for a list of all available versions.

## From source[](https://prometheus.io/docs/prometheus/latest/installation/#from-source)

For building Prometheus components from source, see the `Makefile` targets in the respective repository.

## Using Docker[](https://prometheus.io/docs/prometheus/latest/installation/#using-docker)

All Prometheus services are available as Docker images on [Quay.io](https://quay.io/repository/prometheus/prometheus) or [Docker Hub](https://hub.docker.com/r/prom/prometheus/).

Running Prometheus on Docker is as simple as `docker run -p 9090:9090 prom/prometheus`. This starts Prometheus with a sample configuration and exposes it on port 9090.

The Prometheus image uses a volume to store the actual metrics. For production deployments it is highly recommended to use a [named volume](https://docs.docker.com/storage/volumes/) to ease managing the data on Prometheus upgrades.

### Setting command line parameters[](https://prometheus.io/docs/prometheus/latest/installation/#setting-command-line-parameters)

The Docker image is started with a number of default command line parameters, which can be found in the [Dockerfile](https://github.com/prometheus/prometheus/blob/main/Dockerfile) (adjust the link to correspond with the version in use).

If you want to add extra command line parameters to the `docker run` command, you will need to re-add these yourself as they will be overwritten.

### Volumes & bind-mount[](https://prometheus.io/docs/prometheus/latest/installation/#volumes-bind-mount)

To provide your own configuration, there are several options. Here are two examples.

Bind-mount your `prometheus.yml` from the host by running:

```
docker run \
    -p 9090:9090 \
    -v /path/to/prometheus.yml:/etc/prometheus/prometheus.yml \
    prom/prometheus
```

Or bind-mount the directory containing `prometheus.yml` onto `/etc/prometheus` by running:

```
docker run \
    -p 9090:9090 \
    -v /path/to/config:/etc/prometheus \
    prom/prometheus
```

### Save your Prometheus data[](https://prometheus.io/docs/prometheus/latest/installation/#save-your-prometheus-data)

Prometheus data is stored in `/prometheus` dir inside the container, so the data is cleared every time the container gets restarted. To save your data, you need to set up persistent storage (or bind mounts) for your container.

Run Prometheus container with persistent storage:

```
# Create persistent volume for your data
docker volume create prometheus-data
# Start Prometheus container
docker run \
    -p 9090:9090 \
    -v /path/to/prometheus.yml:/etc/prometheus/prometheus.yml \
    -v prometheus-data:/prometheus \
    prom/prometheus
```

### Custom image[](https://prometheus.io/docs/prometheus/latest/installation/#custom-image)

To avoid managing a file on the host and bind-mount it, the configuration can be baked into the image. This works well if the configuration itself is rather static and the same across all environments.

For this, create a new directory with a Prometheus configuration and a `Dockerfile` like this:

```
FROM prom/prometheus
ADD prometheus.yml /etc/prometheus/
```

Now build and run it:

```
docker build -t my-prometheus .
docker run -p 9090:9090 my-prometheus
```

A more advanced option is to render the configuration dynamically on start with some tooling or even have a daemon update it periodically.

## Storage
Prometheus includes a local on-disk time series database, but also optionally integrates with remote storage systems.

## Local storage[](https://prometheus.io/docs/prometheus/latest/storage/#local-storage)

Prometheus's local time series database stores data in a custom, highly efficient format on local storage.

### On-disk layout[](https://prometheus.io/docs/prometheus/latest/storage/#on-disk-layout)

Ingested samples are grouped into blocks of two hours. Each two-hour block consists of a directory containing a chunks subdirectory containing all the time series samples for that window of time, a metadata file, and an index file (which indexes metric names and labels to time series in the chunks directory). The samples in the chunks directory are grouped together into one or more segment files of up to 512MB each by default. When series are deleted via the API, deletion records are stored in separate tombstone files (instead of deleting the data immediately from the chunk segments).

The current block for incoming samples is kept in memory and is not fully persisted. It is secured against crashes by a write-ahead log (WAL) that can be replayed when the Prometheus server restarts. Write-ahead log files are stored in the `wal` directory in 128MB segments. These files contain raw data that has not yet been compacted; thus they are significantly larger than regular block files. Prometheus will retain a minimum of three write-ahead log files. High-traffic servers may retain more than three WAL files in order to keep at least two hours of raw data.

A Prometheus server's data directory looks something like this:

```
./data
├── 01BKGV7JBM69T2G1BGBGM6KB12
│   └── meta.json
├── 01BKGTZQ1SYQJTR4PB43C8PD98
│   ├── chunks
│   │   └── 000001
│   ├── tombstones
│   ├── index
│   └── meta.json
├── 01BKGTZQ1HHWHV8FBJXW1Y3W0K
│   └── meta.json
├── 01BKGV7JC0RY8A6MACW02A2PJD
│   ├── chunks
│   │   └── 000001
│   ├── tombstones
│   ├── index
│   └── meta.json
├── chunks_head
│   └── 000001
└── wal
    ├── 000000002
    └── checkpoint.00000001
        └── 00000000
```

Note that a limitation of local storage is that it is not clustered or replicated. Thus, it is not arbitrarily scalable or durable in the face of drive or node outages and should be managed like any other single node database.

[Snapshots](https://prometheus.io/docs/prometheus/latest/querying/api/#snapshot) are recommended for backups. Backups made without snapshots run the risk of losing data that was recorded since the last WAL sync, which typically happens every two hours. With proper architecture, it is possible to retain years of data in local storage.

Alternatively, external storage may be used via the [remote read/write APIs](https://prometheus.io/docs/operating/integrations/#remote-endpoints-and-storage). Careful evaluation is required for these systems as they vary greatly in durability, performance, and efficiency.

For further details on file format, see [TSDB format](https://github.com/prometheus/prometheus/blob/release-2.54/tsdb/docs/format/README.md).

## Compaction[](https://prometheus.io/docs/prometheus/latest/storage/#compaction)

The initial two-hour blocks are eventually compacted into longer blocks in the background.

Compaction will create larger blocks containing data spanning up to 10% of the retention time, or 31 days, whichever is smaller.
## Authentication, Authorization, and Encryption[](https://prometheus.io/docs/operating/security/#authentication-authorization-and-encryption)

Prometheus, and most exporters, support TLS. Including authentication of clients via TLS client certificates. Details on configuring Prometheus are [`here`](https://prometheus.io/docs/guides/tls-encryption/).

The Go projects share the same TLS library, based on the Go [crypto/tls](https://golang.org/pkg/crypto/tls) library. We default to TLS 1.2 as minimum version. Our policy regarding this is based on [Qualys SSL Labs](https://www.ssllabs.com/) recommendations, where we strive to achieve a grade 'A' with a default configuration and correctly provided certificates, while sticking as closely as possible to the upstream Go defaults. Achieving that grade provides a balance between perfect security and usability.

TLS will be added to Java exporters in the future.

If you have special TLS needs, like a different cipher suite or older TLS version, you can tune the minimum TLS version and the ciphers, as long as the cipher is not [marked as insecure](https://golang.org/pkg/crypto/tls/#InsecureCipherSuites) in the [crypto/tls](https://golang.org/pkg/crypto/tls) library. If that still does not suit you, the current TLS settings enable you to build a secure tunnel between the servers and reverse proxies with more special requirements.

HTTP Basic Authentication is also supported. Basic Authentication can be used without TLS, but it will then expose usernames and passwords in cleartext over the network.

On the server side, basic authentication passwords are stored as hashes with the [bcrypt](https://en.wikipedia.org/wiki/Bcrypt) algorithm. It is your responsibility to pick the number of rounds that matches your security standards. More rounds make brute-force more complicated at the cost of more CPU power and more time to authenticate the requests.

Various Prometheus components support client-side authentication and encryption. If TLS client support is offered, there is often also an option called `insecure_skip_verify` which skips SSL verification.

## API Security[](https://prometheus.io/docs/operating/security/#api-security)

As administrative and mutating endpoints are intended to be accessed via simple tools such as cURL, there is no built in [CSRF](https://en.wikipedia.org/wiki/Cross-site_request_forgery) protection as that would break such use cases. Accordingly when using a reverse proxy, you may wish to block such paths to prevent CSRF.

For non-mutating endpoints, you may wish to set [CORS headers](https://fetch.spec.whatwg.org/#http-cors-protocol) such as `Access-Control-Allow-Origin` in your reverse proxy to prevent [XSS](https://en.wikipedia.org/wiki/Cross-site_scripting).

If you are composing PromQL queries that include input from untrusted users (e.g. URL parameters to console templates, or something you built yourself) who are not meant to be able to run arbitrary PromQL queries make sure any untrusted input is appropriately escaped to prevent injection attacks. For example `up{job="<user_input>"}` would become `up{job=""} or some_metric{zzz=""}` if the `<user_input>` was `"} or some_metric{zzz="`.

For those using Grafana note that [dashboard permissions are not data source permissions](https://grafana.com/docs/grafana/latest/permissions/#data-source-permissions), so do not limit a user's ability to run arbitrary queries in proxy mode.

## Secrets[](https://prometheus.io/docs/operating/security/#secrets)

Non-secret information or fields may be available via the HTTP API and/or logs.

In Prometheus, metadata retrieved from service discovery is not considered secret. Throughout the Prometheus system, metrics are not considered secret.

Fields containing secrets in configuration files (marked explicitly as such in the documentation) will not be exposed in logs or via the HTTP API. Secrets should not be placed in other configuration fields, as it is common for components to expose their configuration over their HTTP endpoint. It is the responsibility of the user to protect files on disk from unwanted reads and writes.

Secrets from other sources used by dependencies (e.g. the `AWS_SECRET_KEY` environment variable as used by EC2 service discovery) may end up exposed due to code outside of our control or due to functionality that happens to expose wherever it is stored.

## Denial of Service[](https://prometheus.io/docs/operating/security/#denial-of-service)

There are some mitigations in place for excess load or expensive queries. However, if too many or too expensive queries/metrics are provided components will fall over. It is more likely that a component will be accidentally taken out by a trusted user than by malicious action.

It is the responsibility of the user to ensure they provide components with sufficient resources including CPU, RAM, disk space, IOPS, file descriptors, and bandwidth.

It is recommended to monitor all components for failure, and to have them automatically restart on failure.

## Libraries[](https://prometheus.io/docs/operating/security/#libraries)

This document considers vanilla binaries built from the stock source code. Information presented here does not apply if you modify Prometheus source code, or use Prometheus internals (beyond the official client library APIs) in your own code.

## Build Process[](https://prometheus.io/docs/operating/security/#build-process)

The build pipeline for Prometheus runs on third-party providers to which many members of the Prometheus development team and the staff of those providers have access. If you are concerned about the exact provenance of your binaries, it is recommended to build them yourself rather than relying on the pre-built binaries provided by the project.


# Grafana
# Grafana support for Prometheus
[Grafana](http://grafana.com/) supports querying Prometheus. 
The following shows an example Grafana dashboard which queries Prometheus for data:![[grafana_prometheus.png]]

### Importing pre-built dashboards from Grafana.com[](https://prometheus.io/docs/visualization/grafana/#importing-pre-built-dashboards-from-grafana-com)

Grafana.com maintains [a collection of shared dashboards](https://grafana.com/dashboards) which can be downloaded and used with standalone instances of Grafana. Use the Grafana.com "Filter" option to browse dashboards for the "Prometheus" data source only.

You must currently manually edit the downloaded JSON files and correct the `datasource:` entries to reflect the Grafana data source name which you chose for your Prometheus server. Use the "Dashboards" → "Home" → "Import" option to import the edited dashboard file into your Grafana install.


## Overview[](https://grafana.com/docs/grafana/latest/#overview)

_Grafana Open Source Software (OSS)_ enables you to query, visualize, alert on, and explore your metrics, logs, and traces wherever they’re stored. Grafana data source plugins enable you to query data sources including time series databases like Prometheus and CloudWatch, logging tools like Loki and Elasticsearch, NoSQL/SQL databases like Postgres, CI/CD tooling like GitHub, and many more. Grafana OSS provides you with tools to display that data on live dashboards with insightful graphs and visualizations.

# About Grafana[](https://grafana.com/docs/grafana/latest/introduction/#about-grafana)

[Grafana open source software](https://grafana.com/oss/) enables you to query, visualize, alert on, and explore your metrics, logs, and traces wherever they are stored. Grafana OSS provides you with tools to turn your time-series database (TSDB) data into insightful graphs and visualizations. The Grafana OSS plugin framework also enables you to connect other data sources like NoSQL/SQL databases, ticketing tools like Jira or ServiceNow, and CI/CD tooling like GitLab.

After you have [installed Grafana](https://grafana.com/docs/grafana/latest/setup-grafana/installation/) and set up your first dashboard using instructions in [Getting started with Grafana](https://grafana.com/docs/grafana/latest/getting-started/build-first-dashboard/), you will have many options to choose from depending on your requirements. For example, if you want to view weather data and statistics about your smart home, then you can create a [playlist](https://grafana.com/docs/grafana/latest/dashboards/create-manage-playlists/). If you are the administrator for an enterprise and are managing Grafana for multiple teams, then you can set up [provisioning](https://grafana.com/docs/grafana/latest/administration/provisioning/) and [authentication](https://grafana.com/docs/grafana/latest/setup-grafana/configure-security/configure-authentication/).

The following sections provide an overview of Grafana features and links to product documentation to help you learn more. For more guidance and ideas, check out our [Grafana Community forums](https://community.grafana.com/).

## Explore metrics, logs, and traces[](https://grafana.com/docs/grafana/latest/introduction/#explore-metrics-logs-and-traces)

Explore your data through ad-hoc queries and dynamic drilldown. Split view and compare different time ranges, queries and data sources side by side. Refer to [Explore](https://grafana.com/docs/grafana/latest/explore/) for more information.

## Alerts[](https://grafana.com/docs/grafana/latest/introduction/#alerts)

If you’re using Grafana Alerting, then you can have alerts sent through a number of different alert notifiers, including PagerDuty, SMS, email, VictorOps, OpsGenie, or Slack.

Alert hooks allow you to create different notifiers with a bit of code if you prefer some other channels of communication. Visually define [alert rules](https://grafana.com/docs/grafana/latest/alerting/alerting-rules/) for your most important metrics.

## Annotations[](https://grafana.com/docs/grafana/latest/introduction/#annotations)

Annotate graphs with rich events from different data sources. Hover over events to see the full event metadata and tags.

This feature, which shows up as a graph marker in Grafana, is useful for correlating data in case something goes wrong. You can create the annotations manually—just control-click on a graph and input some text—or you can fetch data from any data source. Refer to [Annotations](https://grafana.com/docs/grafana/latest/dashboards/build-dashboards/annotate-visualizations/) for more information.

## Dashboard variables[](https://grafana.com/docs/grafana/latest/introduction/#dashboard-variables)

[Template variables](https://grafana.com/docs/grafana/latest/dashboards/variables/) allow you to create dashboards that can be reused for lots of different use cases. Values aren’t hard-coded with these templates, so for instance, if you have a production server and a test server, you can use the same dashboard for both.

Templating allows you to drill down into your data, say, from all data to North America data, down to Texas data, and beyond. You can also share these dashboards across teams within your organization—or if you create a great dashboard template for a popular data source, you can contribute it to the whole community to customize and use.

## Configure Grafana[](https://grafana.com/docs/grafana/latest/introduction/#configure-grafana)

If you’re a Grafana administrator, then you’ll want to thoroughly familiarize yourself with [Grafana configuration options](https://grafana.com/docs/grafana/latest/setup-grafana/configure-grafana/) and the [Grafana CLI](https://grafana.com/docs/grafana/latest/cli/).

Configuration covers both config files and environment variables. You can set up default ports, logging levels, email IP addresses, security, and more.

## Import dashboards and plugins[](https://grafana.com/docs/grafana/latest/introduction/#import-dashboards-and-plugins)

Discover hundreds of [dashboards](https://grafana.com/grafana/dashboards) and [plugins](https://grafana.com/grafana/plugins) in the official library. Thanks to the passion and momentum of community members, new ones are added every week.

## Authentication[](https://grafana.com/docs/grafana/latest/introduction/#authentication)

Grafana supports different authentication methods, such as LDAP and OAuth, and allows you to map users to organizations. Refer to the [User authentication overview](https://grafana.com/docs/grafana/latest/setup-grafana/configure-security/configure-authentication/) for more information.

In Grafana Enterprise, you can also map users to teams: If your company has its own authentication system, Grafana allows you to map the teams in your internal systems to teams in Grafana. That way, you can automatically give people access to the dashboards designated for their teams. Refer to [Grafana Enterprise](https://grafana.com/docs/grafana/latest/introduction/grafana-enterprise/) for more information.

## Provisioning[](https://grafana.com/docs/grafana/latest/introduction/#provisioning)

While it’s easy to click, drag, and drop to create a single dashboard, power users in need of many dashboards will want to automate the setup with a script. You can script anything in Grafana.

For example, if you’re spinning up a new Kubernetes cluster, you can also spin up a Grafana automatically with a script that would have the right server, IP address, and data sources preset and locked in so users cannot change them. It’s also a way of getting control over a lot of dashboards. Refer to [Provisioning](https://grafana.com/docs/grafana/latest/administration/provisioning/) for more information.

- Graphs & charts
    - [Time series](https://grafana.com/docs/grafana/latest/panels-visualizations/visualizations/time-series/) is the default and main graph visualization. Alerts are supported in this panel.
    - [State timeline](https://grafana.com/docs/grafana/latest/panels-visualizations/visualizations/state-timeline/) for state changes over time.
    - [Status history](https://grafana.com/docs/grafana/latest/panels-visualizations/visualizations/status-history/) for periodic state over time.
    - [Bar chart](https://grafana.com/docs/grafana/latest/panels-visualizations/visualizations/bar-chart/) shows any categorical data.
    - [Histogram](https://grafana.com/docs/grafana/latest/panels-visualizations/visualizations/histogram/) calculates and shows value distribution in a bar chart.
    - [Heatmap](https://grafana.com/docs/grafana/latest/panels-visualizations/visualizations/heatmap/) visualizes data in two dimensions, used typically for the magnitude of a phenomenon.
    - [Pie chart](https://grafana.com/docs/grafana/latest/panels-visualizations/visualizations/pie-chart/) is typically used where proportionality is important.
    - [Candlestick](https://grafana.com/docs/grafana/latest/panels-visualizations/visualizations/candlestick/) is typically for financial data where the focus is price/data movement.
    - [Gauge](https://grafana.com/docs/grafana/latest/panels-visualizations/visualizations/gauge/) is the traditional rounded visual showing how far a single metric is from a threshold.
    - [Trend](https://grafana.com/docs/grafana/latest/panels-visualizations/visualizations/trend/) for datasets that have a sequential, numeric x that is not time.
    - [XY chart](https://grafana.com/docs/grafana/latest/panels-visualizations/visualizations/xy-chart/) provides a way to visualize arbitrary x and y values in a graph.
- Stats & numbers
    - [Stat](https://grafana.com/docs/grafana/latest/panels-visualizations/visualizations/stat/) for big stats and optional sparkline.
    - [Bar gauge](https://grafana.com/docs/grafana/latest/panels-visualizations/visualizations/bar-gauge/) is a horizontal or vertical bar gauge.
- Misc
    - [Table](https://grafana.com/docs/grafana/latest/panels-visualizations/visualizations/table/) is the main and only table visualization.
    - [Logs](https://grafana.com/docs/grafana/latest/panels-visualizations/visualizations/logs/) is the main visualization for logs.
    - [Node graph](https://grafana.com/docs/grafana/latest/panels-visualizations/visualizations/node-graph/) for directed graphs or networks.
    - [Traces](https://grafana.com/docs/grafana/latest/panels-visualizations/visualizations/traces/) is the main visualization for traces.
    - [Flame graph](https://grafana.com/docs/grafana/latest/panels-visualizations/visualizations/flame-graph/) is the main visualization for profiling.
    - [Canvas](https://grafana.com/docs/grafana/latest/panels-visualizations/visualizations/canvas/) allows you to explicitly place elements within static and dynamic layouts.
    - [Geomap](https://grafana.com/docs/grafana/latest/panels-visualizations/visualizations/geomap/) helps you visualize geospatial data.
    - [Datagrid](https://grafana.com/docs/grafana/latest/panels-visualizations/visualizations/datagrid/) allows you to create and manipulate data, and act as data source for other panels.
- Widgets
    - [Dashboard list](https://grafana.com/docs/grafana/latest/panels-visualizations/visualizations/dashboard-list/) can list dashboards.
    - [Alert list](https://grafana.com/docs/grafana/latest/panels-visualizations/visualizations/alert-list/) can list alerts.
    - [Annotations list](https://grafana.com/docs/grafana/latest/panels-visualizations/visualizations/annotations/) can list available annotations.
    - [Text](https://grafana.com/docs/grafana/latest/panels-visualizations/visualizations/text/) can show markdown and html.
    - [News](https://grafana.com/docs/grafana/latest/panels-visualizations/visualizations/news/) can show RSS feeds.
