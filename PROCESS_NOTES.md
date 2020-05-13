# Process notes

Not documentation, really ... just notes for me as a go along. Use at your own risk! :-)

## Getting set up with the Pi

I used a the pi that I had used for `pi-photo` (another of my repos).

Connected my Pi to a keyboard, mouse, and my living room TV via HDMI.

Booted up to desktop.

Commented-out the previous auto-startup line in `/etc/rc.local` ... because I no longer want to use my `pi-photo` code on startup.

Opened the terminal on the pi.

Followed the [install instructions for pikrellcam](http://billw2.github.io/pikrellcam/pikrellcam.html).

## Detecting the pi on my network

- Installed `nmap` with `brew install nmap` .
- Confirmed my local area network is based on `10.0.1.*` using Mac's Network Utility from the desktop.
- Did `sudo nmap -sn 10.0.1.0/24`
- Found the IP address of my pi
- Put that into the browser
- Pikrellcam's site came up. So cool.
    - Note that for some reason the page was jumpy until I started the system using System > Start on the page.
- Rebooted the pi

## Shutting Down

Reminding myself that to shut down:

```
sudo shutdown -h now
```

And to reboot:

```
sudo shutdown -r now
```

## Troubleshooting problem with pikrellcam freezing

The camera feed kept freezing on me, and I did some looking into what might be the issue.

One thing I did was go into `.pikrellcam/pikrellcam.conf` and raise the `loop_diskusage_percent` value to 60 — as I had noted that the previous setting was already below what was available on my card.

I also changed `video_width` `video_height` `still_width` `still_height` to make any captures 640 x 480, which is about as big as I need. (Though consdiering making this 512 x 512, since that's what the model was trained on.)

I also added the line `over_voltage=6` in the Pi's `/boot/config.txt` because the internet said that might help.

## Copying "rosebot" Render repo into a new "bird-watcher" repo

Followed [these instructions](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/duplicating-a-repository).

- Made a new Github repo on the Github site, `pi-bird-watcher-render`
- Git a "bare" version of the rosebot repo: `git clone --bare https://github.com/jkeefe/render-fastai-rosebot.git`
- Changed into that bare version directory (note it's like the same one, but has a `.git` in the directory name): `cd render-fastai-rosebot.git`
- Pushed it up to the _new_ repo: `git push --mirror git@github.com:jkeefe/pi-bird-watcher-render.git`
- Backed out of that directory: `cd ..`
- Deleted the temporary bare repo (be SURE to add the .git!): `rm -rf render-fastai-rosebot.git`
- Made a new clone by pulling it down from Github: `git@github.com:jkeefe/pi-bird-watcher-render.git`

## Copy the pikrellcam config file to local drive

```
scp pi@10.0.1.65:.pikrellcam/pikrellcam.conf ./
```

And the other way around:

```
scp pikrellcam.conf pi@10.0.1.65:.pikrellcam/pikrellcam.conf
```