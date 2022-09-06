# Resource filtering

SDK DMP based automonitoring provides a feature to control what resource types and resources that can be filtered during discovery

As part of App discovery configuration there is an option for the user to select what needs to be discovered

There are two levels at which a user can apply filters

1. Resource Type 
2. Resource

### Resource Type filter is to filter resource types, it will discover the resources based on the filter.

Ex: If vcenter domain contains two resources types one is Host and other is VM

If the user wants to discover and monitor only hosts, there is option to select Host and unselect VM in the discovery configuration Page

![Resource filter based on resource type](/images/selecting_resourcetype_hosts.png)

Only hosts will be discovered, please find the screenshot below for reference

![Resource type discovery](/images/resourcetype_host_discovery.png)

### Resource filter is to filter resources under resource types using filtering condition

Ex: if user wants to discover only host with name **Equals** vcenter1host1, there is option to give the condition shown in below screenshot

![Resource filter based on condition](/images/resourcename_host_selection.png)

Only hosts will name vcenter1host1 will be discovered,  please find the screenshot below for reference

![Resource discovery](/images/resource_host_discovery.png)

Few other condition operators supported for filtering are: Contains, Not Contains, Equals, Not Equals, Starts With, Ends With, Regex

**Note:** <br>
During Resource Type filtering, user need to cautious in selecting the resource types <br>
<br>
Ex: If we unselect Hosts and select only VMs, than the VMs will not be discovered, since its parent is missing <br>
We can't unselect parent and expect child to be discovered <br>
user need to select from bottom up approach, If child needs to be discovered, than parent resource type should be selected.

