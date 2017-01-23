# Lapis Lazuli Mirroring System
_Lapis Lazuli's Mirror didn't disappear; it just ascended into cyberspace._

VelvetBot is a plugin-based service, derived from [kupiakos/LapisMirror](https://github.com/kupiakos/LapisMirror) that imports posted images on r/RWBY,
exports the images onto a mirroring service, then replies with the mirror links.

Currently, VelvetBot imports from the following sites:
* Tumblr (images, photosets, and videos)
* deviantArt
* tinypic
* gyazo
* i.4cdn.org (4chan image hosting)
* Twitter Images
* Artstation
* Drawcrowd
* gifs.com
* puu.sh

It also exports to the following sites:
* imgur for images
* vid.me for videos (in addition to a direct link to the video)

VelvetBot imports modules from a plugin directory dynamically and loads them.
I would recommend reading the class documentation in lapis.py to learn more.

To configure for testing, copy lapis.conf.example to lapis.conf and begin editing.
lapis.conf is the location for all configuration settings for Lapis.
