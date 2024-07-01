This is a repository for running Llama3 8B on Windows.

# How to Run Llama3 8B on Windows

## Prerequsites

### Preparing AWS server

This code was tested on Amazon EC2 g5.2xlarge instance.

OS: Windows Server 2022 Datacenter 64-bit(10.0, Build 20348)

### Install NVIDIA Driver

Instance should have installed NVIDIA driver compatible with your GPU server.

To check if NVIDIA driver is installed, you can run ```nvidia-smi```

If it's not working, you can download in https://www.nvidia.com/download/driverResults.aspx/202377/en-us/ and install.

### Install Cuda Toolkit

Instance should have installed Cuda Toolkit to access GPU on host computer.

To check if it is installed, you can use ```nvcc --version```

If it is not installed yet, you can download in https://developer.nvidia.com/cuda-12-0-0-download-archive and install


### Install Python

Download Python in https://www.python.org/downloads/
