```mermaid
flowchart TD
  %% ---------- L1 ----------
  subgraph L1[硬件拓扑层]
    CPU[CPU 节点<br/>(x86-64 + DDR4)]
    GPU[GPU 节点<br/>(8× H100 + NVLink)]
    FPGA[FPGA 节点<br/>(Xilinx VU13P)]
    Storage[存储节点<br/>(Ceph / NVMe)]
    Interconnect[高速互联<br/>InfiniBand / NVSwitch]
    CPU -->|IB| Interconnect
    GPU -->|IB| Interconnect
    FPGA -->|PCIe<br/>IB| Interconnect
    Storage -->|100 GbE<br/>IB| Interconnect
  end

  %% ---------- L2 ----------
  subgraph L2[资源抽象层]
    SLURM[SLURM<br/>gres.conf + Partition]
    K8s[Kubernetes<br/>nvidia-device-plugin<br/>FPGA device-plugin]
    Labels[资源标签<br/>(gpu / fpga / nvlink)]
  end
  Interconnect --> SLURM
  Interconnect --> K8s
  SLURM --> Labels
  K8s --> Labels

  %% ---------- L3 ----------
  subgraph L3[任务编排层]
    WF[工作流引擎<br/>Argo / Nextflow]
    Sched[调度器<br/>sbatch / Volcano]
  end
  Labels --> WF
  SLURM --> Sched
  K8s --> Sched
  Sched --> WF

  %% ---------- L4 ----------
  subgraph L4[运行时协同层]
    Sim[多物理仿真<br/>MPI / OpenMP]
    Train[AI 训练<br/>PyTorch + NCCL]
    Infer[FPGA 推理<br/>PCIe DMA]
  end
  WF --> Sim
  WF --> Train
  WF --> Infer
  Sim --> Train
  Train --> Infer

  %% ---------- L5 ----------
  subgraph L5[监控与自适应层]
    Prom[Prometheus<br/>DCGM / Node Exporter]
    Graf[Grafana 仪表盘]
    Hook[调度 Hook / Autoscaler]
  end
  Sim --> Prom
  Train --> Prom
  Infer --> Prom
  Prom --> Graf
  Graf --> Hook
  Hook --> SLURM
  Hook --> K8s
```
