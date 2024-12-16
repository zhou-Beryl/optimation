```mermaid
mindmap
  root((升级策略))
    style root fill:#1f4e79,stroke:#1f4e79,color:#ffffff
    subgraph 1[不兼容性和依赖冲突的升级策略]
      style 1 fill:#7a9ab9,stroke:#7a9ab9,color:#ffffff
      splitMode(拆分模式)
      style splitMode fill:#4a7b9d,stroke:#4a7b9d,color:#ffffff
      rollingUpgrade(滚动升级)
      style rollingUpgrade fill:#4a7b9d,stroke:#4a7b9d,color:#ffffff
      partialParallelUpgrade(局部并行升级)
      style partialParallelUpgrade fill:#4a7b9d,stroke:#4a7b9d,color:#ffffff
    end
    subgraph 2[高可用和大规模集群系统的升级方法]
      style 2 fill:#7a9ab9,stroke:#7a9ab9,color:#ffffff
      fastReboot(快速重启)
      style fastReboot fill:#4a7b9d,stroke:#4a7b9d,color:#ffffff
      rollingUpgrade2(滚动升级)
      style rollingUpgrade2 fill:#4a7b9d,stroke:#4a7b9d,color:#ffffff
      bigFlip(大反转)
      style bigFlip fill:#4a7b9d,stroke:#4a7b9d,color:#ffffff
      blueGreenDeployment(蓝绿部署)
      style blueGreenDeployment fill:#4a7b9d,stroke:#4a7b9d,color:#ffffff
      canaryDeployment(金丝雀部署)
      style canaryDeployment fill:#4a7b9d,stroke:#4a7b9d,color:#ffffff
    end
    subgraph 3[OpenStack 升级流程]
      style 3 fill:#7a9ab9,stroke:#7a9ab9,color:#ffffff
      controlNode(升级控制节点)
      style controlNode fill:#4a7b9d,stroke:#4a7b9d,color:#ffffff
      computeNode(升级计算节点)
      style computeNode fill:#4a7b9d,stroke:#4a7b9d,color:#ffffff
      storageNode(升级存储节点)
      style storageNode fill:#4a7b9d,stroke:#4a7b9d,color:#ffffff
    end
    subgraph 4[Kubernetes 升级流程]
      style 4 fill:#7a9ab9,stroke:#7a9ab9,color:#ffffff
      rollingUpgrade3(滚动升级)
      style rollingUpgrade3 fill:#4a7b9d,stroke:#4a7b9d,color:#ffffff
      updateK8SComponent(逐步更新K8S组件)
      style updateK8SComponent fill:#4a7b9d,stroke:#4a7b9d,color:#ffffff
    end
