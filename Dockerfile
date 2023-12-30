# Use an official Ubuntu runtime as a parent image
FROM ubuntu:23.10

# Set the timezone
RUN ln -fs /usr/share/zoneinfo/America/New_York /etc/localtime

# Install any needed packages specified in requirements.txt
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y tzdata && apt-get install -y \
    gnome-screenshot \
    xvfb \
    x11vnc \
    fluxbox \
    python3 \
    python3-pip \
    curl \
    scrot \
    python3-tk \
    python3-dev \
    git \
    xz-utils

# Create /nix directory and change ownership
RUN mkdir -m 0755 /nix && chown root:root /nix

# Create nixbld group and users for Nix's build operations
RUN groupadd -r nixbld && \
    for i in $(seq 1 10); do \
        useradd -c "Nix build user $i" -d /var/empty -g nixbld -G nixbld -M -N -r -s "$(which nologin)" nixbld$i; \
    done

# Install Nix 2.19.1 in single-user mode
#RUN curl -L https://nixos.org/nix/install | sh
RUN curl -L https://releases.nixos.org/nix/nix-2.19.1/install | sh

# Set up environment for Nix
ENV PATH=/root/.nix-profile/bin:$PATH

# Perform a shallow clone of the Nixpkgs repository at a specific commit
# Replace 'your_commit_hash' with the actual commit hash
RUN git clone --depth 1 --branch master https://github.com/NixOS/nixpkgs.git && \
    cd nixpkgs && \
    git fetch --depth 1 origin 33576fdfce2d11204067d6cfa99a2f990ef2169a && \
    git checkout FETCH_HEAD

# Install packages using the specific version of Nixpkgs
# Example: installing Chromium
RUN nix-env -f /nixpkgs -iA chromium
RUN nix-env -f /nixpkgs -iA nodejs
RUN nix-env -f /nixpkgs -iA tesseract

# Set the working directory in the container to /app
WORKDIR /app

# To run chrome-remote-interface for debug
RUN npm install chrome-remote-interface

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

COPY pyproject.toml .
COPY poetry.lock .
WORKDIR /app/modules
WORKDIR /app
COPY modules/__init__.py modules/

RUN ~/.local/bin/poetry install

#COPY fluxbox/init /root/.fluxbox/init
#COPY fluxbox/menu /root/.fluxbox/menu
#COPY fluxbox/keys /root/.fluxbox/keys
#COPY fluxbox/startup /root/.fluxbox/startup
#COPY fluxbox/apps /root/.fluxbox/apps
#COPY fluxbox/slitlist /root/.fluxbox/slitlist
#COPY fluxbox/styles/Default /root/.fluxbox/styles/Default
#COPY fluxvox/overlay /root/.fluxbox/overlay


# Set environment v   ariable
ENV DISPLAY=:1

# Make port 5900 available to the world outside this container

# Run x11vnc when the container launches
#CMD Xvfb :1 -screen 0 1024x768x16 & x11vnc -display :1 -forever

#RUN apt-get update && apt-get install -y dbus-x11 x11-apps
#RUN dbus-uuidgen > /var/lib/dbus/machine-id

EXPOSE 5900

# Copy the entrypoint script into the container
COPY entrypoint.sh /entrypoint.sh

# RUN entrypoint script
RUN chmod +x /entrypoint.sh

# Set the entrypoint script to be executed
ENTRYPOINT ["/entrypoint.sh"]

# Default command to execute
CMD ["/bin/bash"]
