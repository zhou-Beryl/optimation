```mermaid
mindmap
  root((升级策略))
    style root fill:#E0F7FA,stroke:#0288D1,stroke-width:2px
    subgraph 1[不兼容性和依赖冲突的升级策略]
      style 1 fill:#B3E5FC,stroke:#0288D1,stroke-width:2px
      splitMode(拆分模式)
      style splitMode fill:#81D4FA,stroke:#0288D1,stroke-width:2px
      rollingUpgrade(滚动升级)
      style rollingUpgrade fill:#81D4FA,stroke:#0288D1,stroke-width:2px
      partialParallelUpgrade(局部并行升级)
      style partialParallelUpgrade fill:#81D4FA,stroke:#0288D1,stroke-width:2px
    end
    subgraph 2[高可用和大规模集群系统的升级方法]
      style 2 fill:#B3E5FC,stroke:#0288D1,stroke-width:2px
      fastReboot(快速重启)
      style fastReboot fill:#81D4FA,stroke:#0288D1,stroke-width:2px
      rollingUpgrade2(滚动升级)
      style rollingUpgrade2 fill:#81D4FA,stroke:#0288D1,stroke-width:2px
      bigFlip(大反转)
      style bigFlip fill:#81D4FA,stroke:#0288D1,stroke-width:2px
      blueGreenDeployment(蓝绿部署)
      style blueGreenDeployment fill:#81D4FA,stroke:#0288D1,stroke-width:2px
      canaryDeployment(金丝雀部署)
      style canaryDeployment fill:#81D4FA,stroke:#0288D1,stroke-width:2px
    end
    subgraph 3[OpenStack 升级流程]
      style 3 fill:#B3E5FC,stroke:#0288D1,stroke-width:2px
      controlNode(升级控制节点)
      style controlNode fill:#81D4FA,stroke:#0288D1,stroke-width:2px
      computeNode(升级计算节点)
      style computeNode fill:#81D4FA,stroke:#0288D1,stroke-width:2px
      storageNode(升级存储节点)
      style storageNode fill:#81D4FA,stroke:#0288D1,stroke-width:2px
    end
    subgraph 4[Kubernetes 升级流程]
      style 4 fill:#B3E5FC,stroke:#0288D1,stroke-width:2px
      rollingUpgrade3(滚动升级)
      style rollingUpgrade3 fill:#81D4FA,stroke:#0288D1,stroke-width:2px
      updateK8SComponent(逐步更新K8S组件)
      style updateK8SComponent fill:#81D4FA,stroke:#0288D1,stroke-width:2px
    end
