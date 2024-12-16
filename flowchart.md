```mermaid
mindmap
  root((升级策略))
    subgraph 1[不兼容性和依赖冲突的升级策略]
      splitMode(拆分模式)
      rollingUpgrade(滚动升级)
      partialParallelUpgrade(局部并行升级)
    end
    subgraph 2[高可用和大规模集群系统的升级方法]
      fastReboot(快速重启)
      rollingUpgrade2(滚动升级)
      bigFlip(大反转)
      blueGreenDeployment(蓝绿部署)
      canaryDeployment(金丝雀部署)
    end
    subgraph 3[OpenStack 升级流程]
      controlNode(升级控制节点)
      computeNode(升级计算节点)
      storageNode(升级存储节点)
    end
    subgraph 4[Kubernetes 升级流程]
      rollingUpgrade3(滚动升级)
      updateK8SComponent(逐步更新K8S组件)
    end
