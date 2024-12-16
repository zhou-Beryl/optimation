```mermaid
graph TD
    A[升级策略] --> B[不兼容性和依赖冲突的场景]
    B --> C[拆分模式（split mode）]
    B --> D[滚动升级（rolling upgrade）]
    B --> E[局部并行升级（partial parallel upgrade）]
    
    A --> F[高可用和大规模集群系统的升级方法]
    F --> G[快速重启（Fast reboot）]
    F --> H[滚动升级（rolling upgrade）]
    F --> I[大反转（big flip）]
    F --> J[蓝绿部署（Blue-Green Deployment）]
    F --> K[金丝雀部署（Canary Deployment）]
    
    A --> L[OpenStack升级]
    L --> M[分批次升级]
    L --> N[升级控制、计算、存储节点]
    
    A --> O[Kubernetes升级]
    P --> P[滚动升级策略]
    P --> Q[逐步更新各个节点的Kubernetes组件]
