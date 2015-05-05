+++
title = "Debian changing route: the end of the perfect server linux distribution?"
date = "2007-04-10T11:58:30-04:00"
tags = ["linux"]
+++
<p>From the very little experience I have with <a href="http://www.debian.org/">Debian</a>, and from the stuff I've been reading about it, I think I can safely say Debian has always been a special distribution: packages always take very long to get into the stable tree, because Debian wanted to be a rock solid system where packages go through a lot of testing.  ("We release it when it's done")  The end result is a distro where you don't have the latest software, neither as much flexibility as, say <a href="http://www.gentoo.org/">Gentoo</a> or <a href="http://www.archlinux.org">Arch</a>: You'd many times need to adapt your way of doing things to the "Debian way" (or be prepared to look for help in really obscure places and probably break things) but the end result is a stable distro where everything works very decently.  That, combined with no licensing fees (unlike for example <a href="http://www.redhat.com">Red hat</a>), make it the perfect choice for a server in small companies, where money is more important then features such as professional support or official certifications.</p>

<p>However, it seems like Debian is taking a route that will make it lose it's advantages over other distributions in the server market:<!--more--><br />

On april 8th <a href="http://www.debian.org/News/2007/20070408">Debian released version 4.0</a>.  But very soon an <a href="http://www.linux-watch.com/news/NS5673962628.html">article</a> popped up and drew my attention.<br />

It complains about several problems such as multiple NIC's just not working.  After reading this, I skimmed over <a href="http://www.debian.org/releases/etch/i386/release-notes/ch-information.en.html">"potential problems" in their release notes</a>, and what do we see?  Many small issues that could have been fixed by just taking a bit longer, often accompanied by lines such as "Although<br />

<package x> has been tested extensively, you may experience minor problems...".  Problems varying from devices not being created to environment variables blindly being overwritten.  (Come on, how hard is it too prevent that?)<br />

So Debian is changing their release mechanism (or was this just a one-timer?  Even then it's bad practice), thereby loosing it's major benefits over other distributions on the servermarket.<br />

Personally I don't think issues like these will make server administrators switch to something else, but they'll sure have some work on their hands if they decide to upgrade ;-)</p>