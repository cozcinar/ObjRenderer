# Stanford Shapenet Renderer

A little helper script to render .obj files (such as from the stanford shapenet database) with Blender.

Tested on Linux, but should also work for other operating systems.
By default, this scripts generates 30 images by rotating the camera around the object.
Additionally, depth, albedo and normal maps are dumped for every image.

Tested with Blender 2.79.

## Requirements

```bash
wget https://download.blender.org/release/Blender2.79/blender-2.79a-linux-glibc219-x86_64.tar.bz2
tar -xvf blender-2.79-linux-glibc219-x86_64.tar.bz2

# how to use blender renderer with ssh https://blender.stackexchange.com/questions/144083/how-to-get-blender-2-80-to-render-through-an-ssh-connection-minimal-working-ex

sudo apt install mesa-utils
glxinfo
nvidia-xconfig --query-gpu-info
#Next, we run this, where I insert the PCI BusID into the --busid argument:
sudo nvidia-xconfig --busid=PCI:101:0:0 --use-display-device=none --virtual=1280x1024
# Now, this will be running in one shell. Using CTRL+C will not work to kill it. For your subsequent work, you can use a separate shell.
sudo Xorg :1
# this will set the display variable to be what the Xorg command did in the other shell.
export DISPLAY=:1
# sanitiy check
glxinfo | grep -e render -e NVIDIA
```