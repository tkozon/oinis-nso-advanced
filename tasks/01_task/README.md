# NETCONF config-change notification handling and device synchronization

## Overview

This document outlines the tasks required to develop an NSO package designed to handle NETCONF configuration change notifications and synchronize network devices automatically. The package will listen for specific NETCONF notifications indicating configuration changes and trigger synchronization processes to ensure all relevant devices are updated accordingly.

## Objectives

- **Notification Handling:** Listen for and process NETCONF config-change notifications.
- **Device Synchronization:** Automatically synchronize devices upon receiving relevant notifications.

## Prerequisites

Before starting the development, ensure the following prerequisites are met:

- **Load NED from NED Directory:**
  - **NED Package:** `oinic-nc-ned`
  - **Status:** Ensure the NED is loaded and running in NSO.

- **Create Netsim Devices:**
  - **Quantity:** Create at least two Netsim devices using the `oinic-nc-ned`.
  - **Steps:**
    1. Navigate to the NSO directory containing Netsim templates.
    2. Use NSO commands to instantiate two separate Netsim devices based on the `oinic-nc-ned`.

- **Enable NETCONF Notifications for Netsim Devices:**
  - **Configuration File:** Modify `netsim/<DEVICE_NAME>/confd.conf`.
  - **Action:** Add the following XML block inside the `/netconf/capabilities` section to enable NETCONF notifications:
  
    ```xml
    <notification>
      <enabled>true</enabled>
    </notification>
    ```

- **Load Configuration for NETCONF Netsim Devices:**
  
  To load configurations onto your NETCONF Netsim devices, use the following commands:

  ```bash
  netconf-console --port=<DEVICE_PORT> --edit-config=<CONFIG.xml> --db=candidate 
  netconf-console --port=<DEVICE_PORT> --commit

> **_NOTE:_** 
>
>- `<DEVICE_PORT>`: Specify the NETCONF port for the device.  
>  You can find the available ports by running the command:  

>   ```bash
>  ncs-netsim list

>- `CONFIG.xml`: Provide the path to the XML configuration file you wish to load.
> For this use case, an example configuration is located in the xml directory of the project.


