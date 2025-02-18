# Choose a base image with the required CUDA version
FROM nvidia/cuda:11.3.1-base-ubuntu20.04

ENV DEBIAN_FRONTEND=noninteractive
# Install python and pip
RUN apt-get update && \
    apt-get install -y \
        libglib2.0-0 libsm6 libxrender1 libxext6 libgl1 \
        python3 \
        python3-pip

# Set the working directory
WORKDIR /app

# Move the whole repo into the container
COPY . .
# Install torch with the cu113 cuda version
RUN pip install --no-cache-dir torch==1.12.1 torchvision==0.13.1 --index-url https://download.pytorch.org/whl/cu113
RUN pip install --no-cache-dir -r requirements.txt
# make sure the torch installation with cuda worked
# I don't have a machine with CUDA available at the moment, so I'm just skipping this check for now
# RUN python3 -c 'import torch; assert torch.cuda.is_available()'

# Run the app
CMD ["bash", "run_servers.sh"]