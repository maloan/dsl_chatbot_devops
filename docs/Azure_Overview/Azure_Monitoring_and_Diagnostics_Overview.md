## **1. Detection, Triage, and Diagnosis**

These tools assist in identifying and analyzing issues in your Azure environment to enable quick resolution and continuous improvement.

### **Monitoring and Alerts**

- **[Alerts](https://portal.azure.com/#blade/Microsoft_Azure_Monitoring/AzureMonitoringBrowseBlade/alertsV2)**: Proactive notifications based on resource metrics and thresholds to detect anomalies or critical events.
- **[Autoscale](https://portal.azure.com/#blade/Microsoft_Azure_Monitoring/AzureMonitoringBrowseBlade/autoscale)**: Automatically adjusts the number of resources based on load conditions to ensure performance and cost-efficiency.
- **[Metrics](https://portal.azure.com/#blade/Microsoft_Azure_Monitoring/AzureMonitoringBrowseBlade/metrics)**: Real-time monitoring and visualization of performance metrics from Azure resources.

### **Change and Diagnostics**

- **[Change Analysis](https://portal.azure.com/#blade/Microsoft_Azure_ChangeAnalysis/ChangeAnalysisBaseBlade)**: Tracks and visualizes configuration changes to identify issues caused by recent updates.
- **[Diagnostic Settings](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/microsoft.eventhub%2Fnamespaces%2Fproviders%2Fdiagnosticsettings)**: Configure resource-level diagnostic logs and metrics collection for deeper analysis.

### **Log and Workspace Management**

- **[Log Analytics Workspaces](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.OperationalInsights%2Fworkspaces)**: Centralized repository for telemetry logs, enabling advanced analysis using KQL (Kusto Query Language).
- **[Azure Monitor Workspaces](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/microsoft.monitor%2Faccounts)**: Unified monitoring workspace for managing metrics, logs, and diagnostics data.
- **[Managed Prometheus](https://portal.azure.com/#blade/Microsoft_Azure_Monitoring/AzureMonitoringBrowseBlade/prometheus)**: Managed Prometheus service for containerized and Kubernetes environments.
- **[Azure Workbooks](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/microsoft.insights%2Fworkbooks)**: Interactive and customizable reports that combine metrics, logs, and visualizations.
- **[Azure Native Dynatrace Service Partner](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Dynatrace.Observability%2Fmonitors)**: Deep observability and application performance monitoring through Dynatrace integration.

---

## **2. Insights**

Gain detailed visibility and actionable insights into application and service performance.

- **[Application Insights](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/microsoft.insights%2Fcomponents)**: End-to-end monitoring for live applications, offering features like dependency tracking, transaction diagnostics, and custom telemetry analysis.

---

## **3. Monitoring Tools**

Comprehensive tools designed to collect, visualize, and analyze telemetry data for infrastructure, applications, and services.

### **Core Monitoring Tools**

- **[Monitor](https://portal.azure.com/#blade/Microsoft_Azure_Monitoring/AzureMonitoringBrowseBlade)**: Central hub for managing all Azure monitoring resources and visualizing performance data.
- **[Activity Log](https://portal.azure.com/#blade/Microsoft_Azure_Monitoring/AzureMonitoringBrowseBlade/activityLog)**: View and analyze control plane events to track actions performed on Azure resources.
- **[Service Health](https://portal.azure.com/#blade/Microsoft_Azure_Health/AzureHealthBrowseBlade)**: Monitor the health of Azure services and regions, with notifications for planned maintenance or outages.
- **[Network Watcher](https://portal.azure.com/#blade/Microsoft_Azure_Network/NetworkWatcherMenuBlade)**: Diagnose and monitor the performance of Azure and hybrid networks, including packet captures and flow logs.

### **Data Collection**

- **[Data Collection Endpoints](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/microsoft.insights%2Fdatacollectionendpoints)**: Centralize data ingestion points for logs and metrics.
- **[Data Collection Rules](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/microsoft.insights%2Fdatacollectionrules)**: Define rules for filtering, transforming, and routing telemetry data across Azure Monitor.

### **Specialized Monitoring Solutions**

- **[Database Watchers (Preview)](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.DatabaseWatcher%2Fwatchers)**: Monitor and analyze database performance and queries for optimization.
- **[Azure Monitors for SAP Solutions](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Workloads%2Fmonitors)**: Monitor mission-critical SAP workloads on Azure for performance, health, and compliance.
- **[Log Analytics Query Packs (Preview)](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.OperationalInsights%2Fquerypacks)**: Pre-built KQL query packs to simplify and standardize log analytics.

---

## **4. Partner Solutions**

Enhance monitoring and observability with third-party integrations for specialized use cases.

- **[Azure Managed Grafana](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Dashboard%2Fgrafana)**: Managed Grafana service to build real-time dashboards for multi-cloud and hybrid environments.
- **[Datadog - An Azure Native ISV Service Partner](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Datadog%2Fmonitors)**: Unified monitoring for Azure resources and applications through Datadog’s cloud-native observability platform.
- **[Elastic Cloud (Elasticsearch) – An Azure Native ISV Service Partner](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.Elastic%2Fmonitors)**: Integrate Elasticsearch and Kibana with Azure to analyze, visualize, and act on log data.
- **[Azure Native New Relic Service Partner](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/NewRelic.Observability%2Fmonitors)**: Advanced observability and application performance monitoring powered by New Relic.

---

## **5. Resources and Further Reading**

|**Topic**|**Link**|
|---|---|
|[Azure Monitor Overview](../Monitoring/Azure_Monitoring/Azure Monitor Overview)|[Azure Monitor Documentation](https://learn.microsoft.com/en-us/azure/azure-monitor/)|
|Application Insights Overview|[Application Insights Guide](https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview)|
|Network Monitoring with Watcher|[Azure Network Watcher](https://learn.microsoft.com/en-us/azure/network-watcher/)|
|Integrating Grafana with Azure|[Azure Managed Grafana](https://learn.microsoft.com/en-us/azure/azure-managed-grafana/)|
|Log Analytics KQL Basics|[KQL Quick Reference](https://learn.microsoft.com/en-us/azure/data-explorer/kql-quick-reference)|
|Observability with Datadog|[Datadog Integration](https://learn.microsoft.com/en-us/azure/azure-datadog/)|

---
